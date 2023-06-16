from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_rds as rds,
)

class MyStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a VPC with the specified CIDR range
        vpc = ec2.Vpc(self, 'VPC', cidr='10.0.0.0/16')

        # Create public subnets in AZ1a and AZ1b
        public_subnet_az1a = ec2.Subnet(self, 'PublicSubnetAZ1a', vpc=vpc,
            availability_zone='eu-central-1a',
            cidr_block='10.10.10.0/24',
            map_public_ip_on_launch=True,
        )

        public_subnet_az1b = ec2.Subnet(self, 'PublicSubnetAZ1b', vpc=vpc,
            availability_zone='eu-central-1b',
            cidr_block='10.20.20.0/24',
            map_public_ip_on_launch=True,
        )

        # Create an RDS instance in the VPC
        rds_instance = rds.DatabaseInstance(self, 'RDSInstance',
            engine=rds.DatabaseInstanceEngine.mysql(
                version=rds.MysqlEngineVersion.VER_8_0_26
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3,
                ec2.InstanceSize.SMALL,
            ),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnets=[public_subnet_az1a, public_subnet_az1b]),
            multi_az=False,
            allocated_storage=20,
            storage_type=rds.StorageType.GP2,
            cloudwatch_logs_exports=['error', 'general', 'slowquery'],
            deletion_protection=False,
        )
        
