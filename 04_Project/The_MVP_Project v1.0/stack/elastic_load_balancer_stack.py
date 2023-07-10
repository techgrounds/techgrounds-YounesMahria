#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk import (
    aws_elasticloadbalancingv2 as elbv2,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origin,
    App, CfnOutput, Duration, Stack, 
)

from constructs import Construct

class ElasticLoadBalancerStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, security_group_stack, ec2_stack, iam_stack,   **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        app_prd_vpc = vpc_stack.app_prd_vpc
        web_server = ec2_stack.web_server
        app_product_role = iam_stack.app_product_role
        management_server_role = iam_stack.management_server_role


        # Load balancer
        web_server_alb = elbv2.ApplicationLoadBalancer(self, 'web_server_elb',
            vpc=app_prd_vpc,
            internet_facing=True,
        )

        cloudfront.Distribution(self, "myDist",
        default_behavior=cloudfront.BehaviorOptions(origin=origin.LoadBalancerV2Origin(web_server_alb))
        )

        #web_server_alb.add_listener('Listener', port=80)
        #web_server_alb.add_targets('Target', port=80, targets=[web_server])
