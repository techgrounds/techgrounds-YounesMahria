import aws_cdk as cdk

from aws_cdk import (
    aws_ec2 as ec2,
    App, CfnOutput, Duration, Stack, 
)

from constructs import Construct

class ElasticIPStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        

        # Allocate an Elastic IP address to your account
        eip_app_prd_vpc = ec2.CfnEIP(self, 'eip_app_prd_vpc')
        #eip_management_prd_vpc = ec2.CfnEIP(self, 'eip_management_prd_vpc')