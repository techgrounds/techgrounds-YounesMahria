import aws_cdk as cdk
from aws_cdk import aws_ec2 as ec2
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

        # Define constants or variables for common values for Ports
        HTTP_PORT = ec2.Port.tcp(80)
        HTTPS_PORT = ec2.Port.tcp(443)
        SSH_PORT = ec2.Port.tcp(22)
        MYSQL_PORT = ec2.Port.tcp(3306)
        ANY_IPV4 = ec2.Peer.any_ipv4()


        """        
        # Initialize empty lists
        HOME_IPS = []
        OFFICE_IPS = []

        # Ask the user how many home IPs they want to enter
        num_home_ips = int(input("How many home IPs do you want to enter? "))

        # Loop through the number of home IPs
        for i in range(num_home_ips):
            # Prompt the user for each home IP and append it to the list with /32
            home_ip = input(f"Enter home IP {i+1}: ")
            HOME_IPS.append(home_ip + "/32")

        # Ask the user how many office IPs they want to enter
        num_office_ips = int(input("How many office IPs do you want to enter? "))

        # Loop through the number of office IPs
        for i in range(num_office_ips):
            # Prompt the user for each office IP and append it to the list
            office_ip = input(f"Enter office IP {i+1}: ")
            OFFICE_IPS.append(office_ip + "/32")

        # Print the lists of IPs
        print("HOME_IPS:", HOME_IPS)
        print("OFFICE_IPS:", OFFICE_IPS)
        """

                
        ##########################
        # Create Security Groups #
        ##########################

        # Create the management server security group
        security_group_management_server = ec2.SecurityGroup(
            self, "Management Server Security Group",
            vpc=management_prd_vpc,
            security_group_name="Management Server Security Group",
            description="Management Server Security Group from CDK",
            allow_all_outbound=False,
        )
        
        # Create the web server security group
        security_group_web_server = ec2.SecurityGroup(
            self, "Web Server Security Group",
            vpc=app_prd_vpc,
            description="Web Server Security Group from CDK",
            security_group_name="Web Server Security Group",
            allow_all_outbound=False,
        )
        
        # Create the load balancer security group
        security_group_load_balancer = ec2.SecurityGroup(
            self, "Load Balancer Security Group",
            vpc=app_prd_vpc,
            security_group_name="SecurityGroupLoadBalancer",
            description="Load Balancer Security Group from CDK",
            allow_all_outbound=False,
        )
        
        # Create the RDS security group
        security_group_rds = ec2.SecurityGroup(
            self, "RDS Security Group",
            vpc=app_prd_vpc,
            security_group_name="RDS Security Group",
            description="RDS Security Group from CDK",
            allow_all_outbound=False,
        )

        # Create the RDS security group
        security_group_lambda = ec2.SecurityGroup(
            self, "Lambda Security Group",
            vpc=app_prd_vpc,
            security_group_name="Lambda Security Group",
            description="Lambda Security Group from CDK",
            allow_all_outbound=False,
        )
        
        ########################################
        # Security Rules for Management Server #
        ########################################

        # SSH Access to everyone:
        security_group_management_server.add_egress_rule(
            ANY_IPV4, 
            SSH_PORT, 
            "SSH Access to ANY IP"
        )
        
        # HTTP Access to all
        security_group_management_server.add_egress_rule(
            ANY_IPV4, 
            HTTP_PORT, 
            "HTTP Access to ANY IP"
        )
    
        #HTTPS Access to all:
        security_group_management_server.add_egress_rule(
            ANY_IPV4,
            HTTPS_PORT,
            "HTTPS Access to ANY IP"
        )


        # Allow access from office IPs on open ports
        for office_ip in OFFICE_IPS:
            for port in OPEN_PORTS:
                security_group_management_server.connections.allow_from(
                    ec2.Peer.ipv4(office_ip),
                    ec2.Port.tcp(port),
                    f"Allow access from office on port {port}"
                )

        # Allow access from home IPs on open ports
        for home_ip in HOME_IPS:
            for port in OPEN_PORTS:
                security_group_management_server.connections.allow_from(
                    ec2.Peer.ipv4(home_ip),
                    ec2.Port.tcp(port),
                    f"Allow access from home on port {port}"
                )

        #####################################
        # Security Rules for the Web Server #
        #####################################
        
        security_group_web_server.connections.allow_from(
            security_group_management_server, 
            SSH_PORT, 
            "Allow SSH from Management Server"
        ) 
                
        security_group_web_server.connections.allow_from_any_ipv4(
            HTTP_PORT, 
            "Allow HTTP from All"
        )
        
        security_group_web_server.connections.allow_to_any_ipv4(
            HTTP_PORT,
            "Allow HTTP from Web Server to ALL"
        )

        security_group_web_server.connections.allow_from_any_ipv4(
            HTTPS_PORT,
            "Allow HTTPS from Web Server to ALL"
        )

        security_group_web_server.connections.allow_to_any_ipv4(
            HTTPS_PORT,
            "Allow HTTPS from Web Server to ALL"
        )

        # Allow Traffic to and from Database:
        security_group_web_server.connections.allow_to(
            security_group_rds,
            MYSQL_PORT,
            "Allow MySQL from Web Server to Database"
        )
        
        security_group_web_server.connections.allow_from(
            security_group_rds, 
            MYSQL_PORT,
            "Allow MySQL from Database to Web Server"
        )

        ########################################
        # Security Rules for the Load Balancer #
        ########################################

        # the listener at auto_scale_group_stack.py is required to make the correct rules

        #######################################
        # Security Rules for the RDS instance #
        #######################################

        # Allow connection to and from Web Server:
        security_group_rds.connections.allow_from(
            security_group_web_server,
            MYSQL_PORT,
            "Allow MySQL from Web Server to Database"
        )

        security_group_rds.connections.allow_to(
            security_group_web_server,
            MYSQL_PORT,
            "Allow MySQL from Database to Web Server"
        )
        
        # Allow connection to and from Management Server:
        security_group_rds.connections.allow_to(
            security_group_management_server,
            MYSQL_PORT,
            "Allow MySQL from Database to Management Server"
        )

        security_group_rds.connections.allow_from(
            security_group_management_server,
            MYSQL_PORT,
            "Allow MySQL from Management Server to Database"
        )

        # Allow connection from Lambda function:
        security_group_rds.connections.allow_from(
            security_group_lambda,
            MYSQL_PORT,
            "Allow MySQL from Lambda function to Database"
        )

    

        
        ########
        # NACL #
        ########
   
        self.security_group_web_server = security_group_web_server
        self.security_group_rds = security_group_rds
        self.security_group_management_server = security_group_management_server
        self.security_group_load_balancer = security_group_load_balancer
        self.security_group_lambda = security_group_lambda
