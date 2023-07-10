#!/usr/bin/env python3
import os

import aws_cdk as cdk
#import cdk.aws_events.Schedule as Schedule

from aws_cdk import (
    aws_ec2 as ec2,
    aws_autoscaling as autoscaling,
    App, CfnOutput, Duration, Stack, 
)

from constructs import Construct

from stack._variables import (
    COOLDOWN,
    AMAZ_INSTANCE_TYPE,
    AMAZ_LINUX,
)

class AutoScalingGroupStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, security_group_stack, ec2_stack, iam_stack, ssh_stack, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        app_prd_vpc = vpc_stack.app_prd_vpc
        management_prd_vpc = vpc_stack.management_prd_vpc
        security_group_web_server = security_group_stack.security_group_web_server
        security_group_rds = security_group_stack.security_group_rds
        web_server = ec2_stack.web_server
        ec2_app_prd_key = ssh_stack.ec2_app_prd_key
        ec2_app_prd_key_pair = ssh_stack.ec2_app_prd_key_pair
        ec2_management_prd_key = ssh_stack.ec2_management_prd_key
        ec2_management_prd_key_pair = ssh_stack.ec2_management_prd_key_pair
        app_product_role = iam_stack.app_product_role
        management_server_role = iam_stack.management_server_role

       
        # Create EC2 instance in VPC1 with autoscaling
        web_server_autoscaling = autoscaling.AutoScalingGroup(
            self,
            "EC2InstanceVPC1ASG",
            instance_type=ec2.InstanceType(AMAZ_INSTANCE_TYPE),
            machine_image=AMAZ_LINUX,
            vpc=app_prd_vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            security_group=security_group_web_server,
            min_capacity=1,
            max_capacity=2,
            role=app_product_role,
            #instance_id=web_server.instance_id,  # Target the existing web_server instance
        )
        
        # AutoScaling CPU policy
        web_server_autoscaling.scale_on_cpu_utilization(
            "CpuScaling",
            target_utilization_percent=80,
            cooldown=Duration.seconds(COOLDOWN),
        )
