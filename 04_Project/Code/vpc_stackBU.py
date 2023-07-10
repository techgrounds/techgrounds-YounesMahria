import aws_cdk as cdk

from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_s3 as s3,
    aws_rds as rds,
    aws_backup as backupService, 
    aws_ecs as ecs,
    aws_elasticloadbalancingv2 as elbv2,
    aws_autoscaling as autoscaling,
    aws_ecs_patterns as ecs_patterns,
    App, CfnOutput, Duration, Stack, 
)


from stack._variables import (
    CURRENT_MAX_AZS,
    LZ_NAME,
    VPC1_CIDR,
    VPC2_CIDR,
    SUBNET_SIZE,
    COOLDOWN,
    OFFICE_IPS,
    HOME_IPS,
)

from constructs import Construct



class VPCStack(cdk.Stack):
    app_prd_vpc = None
    management_prd_vpc = None
    
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        

        # Allocate an Elastic IP address to your account
        eip_app_prd_vpc = ec2.CfnEIP(self, 'EIP_VPC1')
        eip_management_prd_vpc = ec2.CfnEIP(self, 'EIP_VPC2')

        # VPC1: App Production VPC
        # Create VPC1: app-prd-vpc
        app_prd_vpc = ec2.Vpc(self, 'AppPrdVPC',
            vpc_name='app_prd_vpc',
            ip_addresses=ec2.IpAddresses.cidr(VPC1_CIDR),
            max_azs=CURRENT_MAX_AZS,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=SUBNET_SIZE
                ),
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=SUBNET_SIZE
                ),
            ]
        )
        
                
        # Create a VPC endpoint for Amazon S3 in VPC1
        app_prd_vpc.add_gateway_endpoint(
            "S3Endpoint",
            service=ec2.GatewayVpcEndpointAwsService.S3
        )  
        
        # VPC2: Management Server VPC
        # Create VPC2: management server
        management_prd_vpc = ec2.Vpc(self, 'ManagementServerVPC',
            vpc_name='management_prd_vpc',
            ip_addresses=ec2.IpAddresses.cidr(VPC2_CIDR),
            max_azs=CURRENT_MAX_AZS,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=26
                ),
            ]
        )

        # Create a VPC endpoint for Amazon S3 in VPC2
        management_prd_vpc.add_gateway_endpoint(
            "S3Endpoint",
            service=ec2.GatewayVpcEndpointAwsService.S3
        )
        
        # Add a CfnOutput to display the App VPC ID
        # CfnOutput(self, "AppVPCId", value=app_prd_vpc.vpc_id)

        # Add a CfnOutput to display the Management VPC ID
        # CfnOutput(self, "ManagementVPCId", value=management_prd_vpc.vpc_id)
        # EC2 Instance Settings for Global - Settings that are same for every EC2 Instance.
        # use amazon linux as OS
        amzn_linux = ec2.MachineImage.latest_amazon_linux2(edition=ec2.AmazonLinuxEdition.STANDARD,
                                                              virtualization=ec2.AmazonLinuxVirt.HVM,
                                                              storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE)

        amaz_instance_type = 't2.micro';
           
        

        
        # Get the subnets for Frankfurt Availability Zone 1a and 1b
        subnets = app_prd_vpc.select_subnets(availability_zones=['eu-central-1a', 'eu-central-1b']).subnets


        
        #####################        
        # EC2 Instance Settings for VPC1
        #####################
        # secure group
        security_group_web_server = ec2.SecurityGroup(self, "Web Server SecurityGroup",
                                                  vpc=app_prd_vpc  ,
                                                  description="Web Server Security Group from CDK",
                                                  security_group_name="Web Server SecurityGroup",
                                                  allow_all_outbound=True,
                                                  )

        security_group_web_server.add_ingress_rule(ec2.Peer.ipv4(VPC1_CIDR), ec2.Port.tcp(22), "allow ssh access from the VPC")
         
        # Create EC2 instance in VPC1 with autoscaling
        web_server = autoscaling.AutoScalingGroup(self,
                "EC2InstanceVPC1ASG",
                instance_type=ec2.InstanceType(amaz_instance_type),
                machine_image=amzn_linux,
                vpc=app_prd_vpc,
                vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
                security_group=security_group_web_server,
                min_capacity=1,
                max_capacity=2,
                # vpc_subnets=ec2.SubnetSelection(availability_zones=[LZ_NAME],subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
        )
        
        # AutoScaling  CPUpolicy 
        web_server.scale_on_cpu_utilization(
            "CpuScaling",
            target_utilization_percent=80,
            cooldown=Duration.seconds(COOLDOWN),
        )
        
        # Loadbalancer
        lb = elbv2.ApplicationLoadBalancer(self, 'LB',
            vpc=app_prd_vpc,
            internet_facing=True,
        )

        listener = lb.add_listener('Listener', port=80)
        listener.add_targets('Target', port=80, targets=[web_server])
                
        
        # allow web connect
        web_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "allow http from world")
        web_server.connections.allow_from_any_ipv4(ec2.Port.tcp(443), "allow https from world")


        # Create a security group for the RDS instance
        security_group_rds = ec2.SecurityGroup(
            self,
            "RDSSecurityGroup",
            vpc=app_prd_vpc
        )
        
        # Allow traffic from the EC2 instance to the RDS instance
        security_group_rds.add_ingress_rule(
            security_group_web_server,
            ec2.Port.tcp(3306)
        )


        # Associate the Elastic IP address with the EC2 instance on app_prd_vpc
        ec2.CfnEIPAssociation(self, 'EIPAssociation_VPC2',
            eip=eip_app_prd_vpc.ref,
            instance_id='EC2InstanceVPC1ASG',
        )
        

        
        #####################
        # EC2 Instance Settings for VPC2
        #####################
        # secure group
        security_group_management_server = ec2.SecurityGroup(self, "Management Server SecurityGroup",
                                                  vpc=management_prd_vpc  ,
                                                  description="Management Server Security Group from CDK",
                                                  security_group_name="Management Server SecurityGroup",
                                                  allow_all_outbound=True,
                                                  )

        security_group_management_server.add_ingress_rule(ec2.Peer.ipv4(VPC2_CIDR), ec2.Port.tcp(22), "allow ssh access from the VPC")
        
        for office_ip in OFFICE_IPS:
            security_group_management_server.add_ingress_rule(ec2.Peer.ipv4(office_ip), ec2.Port.tcp(22), "allow ssh access from office")
      
        for home_ip in HOME_IPS:
            security_group_management_server.add_ingress_rule(ec2.Peer.ipv4(home_ip), ec2.Port.tcp(22), "allow ssh access from home")
      
        # Create EC2 instance in VPC2
        management_server = ec2.Instance(self, 'EC2InstanceVPC2',
            instance_type=ec2.InstanceType(amaz_instance_type),
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            vpc=management_prd_vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        )
        
        # Allow web connect
        management_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "allow http from world")
        management_server.connections.allow_from_any_ipv4(ec2.Port.tcp(443), "allow https from world")

        # Associate the Elastic IP address with the EC2 instance on management_prd_vpc
        ec2.CfnEIPAssociation(self, 'EIPAssociation_VPC1',
            eip=eip_management_prd_vpc.ref,
            instance_id='EC2InstanceVPC2',
        )
       # Making resources outside of VPC's
        # Create an AWS Backup plan
        # Create a BackupVault
        vault = backupService.BackupVault(self, "Webserver_BackupVault", backup_vault_name="Webserver_Backup_Vault")

        # Create a BackupPlan
        plan = backupService.BackupPlan(self, "AWS-Webserver_Backup-Plan", backup_plan_name="Webserver_Backup")
        
        # Select which resources to backup
        plan.add_selection("Selection", resources=[
            backupService.BackupResource.from_ec2_instance(web_server),
        ])
        
        # Plan: backup.BackupPlan
        plan.add_rule(backupService.BackupPlanRule(
            backup_vault=vault,
            rule_name="Webserver_Backup_Rule",
            completion_window=Duration.hours(2),
            start_window=Duration.hours(1),
            enable_continuous_backup=True,
            delete_after=Duration.days(7),
            schedule_expression=cdk.aws_events.Schedule.cron( # Only cron expressions are supported
                minute='0',
                hour='20')
        ))
        # Create a VPC peering connection between VPC1 and VPC2
        VPCPeering_connection = ec2.CfnVPCPeeringConnection(self, "MyCfnVPCPeeringConnection",
            peer_vpc_id=app_prd_vpc.vpc_id,
            vpc_id=management_prd_vpc.vpc_id,

            # the properties below are optional
            # peer_owner_id="peerOwnerId",
            # peer_region="peerRegion",
            # peer_role_arn="peerRoleArn",
            # tags=[CfnTag(
            #     key="key",
            #     value="value"
            # )]
        )
                        
        # Get the subnets in AZ1a for both VPCs
        app_prd_vpc_subnets_az1a = [subnet for subnet in app_prd_vpc.public_subnets if subnet.availability_zone == 'eu-central-1a']
        management_prd_vpc_subnets_az1a = [subnet for subnet in management_prd_vpc.public_subnets if subnet.availability_zone == 'eu-central-1a']

        # Create a route in VPC1 to route traffic to VPC2 via the peering connection
        for subnet in app_prd_vpc_subnets_az1a:
            route_table = ec2.RouteTable.from_route_table_id(self, f'RouteTable{subnet.subnet_id}', subnet.route_table.route_table_id)
            route_table.create_route(f'Route{subnet.subnet_id}',
                destination_cidr_block=management_prd_vpc.vpc_cidr_block,
                peer=VPCPeering_connection,
            )
        # Create a route in VPC2 to route traffic to VPC1 via the peering connection
        for subnet in management_prd_vpc_subnets_az1a:
            route_table = ec2.RouteTable.from_route_table_id(self, f'RouteTable{subnet.subnet_id}', subnet.route_table.route_table_id)
            route_table.create_route(f'Route{subnet.subnet_id}',
                destination_cidr_block=app_prd_vpc.vpc_cidr_block,
                peer=VPCPeering_connection,
            )    
        
        # Get the subnets in AZ1a for both VPCs
        app_prd_vpc_subnets_az1b = [subnet for subnet in app_prd_vpc.public_subnets if subnet.availability_zone == 'eu-central-1b']
        management_prd_vpc_subnets_az1b = [subnet for subnet in management_prd_vpc.public_subnets if subnet.availability_zone == 'eu-central-1b']

        # Create a route in VPC1 to route traffic to VPC2 via the peering connection
        for subnet in app_prd_vpc_subnets_az1b:
            route_table = ec2.RouteTable.from_route_table_id(self, f'RouteTable{subnet.subnet_id}', subnet.route_table.route_table_id)
            route_table.create_route(f'Route{subnet.subnet_id}',
                destination_cidr_block=management_prd_vpc.vpc_cidr_block,
                peer=VPCPeering_connection,
            )
        # Create a route in VPC2 to route traffic to VPC1 via the peering connection
        for subnet in management_prd_vpc_subnets_az1b:
            route_table = ec2.RouteTable.from_route_table_id(self, f'RouteTable{subnet.subnet_id}', subnet.route_table.route_table_id)
            route_table.create_route(f'Route{subnet.subnet_id}',
                destination_cidr_block=app_prd_vpc.vpc_cidr_block,
                peer=VPCPeering_connection,
            )    


        # Create an RDS instance in the VPC
        rds_instance = rds.DatabaseInstance(self, 'RDSInstance',
            engine=rds.DatabaseInstanceEngine.mysql(
                version=rds.MysqlEngineVersion.VER_8_0_26
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3,
                ec2.InstanceSize.SMALL,
            ),
            vpc=app_prd_vpc,
            security_groups=[security_group_rds],
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            multi_az=False,
            allocated_storage=20,
            storage_type=rds.StorageType.GP2,
            cloudwatch_logs_exports=['error', 'general', 'slowquery'],
            deletion_protection=False,
        )
              