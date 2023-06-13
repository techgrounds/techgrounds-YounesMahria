#!/usr/bin/env python3
import os

import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_iam as iam
import aws_cdk.aws_s3 as s3

from the_mvp_project.the_mvp_project_stack import TheMvpProjectStack
from aws_cdk import core


app = cdk.App()
TheMvpProjectStack(app, "TheMvpProjectStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()

class MyStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create VPC1: app-prd-vpc
        vpc1 = ec2.Vpc(self, 'AppPrdVPC',
            cidr='10.10.10.0/24',
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(name='Public', subnet_type=ec2.SubnetType.PUBLIC, cidr_mask=24),
                ec2.SubnetConfiguration(name='Private', subnet_type=ec2.SubnetType.ISOLATED, cidr_mask=24),
            ]
        )

        # Enable CloudHSM for VPC1
        vpc1.enable_nat_gateway()
        vpc1.enable_vpn_gateway()
        vpc1.enable_hardware_cryptographic_module()
        
        # Get the subnet IDs
        public_subnet_id = vpc1.public_subnets[0].subnet_id
        private_subnet_id = vpc1.isolated_subnets[0].subnet_id

        # Create EC2 instance in VPC1
        instance1 = ec2.Instance(self, 'EC2InstanceVPC1',
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            vpc=vpc1,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        )

        # Create VPC2: management server
        vpc2 = ec2.Vpc(self, 'ManagementServerVPC',
            cidr='10.20.20.0/24',
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(name='Public', subnet_type=ec2.SubnetType.PUBLIC, cidr_mask=24),
            ]
        )

        # Enable CloudHSM for VPC2
        vpc2.enable_nat_gateway()
        vpc2.enable_vpn_gateway()
        vpc2.enable_hardware_cryptographic_module()
        
        # Get the subnet IDs
        public_subnet_id_vpc2 = vpc2.public_subnets[0].subnet_id

        # Create EC2 instance in VPC2
        instance2 = ec2.Instance(self, 'EC2InstanceVPC2',
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            vpc=vpc2,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        )

        # Create a VPC peering connection
        peering_connection = ec2.CfnVPCPeeringConnection(self, 'VPCPeeringConnection',
            vpc_id=vpc1.vpc_id,
            peer_vpc_id=vpc2.vpc_id,
            peer_region=core.Aws.REGION,
            peer_role_arn=vpc2.vpc_peer_role.role_arn
        )

        # Allow traffic from VPC1, AZ1a to VPC2, AZ1a
        vpc1.private_subnets[0].add_route('VPCPeeringConnectionRouteAZ1a',
            router_id=peering_connection.ref,
            router_type=ec2.RouterType.VPC_PEERING_CONNECTION,
            destination_cidr_block=vpc2.vpc_cidr_block,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE, availability_zones=['eu-central-1a'])
        )

        # Allow traffic from VPC1, AZ1b to VPC2, AZ1b
        vpc1.private_subnets[1].add_route('VPCPeeringConnectionRouteAZ1b',
            router_id=peering_connection.ref,
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

app = core.App()
MyStack(app, 'MyStack')
app.synth()