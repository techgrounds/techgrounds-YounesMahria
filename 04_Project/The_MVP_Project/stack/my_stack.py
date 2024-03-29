#!/usr/bin/env python3
import os

import aws_cdk as cdk
import boto3
#import cdk.aws_events.Schedule as Schedule

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

from .ami_stack import AMIStack
from .s3_stack import S3Stack
from .iam_stack import IAMStack
from .ssh_stack import SSHStack
from .certificate_stack import CertificateStack
from .security_group_stack import SecurityGroupStack
from .rds_stack import RdsStack
from .vpc_stack import VPCStack
from .vpcpeerconnection_stack import VPCPeerConnectionStack
from .ec2_stack import EC2InstanceStack
from .lambda_stack import LambdaStack
from .auto_scaling_group_stack import AutoScalingGroupStack
from .backup_plan import BackupPlanStack
from constructs import Construct

from stack._variables import (
    CURRENT_MAX_AZS,
    LZ_NAME,
    VPC1_CIDR,
    VPC2_CIDR,
    SUBNET_SIZE,
    COOLDOWN,
    OFFICE_IPS,
    HOME_IPS,
    VPC1_PUBLIC_CIDR,
    VPC1_PRIVATE_CIDR,
    VPC2_PUBLIC_CIDR,
    VPC2_PRIVATE_CIDR,
)

class TheMvpProjectStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #####################
        # The infrastructureW
        ####################
        # IMPORTANT: Some stacks are required/dependent from other(s).
        
        # Independent stacks:
        s3_stack = S3Stack(self, "S3Stack") # Creates S3 Bucket, No reference needed
        iam_stack = IAMStack(self, "IAMStack") # Creates IAM Roles, No reference needed  
        vpc_stack = VPCStack(self, "VPCStack") # Creates VPC, No reference needed
        ssh_stack = SSHStack(self, "SSHStack") # Creates SSH, No reference needed
        certificate_stack = CertificateStack(self, "CertificateStack") # Creates Certificate, No reference needed
        
        # Dependent  stacks: 
        vpcpeerconnection_stack = VPCPeerConnectionStack(self, "VPCPeerConnectionStack", vpc_stack=vpc_stack)  # Creates VPC Peering, Reference needed: vpc_stack
        security_group_stack = SecurityGroupStack(self, "SecurityGroupStack",vpc_stack=vpc_stack) # Creates Security, Reference needed: vpc_stack
        #ami_stack = AMIStack(self, "AMIStack", vpc_stack=vpc_stack, security_group_stack=security_group_stack, ssh_stack=ssh_stack, iam_stack=iam_stack) # Creates AMI from the EC2 Instance for Webserver later, No reference needed
        rds_stack = RdsStack(self, "RdsStack", vpc_stack=vpc_stack, security_group_stack=security_group_stack) # Creates RDS, Reference needed: vpc_stack, security_group_stack
        ec2_stack = EC2InstanceStack(self, "EC2InstanceStack", vpc_stack=vpc_stack, security_group_stack=security_group_stack, ssh_stack=ssh_stack, iam_stack=iam_stack) # Creates EC2 Instance, Reference needed: vpc_stack, security_group_stack        
        auto_scaling_group_stack = AutoScalingGroupStack(self, "AutoScalingGroupStack", vpc_stack=vpc_stack, security_group_stack=security_group_stack, ec2_stack=ec2_stack, iam_stack=iam_stack, ssh_stack=ssh_stack, certificate_stack=certificate_stack) # Creates EC2 Instance, Reference needed: vpc_stack, security_group_stack
        backup_plan_stack = BackupPlanStack(self, "BackupPlanStack", ec2_stack=ec2_stack)  # Creates AWS Backup Plan, Reference needed: ec2_stack
        
        