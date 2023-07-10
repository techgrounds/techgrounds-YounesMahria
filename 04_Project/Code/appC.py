from aws_cdk import (
    core,
    aws_ec2 as ec2,
)

class MyStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Assume VPC1 is already created
        vpc1 = ec2.Vpc.from_lookup(self, 'VPC1', vpc_id='vpc-12345678')

        # Create an EC2 instance in VPC1
        instance = ec2.Instance(self, 'Instance',
            instance_type=ec2.InstanceType('t3.micro'),
            machine_image=ec2.AmazonLinuxImage(),
            vpc=vpc1,
        )

        # Allocate an Elastic IP address to your account
        eip = ec2.CfnEIP(self, 'EIP')

        # Associate the Elastic IP address with the instance
        ec2.CfnEIPAssociation(self, 'EIPAssociation',
            eip=eip.ref,
            instance_id=instance.instance_id,
        )