import aws_cdk as cdk
import boto3
from botocore.exceptions import ClientError



from aws_cdk import (
    aws_s3 as s3,
    aws_s3_deployment as s3deploy
)

from stack._variables import (
    S3_BUCKETNAME,
)

from constructs import Construct

class S3Stack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        s3_client = boto3.client('s3')
        try:
            s3_client.head_bucket(Bucket=S3_BUCKETNAME)
            print(f"\033[33mBucket with the same name {S3_BUCKETNAME} already exists! Either you or someone else has already created it.\033[0m")
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == '404':
                # Create a new S3 bucket with the name 'mvptechgrounds2023ym'
                bucket = s3.Bucket(
                    self,
                    "MVPTechgrounds2023YM",
                    bucket_name=S3_BUCKETNAME,
                    encryption=s3.BucketEncryption.KMS,
                    #auto_delete_objects=True,
                    versioned=True,
                )
                print(f"\033[32mSuccessfully created: {S3_BUCKETNAME} stack\033[0m")
            else:
                print(f"\033[31mAn unexpected error occurred: \n{str(e)}\033[0m")
                
            
        """        
        # Get a reference to an existing bucket by name
        bucket = s3.Bucket.from_bucket_name(
            self,
            "MVPTechgrounds2023YM",
            bucket_name=S3_BUCKETNAME
        )

        # Deploy a file to the bucket
        s3deploy.BucketDeployment(self, 'DeployFile',
            sources=[s3deploy.Source.asset('postdeployment/mysqlsampledatabase.zip')],
            destination_bucket=bucket 
        )
        """
        
                                
                
 