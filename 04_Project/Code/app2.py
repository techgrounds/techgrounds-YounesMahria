#!/usr/bin/env python3
import os


import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_iam as iam
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_backup as backupService 

from constructs import Construct
from the_mvp_project.the_mvp_project_stack import TheMvpProjectStack

current_max_azs = 1;


class TheMvpProjectStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        # The infrastructure withing the VPC
        # VPC1: App Production VPC
        # Create VPC1: app-prd-vpc
        vpc1 = ec2.Vpc(self, 'AppPrdVPC',
            ip_addresses=ec2.IpAddresses.cidr("10.10.10.0/24"),
            max_azs=current_max_azs,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=26
                ),
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=26
                ),
            ]
        )
        
        

        """
        # Enable CloudHSM for VPC1
        vpc1.enable_nat_gateway()
        vpc1.enable_vpn_gateway()
        vpc1.enable_hardware_cryptographic_module()
        """
        # Get the subnet IDs
        public_subnet_id_vpc1 = vpc1.public_subnets[0].subnet_id
        private_subnet_id_vpc1 = vpc1.isolated_subnets[0].subnet_id
        
        
        # Create EC2 instance in VPC1
        instance1 = ec2.Instance(self, 'EC2InstanceVPC1',
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            vpc=vpc1,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        )
        
        # Create an Elastic IP
        eip1 = ec2.CfnEIP(self, "MyEIP")

        # Associate the Elastic IP with the EC2 instance
        eip1_association = ec2.CfnEIPAssociation(self, "MyEIPAssociation",
            eip=eip1.ref,
            instance_id=instance1.ref
        )
                
        # VPC2: Management Server VPC
        # Create VPC2: management server
        vpc2 = ec2.Vpc(self, 'ManagementServerVPC',
            ip_addresses=ec2.IpAddresses.cidr("10.20.20.0/24"),
            max_azs=current_max_azs,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=26
                ),
            ]
        )
        
        """
        # Enable CloudHSM for VPC2
        vpc2.enable_nat_gateway()
        vpc2.enable_vpn_gateway()
        vpc2.enable_hardware_cryptographic_module()
        """
        # Get the subnet IDs
        public_subnet_id_vpc2 = vpc2.public_subnets[0].subnet_id
        
        
        # Create EC2 instance in VPC2
        instance2 = ec2.Instance(self, 'EC2InstanceVPC2',
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            vpc=vpc2,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        )
        
        # Create an Elastic IP
        eip2 = ec2.CfnEIP(self, "MyEIP")

        # Associate the Elastic IP with the EC2 instance
        eip2_association = ec2.CfnEIPAssociation(self, "MyEIPAssociation",
            eip=eip2.ref,
            instance_id=instance2.ref
        )

        # The Communication between services (VPC's, Internet, Database)
        # Create a VPC peering connection
        VPCPeering_connection = ec2.CfnVPCPeeringConnection(self, "MyCfnVPCPeeringConnection",
            peer_vpc_id=vpc1.vpc_id,
            vpc_id=vpc2.vpc_id,

            # the properties below are optional
            # peer_owner_id="peerOwnerId",
            # peer_region="peerRegion",
            # peer_role_arn="peerRoleArn",
            # tags=[CfnTag(
            #     key="key",
            #     value="value"
            # )]
        )       
        
        
        # Making resources outside of VPC's
        # Create an AWS Backup plan
        
        # Daily, weekly and monthly with 5 year retention
        plan = backupService.BackupPlan.daily_weekly_monthly5_year_retention(self,"Plan");
        
        # Select which resources to backup
        plan.add_selection("Selection",
            resources=[
                #backupService.BackupResource.from_dynamo_db_table(my_table),  # A DynamoDB table
                #backupService.BackupResource.from_rds_database_instance(my_database_instance),  # A RDS instance
                #backupService.BackupResource.from_rds_database_cluster(my_database_cluster),  # A RDS database cluster
                #backupService.BackupResource.from_rds_serverless_cluster(my_serverless_cluster),  # An Aurora Serverless cluster
                #backupService.BackupResource.from_tag("stage", "prod"),  # All resources that are tagged stage=prod in the region/account
                #backupService.BackupResource.from_construct(my_cool_construct)
            ]
        )
        
        
        # plan: backup.BackupPlan
        plan.add_rule(backupService.BackupPlanRule(
            enable_continuous_backup=True,
            #delete_after=14,
            #delete_after=Duration.days(14)
        ))
        
        """
        # Allow traffic from VPC1, AZ1a to VPC2, AZ1a
        vpc1.private_subnets[0].add_route('VPCPeeringConnectionRouteAZ1a',
            router_id=VPCPeering_connection.ref,
            router_type=ec2.RouterType.VPC_PEERING_CONNECTION,
            destination_cidr_block=vpc2.vpc_cidr_block,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE, availability_zones=['eu-central-1a'])
        )

        # Allow traffic from VPC1, AZ1b to VPC2, AZ1b
        vpc1.private_subnets[1].add_route('VPCPeeringConnectionRouteAZ1b',
            router_id=VPCPeering_connection.ref,
            router_type=ec2.RouterType.VPC_PEERING_CONNECTION,
            destination_cidr_block=vpc2.vpc_cidr_block,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE, availability_zones=['eu-central-1b'])
        )

        # Deny traffic from VPC1, AZ1a to VPC2, AZ1b
        vpc1.private_subnets[0].add_route('DenyVPCPeeringConnectionRouteAZ1b',
            router_id='local',
            router_type=ec2.RouterType.LOCAL,
            destination_cidr_block=vpc2.vpc_cidr_block,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE, availability_zones=['eu-central-1b'])
        )
        """
        
        # Create an S3 bucket
        bucket = s3.Bucket(self, 'MVPTechgrounds2023YM',
            bucket_name='mvptechgrounds2023ym'
        )

        # Create IAM Roles
        # Role 1: AppProductPer
        app_product_role = iam.Role(
            self,
            'AppProductPer',
            assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
            role_name='AppProductPer'
        )
        
        app_product_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3FullAccess'))

        # Role 2: ManagementServerPer
        management_server_role = iam.Role(
            self,
            'ManagementServerPer',
            assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
            role_name='ManagementServerPer'
        )
        
        

app = cdk.App()

# Define your region
env_EU = cdk.Environment(region="eu-central-1")

TheMvpProjectStack(app, 'TheMvpProjectStack', env=env_EU)
app.synth()
