import os

import boto3

import aws_cdk as cdk

from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_elasticloadbalancingv2 as elbv2,
    aws_elasticloadbalancingv2_targets as targets,
    aws_autoscaling as autoscaling,
    aws_certificatemanager as acm,
    aws_cloudwatch as cloudwatch,

)

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
import datetime

from constructs import Construct

from stack._variables import (
    AMAZ_INSTANCE_TYPE,
    AMAZ_LINUX_INSTANCE_TYPE,
    AMAZ_LINUX_MACHINE_TYPE,
    USER_DATA,
    PROXY_USER_DATA,
    AMAZ_WINDOWS_MACHINE_TYPE,
    WINDOWS_USER_DATA,
    AMAZ_WINDOWS_INSTANCE_TYPE,
    COOLDOWN,
    
)

class EC2InstanceStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, security_group_stack, ssh_stack, iam_stack, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        app_prd_vpc = vpc_stack.app_prd_vpc
        management_prd_vpc = vpc_stack.management_prd_vpc
        
        #security_group_proxy_server = security_group_stack.security_group_proxy_server       
        security_group_web_server = security_group_stack.security_group_web_server
        security_group_management_server = security_group_stack.security_group_management_server
        security_group_rds = security_group_stack.security_group_rds
        
        
        ec2_app_prd_key = ssh_stack.ec2_app_prd_key
        ec2_app_prd_key_pair = ssh_stack.ec2_app_prd_key_pair
        ec2_management_prd_key = ssh_stack.ec2_management_prd_key
        ec2_management_prd_key_pair = ssh_stack.ec2_management_prd_key_pair
        app_product_role = iam_stack.app_product_role
        management_server_role = iam_stack.management_server_role


        """
        webserver = ec2.Instance(
            self,
            id="webserver",
            instance_name="webserver",
            vpc=app_prd_vpc,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
            machine_image=AMAZ_LINUX_MACHINE_TYPE,
            user_data=USER_DATA,
            #key_name=ec2_app_prd_key,
            #security_group=security_group_web_server,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/sda1",
                    volume=ec2.BlockDeviceVolume.ebs(20, encrypted=True)
                )
            ],
        )
        """
        """
        
        webserver_instance = ec2.Instance(
                self, "WebServerTemplate",
                vpc=ec2.Vpc.from_lookup(self, "DefaultVPC", is_default=True),
                instance_name="WebServerTemplate",
                instance_type=ec2.InstanceType('t3.nano'),
                machine_image=ec2.MachineImage.latest_amazon_linux2(),
                key_name="WebServerKey", # Imports the key pair. Make sure you create the key pair first!')
                user_data=USER_DATA,
                block_devices=[
                    ec2.BlockDevice(
                        device_name='/dev/xvda',
                        volume=ec2.BlockDeviceVolume.ebs(
                            volume_size=20,
                            encrypted=True,
                        ))
                ]
        )
        """

        # bastion server
        # Create an EC2 instance for the management server
        management_server = ec2.Instance(self,
            id="management_server",
            instance_name="management_server", 
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
            machine_image=AMAZ_WINDOWS_MACHINE_TYPE,
            user_data=WINDOWS_USER_DATA,
            key_name=ec2_management_prd_key,
            vpc=management_prd_vpc,
            security_group=security_group_management_server,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            role=management_server_role,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/sda1",
                    volume=ec2.BlockDeviceVolume.ebs(30, encrypted=True)
                )
            ],
        )

        self.management_server = management_server
        
        
        """
        from aws_cdk import (
    aws_ec2 as ec2,
    core,
)

class BastionStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a security group for the bastion server
        bastion_sg = ec2.SecurityGroup(self, "BastionSG",
            vpc=vpc,
            allow_all_outbound=True,
            description="Allow RDP access from anywhere",
        )

        # Allow RDP access from anywhere
        bastion_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description="Allow RDP access from anywhere",
        )

        # Create a bastion server instance
        bastion = ec2.BastionHostLinux(self, "Bastion",
            vpc=vpc,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            instance_name="Bastion",
            instance_type=ec2.InstanceType("t3.micro"),
            security_group=bastion_sg,
        )

        # Install and configure RD Gateway on the bastion server
        bastion.user_data.add_commands(
            # Add commands here
        )

        """