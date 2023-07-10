import aws_cdk as cdk
from aws_cdk import aws_ec2 as ec2
from constructs import Construct

from stack._variables import (
    CURRENT_MAX_AZS,
    VPC1_CIDR,
    VPC2_CIDR,
    SUBNET_SIZE,
)

class VPCPeerConnectionStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        app_prd_vpc = vpc_stack.app_prd_vpc
        management_prd_vpc = vpc_stack.management_prd_vpc

        # Create a VPC peering connection between VPC1 and VPC2
        vpc_peering_connection = ec2.CfnVPCPeeringConnection(self, 'VpcPeeringConnection',
            vpc_id=app_prd_vpc.vpc_id,
            peer_vpc_id=management_prd_vpc.vpc_id,
            #peer_region=self.region,
            #peer_role_arn=f'arn:aws:iam::{self.account}:role/PeeringRole'
        )
        
        """
        ec2.cfnRoute(
            self,
            "RouteFromVPC1toVPC2",
            destination_cidr_block=management_prd_vpc.vpc_cidr_block,
            route_table_id=app_prd_vpc.public_subnets[0].route_table.route_table_id,
            vpc_peering_connection_id=self,
        )
        
        ec2.cfnRoute(
            self,
            "RouteFromVPC2toVPC1",
            destination_cidr_block=app_prd_vpc.vpc_cidr_block,
            route_table_id=management_prd_vpc.public_subnets[0].route_table.route_table_id,
            vpc_peering_connection_id=self,
        )
        
        
        """
        
        self.vpc_peering_connection = vpc_peering_connection

        ## Tag name the vpc environment
        #cdk.Tags.of(vpc_peering_connection).add('Name', 'my-vpc-peering-connection')
        #cdk.Tags.of(app_prd_vpc).add('Name', 'endpoint-peering-app-prd-vpc', include_resource_types=['AWS::EC2::VPCPeeringConnection'])
        #cdk.Tags.of(management_prd_vpc).add('Name', 'endpoint-peering-management-prd-vpc', include_resource_types=['AWS::EC2::VPCPeeringConnection'])
