import aws_cdk as cdk
import json
import boto3

from aws_cdk import (
    aws_rds as rds,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_s3 as s3,
    aws_secretsmanager as secretsmanager,
    aws_lambda as _lambda,
    aws_sqs as sqs,
    aws_lambda_event_sources as lambda_sources,
    aws_kms as kms,
    
    Duration
)

from stack._variables import (
    S3_BUCKETNAME,
)

from constructs import Construct


class LambdaStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, security_group_stack, rds_stack, **kwargs):
        super().__init__(scope, id, **kwargs)

        app_prd_vpc = vpc_stack.app_prd_vpc
        security_group_lambda = security_group_stack.security_group_lambda
        secret_db = rds_stack.secret_db
        webserver_db = rds_stack.webserver_db

        secret = secretsmanager.Secret(self, "Secret")

        # Create an IAM role for your Lambda function with necessary permissions
        lambda_role = iam.Role(
            self,
            "lambda-vpc-sqs-role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        )

        lambda_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaVPCAccessExecutionRole"))
        lambda_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaSQSQueueExecutionRole"))
        lambda_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"))

        # Add a policy statement to allow the GetSecretValue action on the DBSecret resource
        lambda_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=["secretsmanager:DescribeSecret","secretsmanager:GetSecretValue"],
            resources=[secret_db.secret_arn],
        ))
        
        
        # Get a reference to the KMS key that was automatically created for the bucket
        client = boto3.client("s3")
        response = client.get_bucket_encryption(Bucket=S3_BUCKETNAME)
        bucket_encryption_type = response["ServerSideEncryptionConfiguration"]["Rules"][0]["ApplyServerSideEncryptionByDefault"]["SSEAlgorithm"]
        bucket_encryption_key_arn = response["ServerSideEncryptionConfiguration"]["Rules"][0]["ApplyServerSideEncryptionByDefault"]["KMSMasterKeyID"]
  

    
        # Add a policy statement to your lambda function's IAM role to allow it to use the KMS key
        lambda_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=["kms:Decrypt"],
            resources=[bucket_encryption_key_arn],
        ))
        
        # Create a Lambda function that uses the code from your .zip deployment package
        function = _lambda.Function(
            self,
            "LambdaFunctionWithRDS",
            function_name="PostDeployLambdaRDS",
            description="Deploy your Database schema on RDS",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("postdeployment/lambda_function.zip"),
            role=lambda_role,
            vpc=app_prd_vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            security_groups=[security_group_lambda],
            timeout=cdk.Duration.seconds(30),
            environment={
                "USER_NAME": "admin",
                "RDS_HOST": webserver_db.cluster_endpoint.hostname,
                #"RDS_HOST": webserver_db.db_instance_endpoint_address,  
                "DB_NAME": "WebDatabase",
                "SECRET_NAME": secret_db.secret_name,
                "S3_BUCKET_NAME": S3_BUCKETNAME
            },
        )

        secret.grant_read(function)

        # Create an Amazon SQS queue and configure it to invoke your Lambda function whenever a new message is added.
        queue = sqs.Queue(self, "LambdaRDSQueue")
        function.add_event_source(lambda_sources.SqsEventSource(queue))
        
        