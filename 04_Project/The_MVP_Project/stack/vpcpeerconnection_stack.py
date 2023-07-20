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
        
        # Get the VPCs from the stack
        app_prd_vpc = vpc_stack.app_prd_vpc
        management_prd_vpc = vpc_stack.management_prd_vpc

        # Define the destination CIDR blocks for each VPC
        app_prd_vpc_cidr = app_prd_vpc.vpc_cidr_block
        management_prd_vpc_cidr = management_prd_vpc.vpc_cidr_block

        # Create a VPC peering connection between VPC1 and VPC2
        vpc_peering_connection = ec2.CfnVPCPeeringConnection(
            self,
            'VpcPeeringConnection',
            vpc_id=app_prd_vpc.vpc_id,
            peer_vpc_id=management_prd_vpc.vpc_id,
        )

        # Add routes for the peering connection to all subnets in each VPC
        for subnet in app_prd_vpc.isolated_subnets:
            ec2.CfnRoute(self, f"AppPRDRoute{subnet.node.id}",
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block=management_prd_vpc_cidr,
                vpc_peering_connection_id=vpc_peering_connection.ref,
            )

        for subnet in management_prd_vpc.public_subnets:
            ec2.CfnRoute(self, f"ManagementPRDRoute{subnet.node.id}",
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block=app_prd_vpc_cidr,
                vpc_peering_connection_id=vpc_peering_connection.ref,
            )
        
        self.vpc_peering_connection = vpc_peering_connection



        """
                
        # Get the security groups from the stack
        #security_group_web_server = security_group_stack.security_group_web_server
        #security_group_management_server = security_group_stack.security_group_management_server

        # Create a helper function to add ingress and egress rules for security groups
        def add_security_group_rules(source_sg, dest_sg, description):
            # Allow inbound traffic from source SG to dest SG
            dest_sg.add_ingress_rule(
                source_sg,
                ec2.Port.all_traffic(),
                description,
            )

            # Allow outbound traffic from dest SG to source SG
            dest_sg.add_egress_rule(
                source_sg,
                ec2.Port.all_traffic(),
                description,
            )

        # Add security group rules for web server and management server
        add_security_group_rules(security_group_web_server, security_group_management_server, "Allow traffic between web server and management server")
        add_security_group_rules(security_group_management_server, security_group_web_server, "Allow traffic between management server and web server")
        """
        