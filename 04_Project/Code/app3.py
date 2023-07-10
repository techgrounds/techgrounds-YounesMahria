#!/usr/bin/env python3
import os

"""
import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_iam as iam
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_backup as backupService 
"""

import aws_cdk as cdk
#import cdk.aws_events.Schedule as Schedule

from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_s3 as s3,
    aws_backup as backupService, 
    aws_ecs as ecs,
    aws_elasticloadbalancingv2 as elbv2,
    aws_autoscaling as autoscaling,
    aws_ecs_patterns as ecs_patterns,
    App, CfnOutput, Duration, Stack, 
)



from constructs import Construct
from the_mvp_project.the_mvp_project_stack import TheMvpProjectStack

CURRENT_MAX_AZS = 1;
LZ_NAME = "eu-central" # Local Zone to be used
VPC1_CIDR = "10.10.10.0/24" # VPC CIDR that will be used to create a new VPC
VPC2_CIDR = "10.20.20.0/24" # VPC CIDR that will be used to create a new VPC
SUBNET_SIZE = 26 # Subnet size of the subnets in the Local Zone


class TheMvpProjectStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #####################
        # The infrastructure withing the VPC
        #####################
        
        # EC2 Instance Settings for Global - Settings that are same for every EC2 Instance.
        # use amazon linux as OS
        amzn_linux = ec2.MachineImage.latest_amazon_linux2(edition=ec2.AmazonLinuxEdition.STANDARD,
                                                              virtualization=ec2.AmazonLinuxVirt.HVM,
                                                              storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE)

        amaz_instance_type = 't2.micro';
        
        # VPC1: App Production VPC
        # Create VPC1: app-prd-vpc
        vpc1 = ec2.Vpc(self, 'AppPrdVPC',
            ip_addresses=ec2.IpAddresses.cidr(VPC1_CIDR),
            max_azs=CURRENT_MAX_AZS,
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
        
        #####################        
        # EC2 Instance Settings for VPC1
        #####################
        # secure group
        security_group_web_server = ec2.SecurityGroup(self, "Web Server SecurityGroup",
                                                  vpc=vpc1  ,
                                                  description="Web Server Security Group from CDK",
                                                  security_group_name="Web Server SecurityGroup",
                                                  allow_all_outbound=True,
                                                  )

        security_group_web_server.add_ingress_rule(ec2.Peer.ipv4(VPC1_CIDR), ec2.Port.tcp(22), "allow ssh access from the VPC")
        
        # Create EC2 instance in VPC1
        """        
        web_server = ec2.Instance(self, 'EC2InstanceVPC1',
            instance_type=ec2.InstanceType(amaz_instance_type),
            machine_image=amzn_linux,
            vpc=vpc1,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            security_group=security_group_web_server,
            #key_name="Your SSH key pair name"
        )
        """
        # Create EC2 instance in VPC1 with autoscaling
        web_server = autoscaling.AutoScalingGroup(self,
                "EC2InstanceVPC1ASG",
                instance_type=ec2.InstanceType(amaz_instance_type),
                machine_image=amzn_linux,
                vpc=vpc1,
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
            cooldown=Duration.seconds(300),
        )
        
        # allow web connect
        web_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "allow http from world")
        web_server.connections.allow_from_any_ipv4(ec2.Port.tcp(443), "allow https from world")

        # Create an Elastic IP
        eip1 = ec2.CfnEIP(self, "MyEIP1")

        # Associate the Elastic IP with the EC2 instance
        # eip1_association = ec2.CfnEIPAssociation(self, "MyEIPAssociation",
        #     eip=eip1.ref,
        #     instance_id=web_server.ref
        # )
                
        # VPC2: Management Server VPC
        # Create VPC2: management server
        vpc2 = ec2.Vpc(self, 'ManagementServerVPC',
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
        
        #####################
        # EC2 Instance Settings for VPC2
        #####################
        # secure group
        security_group_management_server = ec2.SecurityGroup(self, "Management Server SecurityGroup",
                                                  vpc=vpc2  ,
                                                  description="Management Server Security Group from CDK",
                                                  security_group_name="Management Server SecurityGroup",
                                                  allow_all_outbound=True,
                                                  )

        security_group_management_server.add_ingress_rule(ec2.Peer.ipv4(VPC2_CIDR), ec2.Port.tcp(22), "allow ssh access from the VPC")
 
        # Create EC2 instance in VPC2
        management_server = ec2.Instance(self, 'EC2InstanceVPC2',
            instance_type=ec2.InstanceType(amaz_instance_type),
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            vpc=vpc2,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        )
        
        # Allow web connect
        management_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "allow http from world")
        management_server.connections.allow_from_any_ipv4(ec2.Port.tcp(443), "allow https from world")

        
        # Create an Elastic IP
        eip2 = ec2.CfnEIP(self, "MyEIP2")

        # Associate the Elastic IP with the EC2 instance
        # eip2_association = ec2.CfnEIPAssociation(self, "MyEIPAssociation",
        #     eip=eip2.ref,
        #     instance_id=management_server.ref
        # )

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
        
        management_server_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('AWSCodeBuildAdminAccess'))
        

app = cdk.App()

# Define your region
env_EU = cdk.Environment(region="eu-central-1")

TheMvpProjectStack(app, 'TheMvpProjectStack', env=env_EU)
app.synth()
