from aws_cdk import (
    aws_ec2 as ec2,
    #aws_iam as iam,
    #aws_s3 as s3,
    #aws_rds as rds,
    #aws_backup as backupService, 
    #aws_ecs as ecs,
    #aws_elasticloadbalancingv2 as elbv2,
    #aws_autoscaling as autoscaling,
    #aws_ecs_patterns as ecs_patterns,
    #App, CfnOutput, Duration, Stack, 
)


MYTESTIP = '0.0.0.0/32' #own ip for testing only




CURRENT_MAX_AZS = 2

LZ_NAME = "eu-central" # Local Zone to be used

VPC1_CIDR = "10.10.10.0/24" # VPC CIDR that will be used to create a new VPC
VPC2_CIDR = "10.20.20.0/24" # VPC CIDR that will be used to create a new VPC

VPC1_PUBLIC_CIDR = "10.10.10.0/25" # VPC CIDR for public subnets
VPC1_PRIVATE_CIDR = "10.10.10.128/25" # VPC CIDR for private subnets
VPC2_PUBLIC_CIDR = "10.20.20.0/25" # VPC CIDR for public subnets
VPC2_PRIVATE_CIDR = "10.20.20.128/25" # VPC CIDR for private subnets
SUBNET_SIZE = 26 # Subnet size of the subnets in the Local Zone
COOLDOWN_SECONDS = 60 # The amount is 60 secounds by default. You shouldn't change this unless you really want it by 1 second.
COOLDOWN_MINUTES = 5 # The amount is 5 minute by default. Change this to increase it or decrease by minute,
COOLDOWN = COOLDOWN_SECONDS*COOLDOWN_MINUTES # Cooldown is the total by multiply 60 seconds times times 5 minutes for 300 seconds.
OFFICE_IPS = ["198.51.100.1/32", "203.0.113.1/32"]  # List of your office IP address
HOME_IPS = ["198.51.100.1/32", "203.0.113.1/32", MYTESTIP] # List of your home IP addresses
OPEN_PORTS = [22,3389]  # Default: 22 and 3389 - List of ports to open connection. Unless you want less/more ports added and know what you are doing.
S3_BUCKETNAME = 'mvp-techgrounds-2023-cloud-ym'

# EC2 Instance - Global Type Selection
AMAZ_INSTANCE_TYPE = 't2.micro'

# EC2 Instance - Linux Settings
AMAZ_LINUX_VERSION = ec2.MachineImage.latest_amazon_linux2
AMAZ_LINUX_EDITION = ec2.AmazonLinuxEdition.STANDARD
AMAZ_LINUX_VIRTUALIZATION = ec2.AmazonLinuxVirt.HVM
AMAZ_LINUX_STORAGE = ec2.AmazonLinuxStorage.GENERAL_PURPOSE

# EC2 Instance - Windows Server Settings
AMAZ_WINDOWS_VERSION = ec2.MachineImage.latest_windows
AMAZ_WINDOWS_EDITION = ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE


# The Main Linux Machine Image Instance
AMAZ_LINUX = AMAZ_LINUX_VERSION(edition=AMAZ_LINUX_EDITION,
                                virtualization=AMAZ_LINUX_VIRTUALIZATION,
                                storage=AMAZ_LINUX_STORAGE)
   
# The Main Windows Server Machine Image Instance     
AMAZ_WINDOWS = AMAZ_WINDOWS_VERSION(
    version=AMAZ_WINDOWS_EDITION
)

# Read the contents of the user data file
with open('userdata/web-server-user-data.sh', 'r') as file:
    web_server_user_data = file.read()

# Create a UserData object from the file contents
web_server_user_data_object = ec2.UserData.custom(web_server_user_data)

USER_DATA = web_server_user_data_object

# Read the contents of the user data file
with open('userdata/proxy-server-user-data.sh', 'r') as file:
    proxy_user_data = file.read()

# Create a UserData object from the file contents
proxy_user_data_object = ec2.UserData.custom(proxy_user_data)

PROXY_USER_DATA = proxy_user_data_object

        

"""
  from stack._variables import (
    CURRENT_MAX_AZS,
    LZ_NAME,
    VPC1_CIDR,
    VPC2_CIDR,
    SUBNET_SIZE,
    COOLDOWN,
    OFFICE_IPS,
    HOME_IPS,
    AMAZ_INSTANCE_TYPE,
    AMAZ_LINUX_EDITION,
    AMAZ_LINUX_VIRTUALIZATION,
    AMAZ_LINUX_STORAGE,
    AMAZ_LINUX,
)
"""