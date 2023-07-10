from aws_cdk import (
    aws_ec2 as ec2,
    aws_rds as rds,
    core,
)

class MyStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC
        vpc = ec2.Vpc(self, "VPC")

        # Create a security group for the RDS instance
        rds_security_group = ec2.SecurityGroup(
            self,
            "RDSSecurityGroup",
            vpc=vpc
        )

        # Create an RDS instance
        rds_instance = rds.DatabaseInstance(
            self,
            "RDSInstance",
            engine=rds.DatabaseInstanceEngine.mysql(
                version=rds.MysqlEngineVersion.VER_8_0_26
            ),
            vpc=vpc,
            security_groups=[rds_security_group]
        )

        # Create a security group for the EC2 instance
        ec2_security_group = ec2.SecurityGroup(
            self,
            "EC2SecurityGroup",
            vpc=vpc
        )

        # Allow traffic from the EC2 instance to the RDS instance
        rds_security_group.add_ingress_rule(
            ec2_security_group,
            ec2.Port.tcp(3306)
        )

        # Create an EC2 instance
        ec2.Instance(
            self,
            "EC2Instance",
            instance_type=ec2.InstanceType("t3.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            vpc=vpc,
            security_group=ec2_security_group
        )