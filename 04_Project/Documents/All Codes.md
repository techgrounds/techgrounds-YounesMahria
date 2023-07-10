```
npm install -g aws-cdk
mkdir The_MVP_Project
cd The_MVP_Project/
cdk init --language python
pip install -r requirements.txt
python.exe -m pip install --upgrade pip
```

```python
pip install boto3
```

```

  

"""

        # 👇 export myBucket for cross-stack reference

        cdk.CfnOutput(self, 'myAppPrdVpcRef',

        value=app_prd_vpc.vpc_name,

        )

  

        # 👇 export myBucket for cross-stack reference

        cdk.CfnOutput(self, 'myManagementPrdVpcRef',

        value=management_prd_vpc.vpc_name,

        )

  

        VPCPeerConnectionStack(self, "VPCPeerConnectionStack")

"""

```

```

import aws_cdk as cdk

  

from aws_cdk import (

    aws_s3 as s3,

    App, CfnOutput, Duration, Stack,

)

  

from constructs import Construct

  
  

class S3BucketStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:

        super().__init__(scope, id, **kwargs)

"""        my_bucket = s3.Bucket(self, 'myBucket', removal_policy=cdk.RemovalPolicy.DESTROY)

        # 👇 export myBucket for cross-stack reference

        cdk.CfnOutput(self, 'myBucketRef',

            value=my_bucket.bucket_name,

            description='The name of the s3 bucket',

            export_name='myBucket'

        )

  

        app = cdk.App()

        S3BucketStack(app, 'my-s3-stack',

            stack_name='my-s3-stack',

            env={

                'region': os.environ['CDK_DEFAULT_REGION'],

                'account': os.environ['CDK_DEFAULT_ACCOUNT']

            }

        )

"""

  
  

class S3Stack(cdk.Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:

        super().__init__(scope, id, **kwargs)

        # Check if S3 bucket exists

        existing_bucket = s3.Bucket.from_bucket_name(

            self,

            "ExistingBucket",

            bucket_name="mvptechgrounds2023ym",

            description='MVP Projectname',

            export_name='mvptechgrounds2023ym',

            removal_policy=cdk.RemovalPolicy.DESTROY

        )

        # Create S3 bucket if it doesn't exist

        if existing_bucket is None:

            # Create S3 bucket

            bucket = s3.Bucket(

                self,

                "MVPTechgrounds2023YM",

                bucket_name="mvptechgrounds2023ym",

                description='MVP Projectname',

                export_name='mvptechgrounds2023ym',

                removal_policy=cdk.RemovalPolicy.DESTROY

            )

            # 👇 export myBucket for cross-stack reference

            cdk.CfnOutput(self, 'myBucketRef',

            value=bucket.bucket_name,

            description='Projectname',

            export_name='mvptechgrounds2023ym'

        )

            # Set bucket region

            bucket.bucket_region = "eu-central-1"

        else:

            print("S3 bucket already exists. Skipping bucket creation.")

```