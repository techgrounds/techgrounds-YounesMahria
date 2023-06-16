from aws_cdk import (
    core,
    aws_ec2 as ec2,
)

class MyStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Assume VPC1 and VPC2 are already created
        vpc1 = ec2.Vpc.from_lookup(self, 'VPC1', vpc_id='vpc-12345678')
        vpc2 = ec2.Vpc.from_lookup(self, 'VPC2', vpc_id='vpc-87654321')

        # Create a VPC peering connection between VPC1 and VPC2
        peering_connection = ec2.CfnVPCPeeringConnection(self, 'PeeringConnection',
            vpc_id=vpc1.vpc_id,
            peer_vpc_id=vpc2.vpc_id,
        )

        # Get the subnets in AZ1a for both VPCs
        vpc1_subnets_az1a = [subnet for subnet in vpc1.public_subnets if subnet.availability_zone == 'eu-central-1a']
        vpc2_subnets_az1a = [subnet for subnet in vpc2.public_subnets if subnet.availability_zone == 'eu-central-1a']

        # Create a route in VPC1 to route traffic to VPC2 via the peering connection
        for subnet in vpc1_subnets_az1a:
            route_table = ec2.RouteTable.from_route_table_id(self, f'RouteTable{subnet.subnet_id}', subnet.route_table.route_table_id)
            route_table.create_route(f'Route{subnet.subnet_id}',
                destination_cidr_block=vpc2.vpc_cidr_block,
                peer=peering_connection,
            )

        # Create a route in VPC2 to route traffic to VPC1 via the peering connection
        for subnet in vpc2_subnets_az1a:
            route_table = ec2.RouteTable.from_route_table_id(self, f'RouteTable{subnet.subnet_id}', subnet.route_table.route_table_id)
            route_table.create_route(f'Route{subnet.subnet_id}',
                destination_cidr_block=vpc1.vpc_cidr_block,
                peer=peering_connection,
            )