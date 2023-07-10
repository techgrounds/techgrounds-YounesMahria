import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2,
    aws_rds as rds,
)
from stack._variables import (
    CURRENT_MAX_AZS,
    VPC1_CIDR,
    VPC2_CIDR,
    SUBNET_SIZE,
)
from constructs import Construct

class VPCStack(cdk.Stack):   
    def __init__(self, scope: Construct, id: str,  **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #vpc1_name: str, vpc2_name: str,
        
        # VPC1: App Production VPC - Create  
        app_prd_vpc = ec2.Vpc(self, 'AppPrdVPC',
            vpc_name='app_prd_vpc',
            ip_addresses=ec2.IpAddresses.cidr(VPC1_CIDR),
            nat_gateways=0,
            enable_dns_support=True,
            enable_dns_hostnames=True,
            #max_azs=CURRENT_MAX_AZS,
            availability_zones=['eu-central-1a','eu-central-1c'],
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="appprdvpcpublic",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=SUBNET_SIZE,
                ),
                ec2.SubnetConfiguration(
                    name="appprdvpcprivate",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=SUBNET_SIZE,
                ),
            ]
        )
        
        # Create a VPC endpoint for Amazon S3 in VPC1
        s3_endpoint_app = app_prd_vpc.add_gateway_endpoint(
            "S3Endpoint",
            service=ec2.GatewayVpcEndpointAwsService.S3,
        )  

        # VPC2: Management Server VPC - Create
        management_prd_vpc = ec2.Vpc(self, 'ManagementServerVPC',
            vpc_name='management_prd_vpc',
            ip_addresses=ec2.IpAddresses.cidr(VPC2_CIDR),
            nat_gateways=0,
            enable_dns_support=True,
            enable_dns_hostnames=True,
            #max_azs=CURRENT_MAX_AZS,
            availability_zones=['eu-central-1a','eu-central-1c'],
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="management_prd_vpc_public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=SUBNET_SIZE,
                ),
                ec2.SubnetConfiguration(
                    name="management_prd_vpc_private",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=SUBNET_SIZE,
                ),
            ]
        )
    
        # Create a VPC endpoint for Amazon S3 in VPC2
        s3_endpoint_management = management_prd_vpc.add_gateway_endpoint(
            "S3Endpoint",
            service=ec2.GatewayVpcEndpointAwsService.S3,
        )
                
        self.app_prd_vpc = app_prd_vpc
        self.management_prd_vpc = management_prd_vpc


        ## Tag name the vpc environment
        cdk.Tags.of(app_prd_vpc).add('Name', 'internet-gateway-app-prd-vpc', exclude_resource_types=['AWS::EC2::VPC'],include_resource_types=['AWS::EC2::InternetGateway'])
        cdk.Tags.of(management_prd_vpc).add('Name', 'internet-gateway-management-prd-vpc', exclude_resource_types=['AWS::EC2::VPC'],include_resource_types=['AWS::EC2::InternetGateway'])

        # Add a Name tag to each public subnet in app_prd_vpc with associated route table 
        for i, subnet in enumerate(app_prd_vpc.public_subnets):
            cdk.Tags.of(subnet).add('Name', f"app-prd-vpc-public-subnet-{i+1}", exclude_resource_types=['AWS::EC2::RouteTable'])
            cdk.Tags.of(subnet).add('Name', f"app-prd-vpc-public-route-table-{i+1}",include_resource_types=['AWS::EC2::RouteTable'])

        # Add a Name tag to each isolated subnet in app_prd_vpc with associated route table 
        for i, subnet in enumerate(app_prd_vpc.isolated_subnets):
            cdk.Tags.of(subnet).add('Name', f"app-prd-vpc-private-subnet-{i+1}", exclude_resource_types=['AWS::EC2::RouteTable'])
            cdk.Tags.of(subnet).add('Name', f"app-prd-vpc-private-route-table-{i+1}",include_resource_types=['AWS::EC2::RouteTable'])

        # Add a Name tag to each public subnet in management-prd-vpc with associated route table 
        for i, subnet in enumerate(management_prd_vpc.public_subnets):
            cdk.Tags.of(subnet).add('Name', f"management-prd-vpc-public-subnet-{i+1}", exclude_resource_types=['AWS::EC2::RouteTable'])
            cdk.Tags.of(subnet).add('Name', f"management-prd-vpc-public-route-table-{i+1}",include_resource_types=['AWS::EC2::RouteTable'])

        # Add a Name tag to each isolated subnet in management-prd-vpc with associated route table 
        for i, subnet in enumerate(management_prd_vpc.isolated_subnets):
            cdk.Tags.of(subnet).add('Name', f"management-prd-vpc-private-subnet-{i+1}", exclude_resource_types=['AWS::EC2::RouteTable'])
            cdk.Tags.of(subnet).add('Name', f"management-prd-vpc-private-route-table-{i+1}",include_resource_types=['AWS::EC2::RouteTable'])


        """
        # Add a Name tag to each public subnet in app_prd_vpc
        for i, subnet in enumerate(app_prd_vpc.public_subnets):
            cdk.Tag('Name', f"app-prd-vpc-public-subnet-{i+1}").visit(subnet)
            cdk.Tag('Name', f"app-prd-vpc-public-route-table-{i+1}").visit(subnet.route_table)

        # Add a Name tag to each isolated subnet in app_prd_vpc
        for i, subnet in enumerate(app_prd_vpc.isolated_subnets):
            cdk.Tag('Name', f"app-prd-vpc-private-subnet-{i+1}").visit(subnet)
            cdk.Tag('Name', f"app-prd-vpc-private-route-table-{i+1}").visit(subnet.route_table)

        # Add a Name tag to each public subnet in management-prd-vpc
        for i, subnet in enumerate(management_prd_vpc.public_subnets):
            cdk.Tag('Name', f"management-prd-vpc-public-subnet-{i+1}").visit(subnet)
            cdk.Tag('Name', f"management-prd-vpc-public-route-table-{i+1}").visit(subnet.route_table)

        # Add a Name tag to each isolated subnet in management-prd-vpc
        for i, subnet in enumerate(management_prd_vpc.isolated_subnets):
            cdk.Tag('Name', f"management-prd-vpc-private-subnet-{i+1}").visit(subnet)
            cdk.Tag('Name', f"management-prd-vpc-private-route-table-{i+1}").visit(subnet.route_table)     

        """




        """
        # Add a Name tag to each public subnet in app_prd_vpc
        for i, subnet in enumerate(app_prd_vpc.public_subnets):
            cdk.Tag.add(subnet, 'Name', f"app-prd-vpc-public-subnet-{i+1}")
            cdk.Tag.add(subnet.route_table, 'Name', f"app-prd-vpc-public-route-table-{i+1}")

        # Add a Name tag to each isolated subnet in app_prd_vpc
        for i, subnet in enumerate(app_prd_vpc.isolated_subnets):
            cdk.Tag.add(subnet, 'Name', f"app-prd-vpc-private-subnet-{i+1}")
            cdk.Tag.add(subnet.route_table, 'Name', f"app-prd-vpc-private-route-table-{i+1}")

        # Add a Name tag to each public subnet in management-prd-vpc
        for i, subnet in enumerate(management_prd_vpc.public_subnets):
            cdk.Tag.add(subnet, 'Name', f"management-prd-vpc-public-subnet-{i+1}")
            cdk.Tag.add(subnet.route_table, 'Name', f"management-prd-vpc-public-route-table-{i+1}")

        # Add a Name tag to each isolated subnet in management-prd-vpc
        for i, subnet in enumerate(management_prd_vpc.isolated_subnets):
            cdk.Tag.add(subnet, 'Name', f"management-prd-vpc-private-subnet-{i+1}")
            cdk.Tag.add(subnet.route_table, 'Name', f"management-prd-vpc-private-route-table-{i+1}")
        """

        
        """      
        # Change the Name tag of each route table in the public subnets of app_prd_vpc
        for i, subnet in enumerate(app_prd_vpc.public_subnets):
            cdk.Tags.of(subnet.route_table).remove('Name')
            cdk.Tags.of(subnet.route_table).add('Name', f"new-app-prd-vpc-public-route-table-{i+1}")
        """      


        """      
        # Add a Name tag to each route table in app_prd_vpc
        # Add a Name tag to each route table in management_prd_vpc
        # Store Subnet IDs from Subnet Names
        app_prd_vpc_public_subnet_ids = [subnet.subnet_id for subnet in app_prd_vpc.public_subnets]
        app_prd_vpc_private_subnet_ids = [subnet.subnet_id for subnet in app_prd_vpc.isolated_subnets]
        management_prd_vpc_public_subnet_ids = [subnet.subnet_id for subnet in management_prd_vpc.public_subnets]
        management_prd_vpc_private_subnet_ids = [subnet.subnet_id for subnet in management_prd_vpc.isolated_subnets]
        self.app_prd_vpc_public_subnet_ids = app_prd_vpc_public_subnet_ids
        self.app_prd_vpc_private_subnet_ids = app_prd_vpc_private_subnet_ids
        self.management_prd_vpc_public_subnet_ids = management_prd_vpc_public_subnet_ids
        self.management_prd_vpc_private_subnet_ids = management_prd_vpc_private_subnet_ids
        """
 
 
        """
        # tag subnets in VPC1
        for subnet in app_prd_vpc.public_subnets:
            cdk.Tags.of(subnet).add('Name', f"{self.stack_name}/public-{subnet.availability_zone}")
        for subnet in app_prd_vpc.isolated_subnets:
            cdk.Tags.of(subnet).add('Name', f"{self.stack_name}/isolated-{subnet.availability_zone}")
        # tag subnets in VPC2
        for subnet in management_prd_vpc.public_subnets:
            cdk.Tags.of(subnet).add('Name', f"{self.stack_name}/public-{subnet.availability_zone}")
        for subnet in management_prd_vpc.isolated_subnets:
            cdk.Tags.of(subnet).add('Name', f"{self.stack_name}/isolated-{subnet.availability_zone}")
        """


        """
        # Create VPC1: app_prd_vpc
        vpc1 = self.create_vpc(vpc1_name)
        # Create VPC2: management_prd_vpc
        vpc2 = self.create_vpc(vpc2_name)
        # Store Subnet IDs from Subnet Names
        subnet_ids = {
            vpc1_name: {
                'public': [subnet.subnet_id for subnet in vpc1.public_subnets],
                'private': [subnet.subnet_id for subnet in vpc1.private_subnets]
            },
            vpc2_name: {
                'public': [subnet.subnet_id for subnet in vpc2.public_subnets],
                'private': [subnet.subnet_id for subnet in vpc2.private_subnets]
            }
        }
        self.subnet_ids = subnet_ids

        def create_vpc(self, vpc_name: str) -> ec2.Vpc:
            return ec2.Vpc(
                self,
                vpc_name,
                vpc_name=vpc_name,
                ip_addresses=ec2.IpAddresses.cidr('10.0.0.0/16'),
                max_azs=2,
                subnet_configuration=[
                    ec2.SubnetConfiguration(
                        subnet_type=ec2.SubnetType.PUBLIC,
                        name='public',
                        cidr_mask=24
                    ),
                    ec2.SubnetConfiguration(
                        subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                        name='private',
                        cidr_mask=24
                    )
                ],
                nat_gateways=1
            )
        """
        
"""  
class SubnetTagger(cdk.IAspect):
    def visit(self, node: cdk.IConstruct):
        if isinstance(node, ec2.Subnet):
            vpc_name = node.node.try_get_context('vpc_name')
            subnet_type = 'public' if node.subnet_type == ec2.SubnetType.PUBLIC else 'private'
            index = node.node.try_get_context('index') + 1
            cdk.Tags.of(node).add('Name', f"{vpc_name}-{subnet_type}-subnet-{index}")
        elif isinstance(node, ec2.CfnRouteTable):
            vpc_name = node.node.try_get_context('vpc_name')
            subnet_type = node.node.try_get_context('subnet_type')
            index = node.node.try_get_context('index') + 1
            cdk.Tags.of(node).add('Name', f"{vpc_name}-{subnet_type}-route-table-{index}")

        app = cdk.App()
        stack = cdk.Stack(app, 'MyStack')

        app_prd_vpc = ec2.Vpc(stack, 'AppPrdVpc', max_azs=3)
        management_prd_vpc = ec2.Vpc(stack, 'ManagementPrdVpc', max_azs=3)

        for i, subnet in enumerate(app_prd_vpc.public_subnets):
            subnet.node.set_context('vpc_name', 'app-prd-vpc')
            subnet.node.set_context('index', i)
        for i, subnet in enumerate(app_prd_vpc.isolated_subnets):
            subnet.node.set_context('vpc_name', 'app-prd-vpc')
            subnet.node.set_context('index', i)
        for i, subnet in enumerate(management_prd_vpc.public_subnets):
            subnet.node.set_context('vpc_name', 'management-prd-vpc')
            subnet.node.set_context('index', i)
        for i, subnet in enumerate(management_prd_vpc.isolated_subnets):
            subnet.node.set_context('vpc_name', 'management-prd-vpc')
            subnet.node.set_context('index', i)

        cdk.Aspects.of(stack).add(SubnetTagger())
"""