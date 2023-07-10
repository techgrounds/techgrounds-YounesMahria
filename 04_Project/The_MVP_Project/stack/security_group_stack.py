import aws_cdk as cdk

from aws_cdk import (
    aws_ec2 as ec2,
    App, CfnOutput, Duration, Stack, 
)

from constructs import Construct

from stack._variables import (
    VPC1_CIDR,
    VPC2_CIDR,
    OFFICE_IPS,
    HOME_IPS,
    OPEN_PORTS,
    MYTESTIP,
)

class SecurityGroupStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        app_prd_vpc = vpc_stack.app_prd_vpc
        management_prd_vpc = vpc_stack.management_prd_vpc

        # Create a Security Group for the Proxy Server
        security_group_proxy_server = ec2.SecurityGroup(self, "Proxy Server SecurityGroup",
            vpc=app_prd_vpc,
            description="Proxy Server Security Group from CDK",
            security_group_name="Proxy Server Security Group",
            allow_all_outbound=True,
        )

        # Allow inbound HTTP traffic
        security_group_proxy_server.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "Allow inbound HTTP traffic"
        )

        # Allow inbound HTTPS traffic
        security_group_proxy_server.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(443),
            "Allow inbound HTTPS traffic"
        )

        """
        # Allow outbound HTTP traffic
        security_group_proxy_server.add_egress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "Allow outbound HTTP traffic"
        )

        # Allow outbound HTTPS traffic
        security_group_proxy_server.add_egress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(443),
            "Allow outbound HTTPS traffic"
        )
        """


        # Create a Security Group for the RDS instance
        security_group_rds = ec2.SecurityGroup(self,"RDS Security Group",
            vpc=app_prd_vpc,
            description="RDS Security Group from CDK",
            security_group_name="RDS Security Group",
        )
        
        # Allow traffic from the EC2 instance to the RDS instance
        security_group_rds.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(3306)
        )


        # Security Group for Management Server
        security_group_management_server = ec2.SecurityGroup(self, "Management Server SecurityGroup",
            vpc=management_prd_vpc,
            description="Management Server Security Group from CDK",
            security_group_name="Management Server Security Group",
            allow_all_outbound=True,
        )
        
        # Allow web connect
        security_group_management_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "allow http from world")
        security_group_management_server.connections.allow_from_any_ipv4(ec2.Port.tcp(443), "allow https from world")


        # Create load balancer security group
        security_group_load_balancer = ec2.SecurityGroup(
            self, "LoadBalancerSG",
            vpc=app_prd_vpc,
            allow_all_outbound=True,
            security_group_name="SecurityGroupLoadBalancer"
        )

        # Allow inbound HTTP traffic
        security_group_load_balancer.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "Allow inbound HTTP traffic"
        )

        # Allow inbound HTTPS traffic
        security_group_load_balancer.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(443),
            "Allow inbound HTTPS traffic"
        )

        """        
        # Allow outbound HTTP traffic
        security_group_load_balancer.add_egress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "Allow outbound HTTP traffic"
        )

        # Allow outbound HTTPS traffic
        security_group_load_balancer.add_egress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(443),
            "Allow outbound HTTPS traffic"
        )
        """
        
                # Create a Security Group for the Web Server
        security_group_web_server = ec2.SecurityGroup(self, "Web Server SecurityGroup",
            vpc=app_prd_vpc,
            description="Web Server Security Group from CDK",
            security_group_name="Web Server Security Group",
            allow_all_outbound=True,
        )
        
        """        
        # Allow inbound traffic on ports 80 and 443 from the private IP address of the proxy server
        security_group_web_server.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "allow http from proxy server"
        )
        security_group_web_server.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(443),
            "allow https from proxy server"
        )
        """
                # Allow inbound HTTP traffic from load balancer security group
        security_group_web_server.add_ingress_rule(
            ec2.SecurityGroup.from_security_group_id(
                self, "LoadBalancerSGRefHTTP", security_group_load_balancer.security_group_id),
            ec2.Port.tcp(80),
            "Allow inbound HTTP traffic from load balancer security group"
        )

        # Allow inbound HTTPS traffic from load balancer security group
        security_group_web_server.add_ingress_rule(
            ec2.SecurityGroup.from_security_group_id(
                self, "LoadBalancerSGRefHTTPS", security_group_load_balancer.security_group_id),
            ec2.Port.tcp(443),
            "Allow inbound HTTPS traffic from load balancer security group"
        )

        
        """
        
        # Allow inbound SSH traffic from management server via transit gateway
        security_group_web_server.add_ingress_rule(
            ec2.Peer.ipv4(management_prd_vpc.vpc_cidr_block),
            ec2.Port.tcp(22),
            "Allow inbound SSH traffic from management server via transit gateway"
        )

        """
        
        # Allow SSH and RDP connections from the management server to the web server
        for port in OPEN_PORTS:
            security_group_web_server.add_ingress_rule(
                #security_group_management_server,
                ec2.Peer.any_ipv4(),
                ec2.Port.tcp(port),
                f"Allow access from management server on port {port}"
            )

        for office_ip in OFFICE_IPS:
            for port in OPEN_PORTS:
                security_group_management_server.add_ingress_rule(
                    ec2.Peer.ipv4(office_ip),
                    ec2.Port.tcp(port),
                    f"Allow access from office on port {port}"
                )

        for home_ip in HOME_IPS:
            for port in OPEN_PORTS:
                security_group_management_server.add_ingress_rule(
                    ec2.Peer.ipv4(home_ip),
                    ec2.Port.tcp(port),
                    f"Allow access from home on port {port}"
                )
              
        self.security_group_proxy_server = security_group_proxy_server
        self.security_group_web_server = security_group_web_server
        self.security_group_rds = security_group_rds
        self.security_group_management_server = security_group_management_server
        self.security_group_load_balancer = security_group_load_balancer