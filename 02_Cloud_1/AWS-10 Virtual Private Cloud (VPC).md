# Virtual Private Cloud (VPC)
Een VPC opzetten

## Key-terms

### VPC
Het is een Virtual Private Cloud in je eigen logisch geïsoleerde omgeving binned de AWS. Je gebruikt AWS service zoals EC2 instantie, in de subnets van je VPC. Het is zelfde als je eigen netwerk in het datacenter zou kunnnen gebruiken maar dan heb je de voordelen van het schaalbare infrastructuur van AWS. 
1) VPC Configureren
2) IP-adresbereuk selecteren
3) Subnets maken
4) Route tables configureren
5) Network gateways configureren
6) Beveiligingsinstellingen configureren
Je kan de instantie in je VPC verbinden met het internet of met je eigen datacenter.

#### Elastic IP addres  
Een 'Static IP' is een onafhankelijke lokale IP adres die je kan toewijzen bij:
1) EC2-Instance
2) NAT-gateway
3) ELB
Hierdoor wordt het niet meer gewijzigd als je de EC2-Instance stopt of opnieuw start. Hiermee zorg je ervoor dat je resources altijd bereikbaar is via hetzelfde IP-adres, zelfs wanneer je resources verplaatst of hersteld.

## Opdracht


### Exercise 1:  

#### Allocate an Elastic IP address to your account.     
Aan de linkerkant van je menu scroll je naar beneden totdat je bij 'Elastic IPs' komt en vervolgens op 'Allocate Elastic IP address' drukken. 
![resultaat](/00_includes/AWS-10-resultaat.png "resultaat")
Vervolgens op nieuwe scherm druk je op 'Allocate'

### Create a new VPC with the following requirements:  
https://eu-central-1.console.aws.amazon.com/vpc/
   - Region: Frankfurt (eu-central-1)  
   - VPC with a public and a private subnet  
   - Name: Lab VPC  
   - CIDR: 10.0.0.0/16  
![resultaat](/00_includes/AWS-10-resultaat2.png "resultaat")

### Requirements for the public subnet:
   - Name: Public subnet 1  
   - CIDR: 10.0.0.0/24  
   - AZ: eu-central-1a  

### Requirements for the private subnet:
   - Name: Private subnet 1  
   - CIDR: 10.0.1.0/24  
   - AZ: eu-central-1a  

![resultaat](/00_includes/AWS-10-resultaat3.png "resultaat")

Your network should now look like this:
![resultaat](/00_includes/AWS-10-resultaat4.png "resultaat")

### Exercise 2:  
![resultaat](/00_includes/AWS-10-resultaat5.png "resultaat")

### A) Create an additional public subnet with the following requirements:
   - VPC: Lab VPC  
   - Name: Public Subnet 2  
   - AZ: eu-central-1b  
   - CIDR: 10.0.2.0/24  

![resultaat](/00_includes/AWS-10-resultaat6.png "resultaat")

### B) Create an additional private subnet with the following requirements:
   - VPC: Lab VPC  
   - Name: Private Subnet 2  
   - AZ: eu-central-1b  
   - CIDR: 10.0.3.0/24  

![resultaat](/00_includes/AWS-10-resultaat7.png "resultaat")

Nu op 'Create subnet' drukken.

### View the main route table for Lab VPC. It should have an entry for the NAT gateway.  Rename this route table to Private Route Table.
Bevestinging dat ik de juiste Route Table heb te pakken want er staat 'nat-0bfdfc38cdd112303'.
![resultaat](/00_includes/AWS-10-resultaat8.png "resultaat")

Vervolgens de naam gewijzigd naar 'Private Route Table'
![resultaat](/00_includes/AWS-10-resultaat9.png "resultaat")

### Explicitly associate the private route table with your two private subnets.   

Druk op 'Subnet associations'
![resultaat](/00_includes/AWS-10-resultaat10.png "resultaat")

Selecteer 'Private Subnet 2' 
Druk op 'Save associations'
![resultaat](/00_includes/AWS-10-resultaat11.png "resultaat")

### View the other route table for Lab VPC. It should have an entry for the internet gateway. Rename this route table to Public Route Table.  

Bevestinging dat ik de juiste Route Table heb te pakken want er staat 'igw-0d369b6fb93b5e53c' en ook staat het al in de naam als 'Lab VPC-rb-public'.
![resultaat](/00_includes/AWS-10-resultaat13.png "resultaat")

Vervolgens de naam gewijzigd naar 'Public Route Table'
![resultaat](/00_includes/AWS-10-resultaat14.png "resultaat")

### Explicitly associate the public route table to your two public subnets.  

Druk op 'Subnet associations'
![resultaat](/00_includes/AWS-10-resultaat15.png "resultaat")

Selecteer 'Private Subnet 2' 
Druk op 'Save associations'
![resultaat](/00_includes/AWS-10-resultaat16.png "resultaat")


### Exercise 3:  
### Create a Security Group with the following requirements:  
   - Name: Web SG  
   - Description: Enable HTTP Access  
   - VPC: Lab VPC  
   - Inbound rule: Allow HTTP access from anywhere  
   - Outbound rule: Allow all traffic  

Aan de linkerkant van je menu scroll je naar beneden totdat je bij 'Security groups' komt en vervolgens op 'Create security groups' drukken. 
![resultaat](/00_includes/AWS-10-resultaat17.png "resultaat")

Alles ingevuld zoals bovenaan staat:
![resultaat](/00_includes/AWS-10-resultaat18.png "resultaat")
Druk op 'Create security group'

### Exercise 4:  
### Launch an EC2 instance... 

Terug naar 'VPC dashboard > Launch EC2 Instances'
![resultaat](/00_includes/AWS-10-resultaat19.png "resultaat")

### ...with the following requirements:
   - **Key:** Name  
   - **Value:** Web server
![resultaat](/00_includes/AWS-10-resultaat23.png "resultaat")
   - **AMI:** Amazon Linux 2  
   - **Type:** t3.micro  
   - **Key pair:** no key pair  

#### Network settings
   - **VPC:** Lab VPC
   - **Subnet:** Public subnet 2  
   - **Auto-assign Public IP:** Enable  
   - **Security Group:** Web SG  
![resultaat](/00_includes/AWS-10-resultaat20.png "resultaat")
   - User data:  
```
#!/bin/bash
# Install Apache Web Server and PHP
yum install -y httpd mysql php
# Download Lab files
wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
unzip lab-app.zip -d /var/www/html/
# Turn on web server
chkconfig httpd on
service httpd start
```
   - Tag:

Dan nog de instantie een 'Elastic IP address' geven.
![resultaat](/00_includes/AWS-10-resultaat21.png "resultaat")


### Connect to your server using the public IPv4 DNS name.  

Nadat 'Elastic IP Address' is aangeven op je 'Instance ID' dan zie je 'Public DNS' bij 'Elastic IP Address'.
![resultaat](/00_includes/AWS-10-resultaat25.png "resultaat")
*De reden waarom bij 'instance' het werkt als je kopieert naar je clipbaord, maar niet als je 'open adress' klit is omdat het een https url is.*

Mijn IPv4 DNS van:
```
ec2-3-75-146-133.eu-central-1.compute.amazonaws.com
```

Dit is de resultaat ervan:
![resultaat](/00_includes/AWS-10-resultaatC.png "resultaat")

De VPC had deze instellingen op het einde.
![resultaat](/00_includes/AWS-10-resultaatA.png "resultaat")

![resultaat](/00_includes/AWS-10-resultaatB.png "resultaat")

### Gebruikte bronnen
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#using-instance-addressing-eips-allocating
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-vpc.html
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html


### Ervaren problemen
Krijg steeds 'The connection has timed out' en ik merkte later dat ik het 'Elastic IP address' moets geven bij 'Instance' verder werkte het toen prima.

Ik heb gemerkt dat bij User Data een type fout zat (een enter) waardoor het apache zip file niet kon vinden en installeren, hierdoor kreeg ik gewoon de default test page.
![resultaat](/00_includes/AWS-10-resultaat24.png "resultaat")

### Resultaat
Het kunnen opzetten van een VPC met public en private subnets en het aanwijzen op de juiste route tables. Nieuwe subnets maken en ze toevoegen bij de juist route tables. Een security group maken voor http verbinding. EC2 instance maken met aangepaste requirements.