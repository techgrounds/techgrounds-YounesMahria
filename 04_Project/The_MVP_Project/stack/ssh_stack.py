import aws_cdk as cdk
import boto3
from botocore.exceptions import ClientError

from aws_cdk import (
    aws_ec2 as ec2,
    App, CfnTag, CfnOutput, Duration, Stack,
)
from constructs import Construct
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

import os

class SSHStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create the 'rsakeys' directory if it doesn't exist
        os.makedirs('rsakeys', exist_ok=True)

        ec2_client = boto3.client('ec2')
        ec2_app_prd_key = 'app_private_key'
        ec2_app_prd_key_pair = None

        try:
            ec2_client.describe_key_pairs(KeyNames=[ec2_app_prd_key])
            print(f"\033[33mThe Key pair: {ec2_app_prd_key} already exists! If you need the private key, ask the owner.\033[0m")
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'InvalidKeyPair.NotFound':
                # Generate a new RSA key pair for the Web server
                app_key = rsa.generate_private_key(
                    public_exponent=65537,
                    key_size=2048,
                    backend=default_backend()
                )

                # Serialize the private key to PEM format
                app_pem = app_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                )

                # Save the private key to a file in the 'rsakeys' directory
                with open(os.path.join('rsakeys', 'app_private_key.pem'), 'wb') as file:
                    file.write(app_pem)

                # Serialize the public key to OpenSSH format
                app_public_key = app_key.public_key().public_bytes(
                    serialization.Encoding.OpenSSH,
                    serialization.PublicFormat.OpenSSH
                )

                # Create the SSH key pair for the Web server
                ec2_app_prd_key_pair = ec2.CfnKeyPair(
                    self,
                    "app_private_key",
                    key_name=ec2_app_prd_key,
                    key_type='rsa',
                    public_key_material=app_public_key.decode('utf-8'),
                    tags=[CfnTag(
                        key="Name",
                        value="Web Server Key"
                    )]
                )
                
                # Set DeletionPolicy to Retain
                ec2_app_prd_key_pair.apply_removal_policy(cdk.RemovalPolicy.RETAIN)
                #cdk.CfnResource(ec2_app_prd_key_pair, "app_private_key").apply_removal_policy(cdk.RemovalPolicy.RETAIN)
                
                print(f"\033[32mSuccessfully created: {ec2_app_prd_key} key pair\033[0m")
            else:
                print(f"\033[31mAn unexpected error occurred: \n{str(e)}\033[0m")

        self.ec2_app_prd_key = ec2_app_prd_key
        self.ec2_app_prd_key_pair = ec2_app_prd_key_pair

        ec2_management_prd_key = 'management_private_key'
        ec2_management_prd_key_pair = None

        try:
            ec2_client.describe_key_pairs(KeyNames=[ec2_management_prd_key])
            print(f"\033[33mThe Key pair: {ec2_management_prd_key} already exists! If you need the private key, ask the owner.\033[0m")
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'InvalidKeyPair.NotFound':
                # Generate a new RSA key pair for the Management server
                management_key = rsa.generate_private_key(
                    public_exponent=65537,
                    key_size=2048,
                    backend=default_backend()
                )

                # Serialize the private key to PEM format
                management_pem = management_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                )

                # Save the private key to a file in the 'rsakeys' directory
                with open(os.path.join('rsakeys', 'management_private_key.pem'), 'wb') as file:
                    file.write(management_pem)

                # Serialize the public key to OpenSSH format
                management_public_key = management_key.public_key().public_bytes(
                    serialization.Encoding.OpenSSH,
                    serialization.PublicFormat.OpenSSH
                )

                # Create the SSH key pair for the Management server
                ec2_management_prd_key_pair = ec2.CfnKeyPair(
                    self,
                    "management_private_key",
                    key_name=ec2_management_prd_key,
                    key_type='rsa',
                    public_key_material=management_public_key.decode('utf-8'),
                    tags=[CfnTag(
                        key="Name",
                        value="Management Server Key"
                    )]
                )
                
                # Set DeletionPolicy to Retain
                ec2_management_prd_key_pair.apply_removal_policy(cdk.RemovalPolicy.RETAIN)
                #cdk.CfnResource(ec2_management_prd_key_pair, "management_private_key").apply_removal_policy(cdk.RemovalPolicy.RETAIN)
                
                print(f"\033[32mSuccessfully created: {ec2_management_prd_key} key pair\033[0m")
            else:
                print(f"\033[31mAn unexpected error occurred: \n{str(e)}\033[0m")

        self.ec2_management_prd_key = ec2_management_prd_key
        self.ec2_management_prd_key_pair = ec2_management_prd_key_pair
          
        """       
        # Display a warning message with "Yes" and "No" buttons
        response = messagebox.askyesno('Warning', 'The private key files have been created. Make sure to store them in a secure location. Click on \'No\' if you read this message.')

        # Check the user's response
        if response:
            # The user clicked "Yes"
            messagebox.showwarning('Warning', 'You have not fully read or understand the security risk, please don\'t assume you know better.')
        else:
            # The user clicked "No"
            pass
        """
        
        """        
        # Create a NACL for the web server VPC
        nacl_web = ec2.CfnNetworkAcl(
            self,
            "WebServerNacl",
            vpc_id=vpc_web.vpc_id
        )
        # Inbound rule in vpc_web for SSH
        ec2.CfnNetworkAclEntry(
            self,
            "WebServerNaclInboundSSH",
            network_acl_id=nacl_web.ref,
            rule_number=100,
            protocol=6,  # TCP
            rule_action="allow",  # allow
            egress=False,  # inbound
            port_range=ec2.CfnNetworkAclEntry.PortRangeProperty(
                from_=22,
                to=22
            ),
            cidr_block="10.20.20.0/24",  # CIDR of vpc_manage
        )
        # Create a NACL for the management server VPC
        nacl_manage = ec2.CfnNetworkAcl(
            self,
            "ManagementServerNacl",
            vpc_id=vpc_manage.vpc_id
        )
        # Outbound rule in vpc_manage for SSH
        ec2.CfnNetworkAclEntry(
            self,
            "ManagementServerNaclOutboundSSH",
            network_acl_id=nacl_manage.ref,
            rule_number=100,
            protocol=6,  # TCP
            rule_action="allow",  # allow
            egress=True,  # outbound
            port_range=ec2.CfnNetworkAclEntry.PortRangeProperty(
                from_=22,
                to=22
            ),
            cidr_block="10.10.10.0/24",  # CIDR of vpc_web
        )
        # Associate NACL to all the subnets of the WebServer
        for i, subnet in enumerate(vpc_web.public_subnets + vpc_web.private_subnets, 1):
            ec2.CfnSubnetNetworkAclAssociation(
                self,
                f"WebServerSubnet{i}NaclAssociation",
                subnet_id=subnet.subnet_id,
                network_acl_id=nacl_web.ref,
        )
        # Associate NACL to all the subnets of the ManagementServer
        for i, subnet in enumerate(vpc_manage.public_subnets + vpc_manage.private_subnets, 1):
            ec2.CfnSubnetNetworkAclAssociation(
                self,
                f"ManagementServerSubnet{i}NaclAssociation",
                subnet_id=subnet.subnet_id,
                network_acl_id=nacl_manage.ref,
        )
        """        


        """
                # Create the 'rsakeys' directory if it doesn't exist
        os.makedirs('rsakeys', exist_ok=True)

        ec2_client = boto3.client('ec2')
        ec2_app_prd_key = 'app_private_key'
        ec2_app_prd_key_pair = None
        
        # Generate a new RSA key pair for the Web server
        app_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        # Serialize the private key to PEM format
        app_pem = app_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

        # Save the private key to a file in the 'rsakeys' directory
        with open(os.path.join('rsakeys', 'app_private_key.pem'), 'wb') as file:
            file.write(app_pem)

        # Serialize the public key to OpenSSH format
        app_public_key = app_key.public_key().public_bytes(
            serialization.Encoding.OpenSSH,
            serialization.PublicFormat.OpenSSH
        )

        # Create the SSH key pair for the Web server
        ec2_app_prd_key_pair = ec2.CfnKeyPair(
            self,
            "app_private_key",
            key_name=ec2_app_prd_key,
            key_type='rsa',
            public_key_material=app_public_key.decode('utf-8'),
            tags=[CfnTag(
                key="Name",
                value="Web Server Key"
            )]
        )
        
        try:
            ec2_client.describe_key_pairs(KeyNames=[ec2_app_prd_key])
            print(f"\033[33mThe Key pair: {ec2_app_prd_key} already exists! If you need the private key, ask the owner.\033[0m")
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'InvalidKeyPair.NotFound':
                print(f"\033[32mSuccessfully created: {ec2_app_prd_key} key pair\033[0m")
            else:
                print(f"\033[31mAn unexpected error occurred: \n{str(e)}\033[0m")

        self.ec2_app_prd_key = ec2_app_prd_key
        self.ec2_app_prd_key_pair = ec2_app_prd_key_pair


        ec2_management_prd_key = 'management_private_key'
        ec2_management_prd_key_pair = None
        
        # Generate a new RSA key pair for the Management server
        management_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        # Serialize the private key to PEM format
        management_pem = management_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

        # Save the private key to a file in the 'rsakeys' directory
        with open(os.path.join('rsakeys', 'management_private_key.pem'), 'wb') as file:
            file.write(management_pem)

        # Serialize the public key to OpenSSH format
        management_public_key = management_key.public_key().public_bytes(
            serialization.Encoding.OpenSSH,
            serialization.PublicFormat.OpenSSH
        )

        # Create the SSH key pair for the Management server
        ec2_management_prd_key_pair = ec2.CfnKeyPair(
            self,
            "management_private_key",
            key_name=ec2_management_prd_key,
            key_type='rsa',
            public_key_material=management_public_key.decode('utf-8'),
            tags=[CfnTag(
                key="Name",
                value="Management Server Key"
            )]
        )

        
        try:
            ec2_client.describe_key_pairs(KeyNames=[ec2_management_prd_key])
            print(f"\033[33mThe Key pair: {ec2_management_prd_key} already exists! If you need the private key, ask the owner.\033[0m")
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'InvalidKeyPair.NotFound':
                print(f"\033[32mSuccessfully created: {ec2_management_prd_key} key pair\033[0m")
            else:
                print(f"\033[31mAn unexpected error occurred: \n{str(e)}\033[0m")

        self.ec2_management_prd_key = ec2_management_prd_key
        self.ec2_management_prd_key_pair = ec2_management_prd_key_pair
        """