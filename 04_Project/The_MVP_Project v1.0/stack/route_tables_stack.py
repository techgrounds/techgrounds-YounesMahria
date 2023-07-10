import aws_cdk as cdk
from aws_cdk import aws_ec2 as ec2
from constructs import Construct

class RouteTablesStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, vpcpeerconnection_stack, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        app_prd_vpc = vpc_stack.app_prd_vpc
        management_prd_vpc = vpc_stack.management_prd_vpc
        vpc_peering_connection = vpcpeerconnection_stack.vpc_peering_connection
        """
        # Create an internet gateway for VPC1
        internet_gateway_vpc1 = ec2.CfnInternetGateway(self, 'InternetGatewayVPC1',
            tags=[cdk.CfnTag(
                key="Name",
                value="internet_gateway_app"
            )]
        )

        # Attach the internet gateway to VPC1
        ec2.CfnVPCGatewayAttachment(self, 'InternetGatewayAttachmentVPC1',
            vpc_id=app_prd_vpc.vpc_id,
            internet_gateway_id=internet_gateway_vpc1.ref
        )

        # Create an internet gateway for VPC2
        internet_gateway_vpc2 = ec2.CfnInternetGateway(self, 'InternetGatewayVPC2',
            tags=[cdk.CfnTag(
                key="Name",
                value="internet_gateway_management"
            )]
        )

        # Attach the internet gateway to VPC2
        ec2.CfnVPCGatewayAttachment(self, 'InternetGatewayAttachmentVPC2',
            vpc_id=management_prd_vpc.vpc_id,
            internet_gateway_id=internet_gateway_vpc2.ref
        )
        """

        # Get the subnets in AZ1a for both VPCs
        app_prd_vpc_subnets_az1a = [subnet for subnet in app_prd_vpc.public_subnets if subnet.availability_zone == 'eu-central-1a']
        management_prd_vpc_subnets_az1a = [subnet for subnet in management_prd_vpc.public_subnets if subnet.availability_zone == 'eu-central-1a']

        # Create a route table in VPC1 for AZ1a subnets
        route_table_app_public = ec2.CfnRouteTable(self, 'RouteTableAppPublic', 
            vpc_id=app_prd_vpc.vpc_id,
            tags=[cdk.CfnTag(
                key="Name",
                value="route_table_app_public"
            )]
        )

        # Add routes to the route table
        for counter, subnet in enumerate(app_prd_vpc_subnets_az1a):
            route = ec2.CfnRoute(
                self, f'RouteTableAppPublicRoute-{counter}',
                route_table_id=route_table_app_public.ref,
                destination_cidr_block=management_prd_vpc.vpc_cidr_block,
                vpc_peering_connection_id=vpc_peering_connection.ref
            )
            # Associate the route tables with the subnets
            ec2.CfnSubnetRouteTableAssociation(
                self, f'RouteTableAppPublicAssociation-{counter}',
                route_table_id=route_table_app_public.ref,
                subnet_id=subnet.subnet_id
            )

        # Create a route table in VPC2 for AZ1a subnets
        route_table_management_public = ec2.CfnRouteTable(self, 'RouteTableManagementPublic', 
            vpc_id=management_prd_vpc.vpc_id,
            tags=[cdk.CfnTag(
                key="Name",
                value="route_table_management_public"
            )]
        )

        # Add routes to the route table
        for counter, subnet in enumerate(management_prd_vpc_subnets_az1a):
            route = ec2.CfnRoute(
                self, f'RouteTableManagementPublicRoute-{counter}',
                route_table_id=route_table_management_public.ref,
                destination_cidr_block=app_prd_vpc.vpc_cidr_block,
                vpc_peering_connection_id=vpc_peering_connection.ref
            )
            # Associate the route tables with the subnets
            ec2.CfnSubnetRouteTableAssociation(
                self, f'RouteTableManagementPublicAssociation-{counter}',
                route_table_id=route_table_management_public.ref,
                subnet_id=subnet.subnet_id
            )

        # Get the subnets in AZ1c for both VPCs
        app_prd_vpc_subnets_az1c = [subnet for subnet in app_prd_vpc.public_subnets if subnet.availability_zone == 'eu-central-1c']
        management_prd_vpc_subnets_az1c = [subnet for subnet in management_prd_vpc.public_subnets if subnet.availability_zone == 'eu-central-1c']

        # Create a route table in VPC1 for AZ1c subnets
        route_table_app_private = ec2.CfnRouteTable(self, 'RouteTableAppPrivate', 
            vpc_id=app_prd_vpc.vpc_id,
            tags=[cdk.CfnTag(
                key="Name",
                value="route_table_app_private"
            )]
        )

        # Add routes to the route table
        for counter, subnet in enumerate(app_prd_vpc_subnets_az1c):
            route = ec2.CfnRoute(
                self, f'RouteTableAppPrivateRoute-{counter}',
                route_table_id=route_table_app_private.ref,
                destination_cidr_block=management_prd_vpc.vpc_cidr_block,
                vpc_peering_connection_id=vpc_peering_connection.ref
            )
            # Associate the route tables with the subnets
            ec2.CfnSubnetRouteTableAssociation(
                self, f'RouteTableAppPrivateAssociation-{counter}',
                route_table_id=route_table_app_private.ref,
                subnet_id=subnet.subnet_id
            )

        # Create a route table in VPC2 for AZ1c subnets
        route_table_management_private = ec2.CfnRouteTable(self, 'RouteTableManagementPrivate', 
            vpc_id=management_prd_vpc.vpc_id,
            tags=[cdk.CfnTag(
                key="Name",
                value="route_table_management_private"
            )]
        )

        # Add routes to the route table
        for counter, subnet in enumerate(management_prd_vpc_subnets_az1c):
            route = ec2.CfnRoute(
                self, f'RouteTableManagementPrivateRoute-{counter}',
                route_table_id=route_table_management_private.ref,
                destination_cidr_block=app_prd_vpc.vpc_cidr_block,
                vpc_peering_connection_id=vpc_peering_connection.ref
            )
            # Associate the route tables with the subnets
            ec2.CfnSubnetRouteTableAssociation(
                self, f'RouteTableManagementPrivateAssociation-{counter}',
                route_table_id=route_table_management_private.ref,
                subnet_id=subnet.subnet_id
            )

        
        
        """
        # Associate the route tables with the subnets
        for subnet in app_prd_vpc_subnets_az1a:
            ec2.CfnSubnetRouteTableAssociation(
                self, f'RouteTableAssociationVPC1AZ1a-{subnet.subnet_id}',
                route_table_id=route_table_vpc1_az1a.ref,
                subnet_id=subnet.subnet_id
            )           
            
            
             
        # Associate the route tables with the subnets
        for subnet in app_prd_vpc_subnets_az1a:
            subnet.route_table(route_table_vpc1_az1a)
        for subnet in app_prd_vpc_subnets_az1c:
            subnet.route_table(route_table_vpc1_az1c)
        for subnet in management_prd_vpc_subnets_az1a:
            subnet.route_table(route_table_vpc2_az1a)
        for subnet in management_prd_vpc_subnets_az1c:
            subnet.route_table(route_table_vpc2_az1c)
        """