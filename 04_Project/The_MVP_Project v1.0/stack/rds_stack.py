import aws_cdk as cdk

from aws_cdk import (
    aws_rds as rds,
    aws_ec2 as ec2
)

from constructs import Construct


class RdsStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, security_group_stack, **kwargs):
        super().__init__(scope, id, **kwargs)

        app_prd_vpc = vpc_stack.app_prd_vpc
        security_group_rds = security_group_stack.security_group_rds

        # Create an RDS instance in the VPC
        rds_instance = rds.DatabaseInstance(self, 'RDSInstance',
            database_name="mvp_rds_database",
            engine=rds.DatabaseInstanceEngine.mysql(
                version=rds.MysqlEngineVersion.VER_8_0_32
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3,
                ec2.InstanceSize.SMALL,
            ),
            credentials=rds.Credentials.from_username(
                username="admin",
            ),
            port=3306,
            backup_retention=cdk.Duration.days(7),
            auto_minor_version_upgrade=True,
            vpc=app_prd_vpc,
            security_groups=[security_group_rds],
            vpc_subnets=ec2.SubnetSelection(
                subnet_group_name="app_prd_vpc_private",
                availability_zones=["eu-central-1a","eu-central-1c"],
            ),
            multi_az=False,
            allocated_storage=20,
            storage_type=rds.StorageType.GP2,
            cloudwatch_logs_exports=['error', 'general', 'slowquery'],
            deletion_protection=False,
        )
        
        self.rds_instance = rds_instance
        
        

class RdsReadReplicaStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, rds_stack, security_group_stack, **kwargs):
        super().__init__(scope, id, **kwargs)

        app_prd_vpc = vpc_stack.app_prd_vpc
        rds_instance = rds_stack.rds_instance
        security_group_rds = security_group_stack.security_group_rds

        # Create a read replica of the source RDS instance
        read_replica = rds.DatabaseInstanceReadReplica(self, 'RDSReadReplica',
            database_name="mvp_rds_read_replica_database",
            source_database_instance=rds_instance,
            instance_type=rds_instance._instance_type,
            vpc=rds_instance.vpc,
            security_groups=[security_group_rds],
            vpc_subnets=ec2.SubnetSelection(
                subnet_group_name="app_prd_vpc_private",
                availability_zones=["eu-central-1a","eu-central-1c"],
            ),
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )
        read_replica.auto_minor_version_upgrade = True
        read_replica.apply_immediately = True