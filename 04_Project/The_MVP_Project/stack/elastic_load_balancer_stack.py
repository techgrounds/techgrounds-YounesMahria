#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk import (
    aws_elasticloadbalancingv2 as elbv2,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origin,
    aws_ec2 as ec2,
    aws_elasticloadbalancingv2 as elbv2,
    aws_elasticloadbalancingv2_targets as targets,

    App, CfnOutput, Duration, Stack, 
)

from stack._variables import (
    AMAZ_INSTANCE_TYPE,
    AMAZ_LINUX,
    USER_DATA,
    AMAZ_WINDOWS,
    COOLDOWN
)

from constructs import Construct

class ElasticLoadBalancerStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, security_group_stack, ec2_stack, iam_stack, certificate_stack, auto_scaling_group_stack, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        app_prd_vpc = vpc_stack.app_prd_vpc
        management_prd_vpc = vpc_stack.management_prd_vpc
        #proxy_server = ec2_stack.proxy_server
        management_server = ec2_stack.management_server
        app_product_role = iam_stack.app_product_role
        management_server_role = iam_stack.management_server_role
        security_group_web_server = security_group_stack.security_group_web_server
        server_certificate_arn = certificate_stack.server_certificate_arn
        web_server_auto_scaling_group = auto_scaling_group_stack.web_server_auto_scaling_group
        security_group_load_balancer = security_group_stack.security_group_load_balancer
    

        # Create an Application Load Balancer
        elb_web_server = elbv2.ApplicationLoadBalancer(self, "ALB",
            load_balancer_name="Proxy-Server",
            vpc=app_prd_vpc,
            internet_facing=True,
            security_group=security_group_load_balancer,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        )
        
        # Create a target group for the web server instances in the Auto Scaling group
        target_group_webserver = elbv2.ApplicationTargetGroup(
            self,
            "WebServerTargetGroup",
            target_group_name="TargetGroupWebserver",
            vpc=app_prd_vpc,
            port=80, #443
            protocol=elbv2.ApplicationProtocol.HTTP,
            target_type=elbv2.TargetType.INSTANCE,
            targets=[web_server_auto_scaling_group],
            health_check=elbv2.HealthCheck(
                protocol=elbv2.Protocol.HTTP,
                port="80", #443
                path="/",
                timeout=cdk.Duration.seconds(5),
                healthy_threshold_count=2,
                unhealthy_threshold_count=6,
                interval=cdk.Duration.seconds(10)
            )
        )

        # Create a listener for HTTP traffic on port 80 and add the target group
        http_listener = elb_web_server.add_listener("HTTPListener",
            port=80,
            protocol=elbv2.ApplicationProtocol.HTTP,
            #default_action=elbv2.ListenerAction.forward(target_groups=[target_group]),
            open=True
        )


        # Output the load balancer DNS name
        cdk.CfnOutput(
            self,
            "LoadBalancerDNS",
            value=elb_web_server.load_balancer_dns_name
        )

        # Configure the HTTP Listener to redirect requests to HTTPS
        http_listener.add_action(
            "HTTPSRedirect",
            action=elbv2.ListenerAction.redirect(
                protocol="HTTPS",
                port="443",
                host="#{host}",
                path="/#{path}",    
                query="#{query}",
            ),
        )

        # Create a listener for HTTPS traffic on port 443 and set TLS policy
        https_listener = elb_web_server.add_listener("HTTPSListener",
            port=443,
            protocol=elbv2.ApplicationProtocol.HTTPS,
            certificates=[elbv2.ListenerCertificate.from_arn(server_certificate_arn)],
            #default_action=elbv2.ListenerAction.forward(target_groups=[target_group])
            default_target_groups=[target_group_webserver]
        )

        # Define the TLS security policy
        tls_policy = elbv2.SslPolicy.FORWARD_SECRECY_TLS12_RES

        # Set the TLS security policy for the HTTPS listener
        https_listener.ssl_policy = tls_policy


        #### Management Server
        """       

        # Create a new Network Load Balancer in the management_prd_vpc
        nlb_management_server = elbv2.NetworkLoadBalancer(self, "ManagementNLB",
            load_balancer_name="ManagementServer",
            vpc=management_prd_vpc,
            internet_facing=True,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        )

        # Create a target group for the management server
        target_group_management = elbv2.NetworkTargetGroup(
            self,
            "ManagementTargetGroup",
            target_group_name="TargetGroupManagement",
            vpc=management_prd_vpc,
            port=3389,
            protocol=elbv2.Protocol.TCP,
            target_type=elbv2.TargetType.INSTANCE,
            targets=[management_server],
            health_check=elbv2.HealthCheck(
                protocol=elbv2.Protocol.TCP,
                port="3389",
                timeout=cdk.Duration.seconds(5),
                healthy_threshold_count=2,
                unhealthy_threshold_count=6,
                interval=cdk.Duration.seconds(10)
            )
        )

        # Create a listener for RDP traffic on port 3389 and add the target group
        rdp_listener = nlb_management_server.add_listener("RDPListener",
            port=3389,
            protocol=elbv2.Protocol.TCP,
            default_target_groups=[target_group_management]
        )
        """       

        """       
        # Add the target group to the load balancer
        listener = elb_web_server.add_listener(
            "MyListener",
            port=80,
            open=True,
        )
        """