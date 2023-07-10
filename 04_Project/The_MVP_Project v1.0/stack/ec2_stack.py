import os

import aws_cdk as cdk

from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct

from stack._variables import (
    AMAZ_INSTANCE_TYPE,
    AMAZ_LINUX,
    USER_DATA,
    AMAZ_WINDOWS,
)

class EC2InstanceStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, security_group_stack, ssh_stack, iam_stack, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        app_prd_vpc = vpc_stack.app_prd_vpc
        management_prd_vpc = vpc_stack.management_prd_vpc
        security_group_web_server = security_group_stack.security_group_web_server
        security_group_management_server = security_group_stack.security_group_management_server
        security_group_rds = security_group_stack.security_group_rds
        ec2_app_prd_key = ssh_stack.ec2_app_prd_key
        ec2_app_prd_key_pair = ssh_stack.ec2_app_prd_key_pair
        ec2_management_prd_key = ssh_stack.ec2_management_prd_key
        ec2_management_prd_key_pair = ssh_stack.ec2_management_prd_key_pair
        app_product_role = iam_stack.app_product_role
        management_server_role = iam_stack.management_server_role

        # Create an EC2 instance for the web server
        web_server = ec2.Instance(self,
            "web_server",
            instance_name="web_server",
            instance_type=ec2.InstanceType(AMAZ_INSTANCE_TYPE),
            machine_image=AMAZ_LINUX,
            key_name=ec2_app_prd_key,
            vpc=app_prd_vpc,
            security_group=security_group_web_server,
            user_data=ec2.UserData.custom(USER_DATA),
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            role=app_product_role,
        )

        # Allow inbound traffic on port 80 from the private IP address of the admin server
        web_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "allow http from world")
        web_server.connections.allow_from_any_ipv4(ec2.Port.tcp(443), "allow https from world")

        # Create an EC2 instance for the management server
        management_server = ec2.Instance(self,
            id="management_server",
            instance_name="management_server", 
            instance_type=ec2.InstanceType(AMAZ_INSTANCE_TYPE),
            machine_image=AMAZ_WINDOWS,
            key_name=ec2_management_prd_key,
            vpc=management_prd_vpc,
            security_group=security_group_management_server,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            role=management_server_role,
        )
        
        # Allow web connect
        management_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "allow http from world")
        management_server.connections.allow_from_any_ipv4(ec2.Port.tcp(443), "allow https from world")

        self.web_server = web_server
        self.management_server = management_server
        
        
        # Allocate an Elastic IP address for VPC1 - Web Server
        # eip_app_prd_vpc = ec2.CfnEIP(self, 'EIP_VPC1')

        # Associate the Elastic IP address with the web server instance
        #ec2.CfnEIPAssociation(self,
        #    "EIPAssociation",
        #    #eip=eip_app_prd_vpc.ref,
        #    instance_id=web_server.instance_id)
