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
    AMAZ_LINUX,
    USER_DATA,
    PROXY_USER_DATA,
    AMAZ_WINDOWS,
    COOLDOWN
)

class EC2InstanceStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, security_group_stack, ssh_stack, iam_stack, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        app_prd_vpc = vpc_stack.app_prd_vpc
        management_prd_vpc = vpc_stack.management_prd_vpc
        
        security_group_proxy_server = security_group_stack.security_group_proxy_server       
        security_group_web_server = security_group_stack.security_group_web_server
        security_group_management_server = security_group_stack.security_group_management_server
        security_group_rds = security_group_stack.security_group_rds
        
        
        ec2_app_prd_key = ssh_stack.ec2_app_prd_key
        ec2_app_prd_key_pair = ssh_stack.ec2_app_prd_key_pair
        ec2_management_prd_key = ssh_stack.ec2_management_prd_key
        ec2_management_prd_key_pair = ssh_stack.ec2_management_prd_key_pair
        app_product_role = iam_stack.app_product_role
        management_server_role = iam_stack.management_server_role


        # Create an EC2 instance for the management server
        management_server = ec2.Instance(self,
            id="management_server",
            instance_name="management_server", 
            instance_type=ec2.InstanceType(AMAZ_INSTANCE_TYPE),
            machine_image=AMAZ_WINDOWS,
            key_name=ec2_management_prd_key,
            vpc=management_prd_vpc,
            security_group=security_group_management_server,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            role=management_server_role,
        )
        
        # self.web_server = web_server
        self.management_server = management_server
        #self.proxy_server = proxy_server