import aws_cdk as cdk
from aws_cdk import aws_certificatemanager as acm, aws_iam as iam
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
import datetime
import boto3
from botocore.exceptions import ClientError
from constructs import Construct

class CertificateStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Generate a private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )

        # Save the private key to a file
        with open("certificates/mydomain.key", "wb") as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            ))

        # Generate a certificate signing request (CSR)
        csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, u"mydomain.com"),
        ])).sign(private_key, hashes.SHA256())

        # Save the CSR to a file
        with open("certificates/mydomain.csr", "wb") as f:
            f.write(csr.public_bytes(serialization.Encoding.PEM))

        # Create a self-signed certificate
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, u"mydomain.com"),
        ])
        cert = x509.CertificateBuilder().subject_name(
            subject
        ).issuer_name(
            issuer
        ).public_key(
            private_key.public_key()
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.datetime.utcnow()
        ).not_valid_after(
            datetime.datetime.utcnow() + datetime.timedelta(days=365)
        ).sign(private_key, hashes.SHA256())

        # Save the self-signed certificate to a file
        with open("certificates/mydomain.crt", "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))

        # Read the contents of the self-signed certificate and private key files
        with open("certificates/mydomain.crt", "r") as f:
            certificate_body = f.read()

        with open("certificates/mydomain.key", "r") as f:
            private_key = f.read()

                
        # Check if a server certificate with the desired name already exists
        certificate_name = "mydomain"
        iam_client = boto3.client('iam')
        response = iam_client.list_server_certificates()
        certificate_exists = False

        for cert in response['ServerCertificateMetadataList']:
            if cert['ServerCertificateName'] == certificate_name:
                certificate_exists = True
                break

        if not certificate_exists:
            try:
                # Upload the self-signed certificate to IAM
                response = iam_client.upload_server_certificate(
                    CertificateBody=certificate_body,
                    PrivateKey=private_key,
                    ServerCertificateName=certificate_name
                )
                # Get the ARN of the server certificate
                server_certificate_arn = response['ServerCertificateMetadata']['Arn']
                print(f'\033[92mA new server certificate with name "{certificate_name}" has been created\033[0m')
            except ClientError as e:
                print(f'\033[91mError uploading the certificate: {e.response["Error"]["Message"]}\033[0m')
        else:
            # Get the ARN of the existing server certificate
            response = iam_client.get_server_certificate(ServerCertificateName=certificate_name)
            server_certificate_arn = response['ServerCertificate']['ServerCertificateMetadata']['Arn']
            print(f'\033[93mA server certificate with name "{certificate_name}" already exists and chosen! \033[0m')
                        
        self.server_certificate_arn = server_certificate_arn