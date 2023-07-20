#!/usr/bin/env python3
import os
import boto3

import aws_cdk as cdk

from aws_cdk import (
    aws_ec2 as ec2,
    aws_autoscaling as autoscaling,
    aws_elasticloadbalancingv2 as elbv2,
    aws_elasticloadbalancingv2_targets as targets,
    aws_certificatemanager as acm,
    aws_cloudwatch as cloudwatch,
    
    App, CfnOutput, Duration, Stack, 

)

from constructs import Construct


from stack._variables import (
    AMAZ_INSTANCE_TYPE,
    AMAZ_LINUX_MACHINE_TYPE,
    AMAZ_LINUX_INSTANCE_TYPE,
    USER_DATA,
    COOLDOWN,
    AMI_NAME,
)

class AutoScalingGroupStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, security_group_stack, ec2_stack, iam_stack, ssh_stack, certificate_stack, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        app_prd_vpc = vpc_stack.app_prd_vpc
        security_group_web_server = security_group_stack.security_group_web_server
        security_group_load_balancer = security_group_stack.security_group_load_balancer
        ec2_app_prd_key = ssh_stack.ec2_app_prd_key
        server_certificate_arn = certificate_stack.server_certificate_arn


        # Check if the AMI ID is valid
        # Create an Auto Scaling group with AMI
        web_server_auto_scaling_group = autoscaling.AutoScalingGroup(
            self,
            "AutoScalingGroup",
            auto_scaling_group_name="Webserver",
            vpc=app_prd_vpc,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
            machine_image=ec2.MachineImage.generic_linux({"eu-central-1": "ami-03f8da27a5f138bc4"}), 
            #machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
            user_data=USER_DATA,
            key_name=ec2_app_prd_key,
            security_group=security_group_web_server,
            min_capacity=1,
            max_capacity=3,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            block_devices=[
                autoscaling.BlockDevice(
                    device_name="/dev/xvda",
                    volume=autoscaling.BlockDeviceVolume.ebs(20, encrypted=True)
                )
            ],
            health_check=autoscaling.HealthCheck.elb(grace=Duration.seconds(300)),
        )
        
        # Tag the instances launched by the Auto Scaling group
        web_server_auto_scaling_group.node.default_child.add_property_override("Tags", [{
            "Key": "Name",
            "Value": "web_server",
            "PropagateAtLaunch": True
        }])

        
        # Create a Metric object for the CPU utilization of the instances in the Auto Scaling group
        cpu_metric = cloudwatch.Metric(
            namespace="AWS/EC2",
            metric_name="CPUUtilization",
            dimensions_map={"AutoScalingGroupName": web_server_auto_scaling_group.auto_scaling_group_name},
            statistic="Average",
        )

    
        # Configure a step scaling policy to scale out when CPU utilization exceeds 80% or 30%
        scaling_policy = web_server_auto_scaling_group.scale_on_metric(
            "ScalingPolicy",
            metric=cpu_metric,
            scaling_steps=[
                autoscaling.ScalingInterval(upper=30, change=-1),
                autoscaling.ScalingInterval(lower=70, change=1),
            ],
            adjustment_type=autoscaling.AdjustmentType.CHANGE_IN_CAPACITY,
        )
                        
        self.web_server_auto_scaling_group = web_server_auto_scaling_group
        
        
        ###############################
        # Load Balancer for Webserver #
        ###############################
        
        webserver_lb = elbv2.ApplicationLoadBalancer(self, "WebServerLB",
            vpc=app_prd_vpc,
            internet_facing=True,
            load_balancer_name="WebServerLB",
            security_group=security_group_load_balancer,
        )
        
        # Output the Public IP (DNS Name) of the load balancer:
        CfnOutput(self, "WebServer_Public_IP", value=webserver_lb.load_balancer_dns_name)
    
        # Create Target Group for Webserver:
        target_group_webserver = elbv2.ApplicationTargetGroup(self, "TargetGroupWebserver",
            target_group_name="TargetGroupWebserver",
            vpc=app_prd_vpc,
            port=80,
            protocol=elbv2.ApplicationProtocol.HTTP,
            target_type=elbv2.TargetType.INSTANCE,
            targets=[web_server_auto_scaling_group],
            health_check=elbv2.HealthCheck( 
                port="80",
                protocol=elbv2.Protocol.HTTP,
                path="/",
                timeout=Duration.seconds(5),
                healthy_threshold_count=2,
                unhealthy_threshold_count=6,
                interval=Duration.seconds(10)
            )
        )
        
        # Import an existing SSL certificate
        certificate = acm.Certificate.from_certificate_arn(
            self,
            "Certificate",
            certificate_arn="arn:aws:acm:eu-central-1:397793253523:certificate/eb703dad-bda0-4a8c-b4bc-b8462891c02d",
        )
        
        # Link ELB to Web Server:
        listener = webserver_lb.add_listener("Listener", 
            default_target_groups=[target_group_webserver], 
            protocol=elbv2.ApplicationProtocol.HTTPS,
            port=443,
            ssl_policy=elbv2.SslPolicy.RECOMMENDED, 
            certificates=[elbv2.ListenerCertificate.from_arn(server_certificate_arn)],
            #certificates=[certificate]
        )
        
        
        listener.connections.allow_from_any_ipv4(
            ec2.Port.tcp(80), "Allow HTTP from All")
        
        listener.connections.allow_to_any_ipv4(
            ec2.Port.tcp(80), "Allow HTTP to All")

        listener.connections.allow_to_any_ipv4(
            ec2.Port.tcp(443), "Allow HTTPS to All")
        

        # Redirect HTTP to HTTPS: -> To make it work, change protocol of listener to HTTPS, and add certificate.
        webserver_lb.add_redirect(
            source_protocol=elbv2.ApplicationProtocol.HTTP,
            source_port=80,
            target_protocol=elbv2.ApplicationProtocol.HTTPS,
            target_port=443,
        )   
        
        # Define the TLS security policy
        tls_policy = elbv2.SslPolicy.FORWARD_SECRECY_TLS12_RES

        # Set the TLS security policy for the HTTPS listener
        listener.ssl_policy = tls_policy