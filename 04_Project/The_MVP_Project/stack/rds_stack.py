import aws_cdk as cdk
import json

from aws_cdk import (
    aws_rds as rds,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_s3 as s3,
    aws_secretsmanager as secretsmanager,
    aws_lambda as _lambda,
    aws_sqs as sqs,
    aws_lambda_event_sources as lambda_sources,
    
    Duration
)

from stack._variables import (
    S3_BUCKETNAME,
)

from constructs import Construct


class RdsStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, security_group_stack, **kwargs):
        super().__init__(scope, id, **kwargs)

        app_prd_vpc = vpc_stack.app_prd_vpc
        security_group_rds = security_group_stack.security_group_rds

        ###############################################
        # Create a secret to store the database password
        secret_db = secretsmanager.Secret(
            self,
            "DBSecret",
            secret_name="DBSecret",
            generate_secret_string=secretsmanager.SecretStringGenerator(
                secret_string_template=json.dumps({"username": "admin"}),
                generate_string_key="password",
                exclude_characters='"@/\\',
            ),
        )

        # Create a VPC endpoint for Secrets Manager
        secretsmanager_endpoint = app_prd_vpc.add_interface_endpoint(
            "SecretsManagerEndpoint",
            service=ec2.InterfaceVpcEndpointAwsService.SECRETS_MANAGER,
        )
        
        # Add aurora DB To Private_Isolated subnet on the webserver vpc:
        webserver_db = rds.ServerlessCluster(self, "WebServerDB",
            engine=rds.DatabaseClusterEngine.AURORA_MYSQL,
            vpc=app_prd_vpc,
            credentials=rds.Credentials.from_secret(secret_db),
            default_database_name="WebDatabase",
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            security_groups=[security_group_rds],
            backup_retention=cdk.Duration.days(7),
            removal_policy=cdk.RemovalPolicy.SNAPSHOT,
        )
        
        #print(secret_db.to_string())
        

        
        """
        # Create an RDS instance in the VPC
        webserver_db = rds.DatabaseInstance(
            self, 
            'RDSInstance',
            database_name = "mvp_rds_database",
            engine = rds.DatabaseInstanceEngine.mysql(
                version = rds.MysqlEngineVersion.VER_8_0_32
            ),
            instance_type = ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3,
                ec2.InstanceSize.SMALL,
            ),
            credentials=rds.Credentials.from_secret(secret_db),
            port = 3306,
            backup_retention = cdk.Duration.days(7),
            auto_minor_version_upgrade = True,
            vpc = app_prd_vpc,
            security_groups = [security_group_rds],
            vpc_subnets = ec2.SubnetSelection(
                #subnet_group_name="app_prd_vpc_private",
                availability_zones = ["eu-central-1a","eu-central-1c"],
                subnet_type = ec2.SubnetType.PRIVATE_ISOLATED,
            ),
            multi_az = True,
            allocated_storage = 20,
            storage_type = rds.StorageType.GP2,
            cloudwatch_logs_exports = ['error', 'general', 'slowquery'],
            deletion_protection = False,
        )   
        
        
        #webserver_db.connections.allow_from(management_server, ec2.Port.tcp(3306));
        #webserver_db.connections.allow_from(management_server, ec2.Port.tcp(1433));

        # Create a read replica of the source RDS instance
        read_replica = rds.DatabaseInstanceReadReplica(self, 'RDSReadReplica',
            #database_name="mvp_rds_read_replica_database",
            source_database_instance=webserver_db,
            instance_type=webserver_db._instance_type,
            vpc=webserver_db.vpc,
            security_groups=[security_group_rds],
            vpc_subnets=ec2.SubnetSelection(
                #subnet_group_name="app_prd_vpc_private",
                availability_zones=["eu-central-1a","eu-central-1c"],
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
            ),
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )
        read_replica.auto_minor_version_upgrade = True
        read_replica.apply_immediately = True
        """

        self.secret_db = secret_db
        self.webserver_db = webserver_db

"""

class RDSAuroraDB(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, security_group_stack, **kwargs):
        super().__init__(scope, id, **kwargs)

        app_prd_vpc = vpc_stack.app_prd_vpc
        security_group_rds = security_group_stack.security_group_rds
        #management_server = ec2_stack.management_server

        

        # Add aurora DB To Private_Isolated subnet on the webserver vpc:
        webserver_db = rds.ServerlessCluster(self, "WebServerDB",
            engine=rds.DatabaseClusterEngine.AURORA_MYSQL,
            vpc=app_prd_vpc,
            default_database_name="Cloud10",
            subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
            security_groups=[security_group_rds],
            backup_retention=cdk.Duration.days(7),
            removal_policy=cdk.RemovalPolicy.SNAPSHOT,
        )
"""
        
"""        
        # Create an Aurora DB cluster with multi-AZ enabled
        webserver_db = rds.ServerlessCluster(self, "Cluster",
            engine = rds.DatabaseClusterEngine.aurora_mysql(
                version = rds.AuroraMysqlEngineVersion.VER_2_09_1
            ),
            vpc = app_prd_vpc,
            scaling = rds.ServerlessScalingOptions(
                auto_pause = Duration.minutes(10),
                min_capacity = rds.AuroraCapacityUnit.ACU_8,
                max_capacity = rds.AuroraCapacityUnit.ACU_32,
            ),
            enable_data_api = True,
            backup_retention = Duration.days(7),
            deletion_protection = False,
            removal_policy = cdk.RemovalPolicy.DESTROY,
        )

        # Enable multi-AZ deployment for the cluster
        webserver_db.enable_multi_az()
"""