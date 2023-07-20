import aws_cdk as cdk
import boto3
import cdk_create_ami as ami_create


from botocore.exceptions import ClientError

import cdk_create_ami as ami_create

from aws_cdk import (
    aws_ec2 as ec2,
    aws_imagebuilder
)

from stack._variables import (
    AMAZ_LINUX_INSTANCE_TYPE,
    AMAZ_LINUX_MACHINE_TYPE,
    USER_DATA,
    AMI_NAME,
)


from constructs import Construct

class AMIStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, security_group_stack, ssh_stack, iam_stack, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        app_prd_vpc = vpc_stack.app_prd_vpc
        security_group_web_server = security_group_stack.security_group_web_server
        ec2_app_prd_key = ssh_stack.ec2_app_prd_key
        
        
        
        # Create an EC2 client
        ec2_client = boto3.client('ec2')

        # Check if AMI with name "AMI_Webserver" already exists
        response = ec2_client.describe_images(Filters=[
            {
                'Name': 'name',
                'Values': [AMI_NAME]
            }
        ])

        # If no matching AMIs found, create the EC2 instance ////and AMI
        if len(response['Images']) == 0:
            # Create the EC2 instance
            webserver = ec2.Instance(
                self,
                id="webserver",
                instance_name="webserver",
                vpc=app_prd_vpc,
                instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
                machine_image=AMAZ_LINUX_MACHINE_TYPE,
                user_data=USER_DATA,
                #key_name=ec2_app_prd_key,
                #security_group=security_group_web_server,
                vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
                block_devices=[
                    ec2.BlockDevice(
                        device_name="/dev/sda1",
                        volume=ec2.BlockDeviceVolume.ebs(20, encrypted=True)
                    )
                ],
            )
            
            # Create the AMI
            ami_image = ami_create.CreateAMI(
                self,
                'amiImage',
                name=AMI_NAME,
                description="AMI for Webserver",
                instance_id=webserver.instance_id,
                delete_ami=False,
                delete_instance=True,
            )
            print(f"\033[32mSuccessfully Created AMI: {AMI_NAME} \033[0m")
        else:
            # AMI already exists, perform any desired actions
            print(f"\033[33mAMI with name {AMI_NAME} already exists. Skipping instance and AMI creation! Please remember that AMI must be manaul deleted!\033[0m")

        
        """
        ami_image = ami_create.CreateAMI(self, "amiImage",
            name="AMI_Webserver",
            instance_id=cdk.basewebserver.instance_id,
            delete_ami=False,
            delete_instance=True,
            block_device_mappings=[
                {
                    "device_name": "/dev/sdh",
                    "ebs": {
                        "volume_size": 20,
                        "volume_type": ami_create.VolumeType.GP3,
                        "delete_on_termination": True
                    }
                }
            ],
            tag_specifications=[
                {
                    "resource_type": ami_create.ResourceType.IMAGE,
                    "tags": [{"key": "AMI", "value": "AMI_Webserver"}]
                }
            ]
        )
        """
        



