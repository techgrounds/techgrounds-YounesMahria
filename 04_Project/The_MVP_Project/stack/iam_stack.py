import aws_cdk as cdk

from aws_cdk import (
    aws_iam as iam,
    App, CfnOutput, Duration, Stack, 
)

from constructs import Construct

class IAMStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # Create IAM Roles
        # Role 1: AppProductPer
        app_product_role = iam.Role(
            self,
            'AppProductPer',
            assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
            role_name='AppProductPer',
            
        )
        
        app_product_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3FullAccess'))

        # Role 2: ManagementServerPer
        management_server_role = iam.Role(
            self,
            'ManagementServerPer',
            assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
            role_name='ManagementServerPer'
        )
        
        management_server_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('AWSCodeBuildAdminAccess'))

        self.app_product_role = app_product_role
        self.management_server_role = management_server_role
