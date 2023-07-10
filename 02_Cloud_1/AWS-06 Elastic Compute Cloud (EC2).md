# AWS-06 Elastic Compute Cloud (EC2)
Weten hoe EC2/Elastic Compute Cloud werkt.

## Key-terms

### EC2 / Elastic Compute Cloud  
Het is een service waarbij je een ​​Virtuele Machine kan gebruiken in AWS. Het is een instantie die mogelijke combinaties/mix hebben van CPU, geheugen, opslag en netwerk capacity. Elke instantie type heeft een of meerdere instantie grootte waarbij je het kan opschalen.

## Opdracht

### Exercise 1:
#### 1) Navigate to the EC2 menu.  
We beginnen op https://aws.amazon.com/ec2/ en vervolgens op 'Get started with Amazon EC2'
![resultaat](/00_includes/AWS-06-resultaat2.png "resultaat")

#### 2) Launch an EC2 instance with the following requirements:
We gaan eerste op 'Launch instance' drukken.
![resultaat](/00_includes/AWS-06-resultaat3.png "resultaat")

Op de nieuwe scherm gaan wij vervolgens alles een voor een doornemen.
   - **Name:** Web server SG       ![resultaat](/00_includes/AWS-06-resultaat4.png "resultaat")
   - **AMI:** Amazon Linux 2 AMI (HVM), SSD Volume Type       ![resultaat](/00_includes/AWS-06-resultaat5.png "resultaat")
   - **Instance type:** t2.micro       ![resultaat](/00_includes/AWS-06-resultaat6.png "resultaat")
   - **Key pair (login):** younestgaws  
     *alvast een aanmaken*     ![resultaat](/00_includes/AWS-06-resultaat6a.png "resultaat")
     ![resultaat](/00_includes/AWS-06-resultaat6b.png "resultaat")
   - **New Security Group:**
	   - **Rules:** Allow SSH, HTTP and HTTPS from anywhere
	   - **Subnet**: Default, no preference  
          ![resultaat](/00_includes/AWS-06-resultaat7.png "resultaat")
   - **Root volume:** general purpose SSD, Size: 8 GiB       ![resultaat](/00_includes/AWS-06-resultaat8.png "resultaat")
    - **Advanced details**
	    - **Termination protection:** enabled  
          ![resultaat](/00_includes/AWS-06-resultaat9.png "resultaat")
	   - **User data:**  
```
#!/bin/bash
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hello From Your Web Server!</h1></html>' >   /var/www/html/index.html
```
   ![resultaat](/00_includes/AWS-06-resultaat10.png "resultaat")

Uit eindelijke nadat je alles hebt doorgenomen druk je op 'Launch Instance'

-----
*1 - Key pair (login), dit wordt later gedaan, het werd nog niet gevraagd* dus die stond leeg. 

*2 - Review commands*  (Je kan de API calls terug lezen)
#### Instance setup:   
##### (API call: RunInstances)
```
{ "MaxCount": 1, "MinCount": 1, "ImageId": "ami-0adbcf08fdd664fed", "InstanceType": "t2.micro", "EbsOptimized": false, "NetworkInterfaces": [ { "DeviceIndex": 0, "AssociatePublicIpAddress": true, "Groups": [ "<groupId of the new security group created below>" ] } ], "TagSpecifications": [ { "ResourceType": "instance", "Tags": [ { "Key": "Name", "Value": "Web server SG" } ] } ], "PrivateDnsNameOptions": { "HostnameType": "ip-name", "EnableResourceNameDnsARecord": true, "EnableResourceNameDnsAAAARecord": false } }
```

#### New security group setup:  
##### (API call: CreateSecurityGroup)
```
{ "GroupName": "launch-wizard-1", "Description": "launch-wizard-1 created 2023-04-26T09:24:05.604Z", "VpcId": "vpc-08f96278af377f453" }
```

##### (API call: AuthorizeSecurityGroupIngress)
```
{ "GroupId": "<groupId of the security group created above>", "IpPermissions": [ { "IpProtocol": "tcp", "FromPort": 22, "ToPort": 22, "IpRanges": [ { "CidrIp": "0.0.0.0/0" } ] }, { "IpProtocol": "tcp", "FromPort": 443, "ToPort": 443, "IpRanges": [ { "CidrIp": "0.0.0.0/0" } ] }, { "IpProtocol": "tcp", "FromPort": 80, "ToPort": 80, "IpRanges": [ { "CidrIp": "0.0.0.0/0" } ] } ] }
```

----

### Exercise 2:
#### Wait for the Status Checks to get out of the initialization stage. When you click the Status Checks tab, you should see that the System reachability and the Instance reachability checks have passed.  
![resultaat](/00_includes/AWS-06-resultaat11.png "resultaat")
*Je kan ook meteen op 'Instances' of 'i-08d23c8248eeae635' drukken*

#### Log in to your EC2 instance using an ssh connection.  
We gaan terug naar de 'instances' een van de mogelijkeheden is:
![resultaat](/00_includes/AWS-06-resultaat12.png "resultaat")

Vervolgens op 'i-08d23c8248eeae635' drukken.
![resultaat](/00_includes/AWS-06-resultaat13.png "resultaat")

Op 'Connect' drukken.
![resultaat](/00_includes/AWS-06-resultaat14.png "resultaat")

We gaan naar 'SSH client' en de 'Example' kopieren.
![resultaat](/00_includes/AWS-06-resultaat15.png "resultaat")

**Powershell**
Nu de powershell open maken van windows, naar onze map nagiveren en vervolgens de ssh verbinding maken.

```
cd C:\Users\TechGrounds\Desktop\Cloud\AWS
```

```
	ssh -i "younestgaws.pem" ec2-user@ec2-52-57-79-59.eu-central-1.compute.amazonaws.com
```

Als alles goed werkt krijgt ik nu de welcome scherm van 'Amazon Linux 2 AMI'
![resultaat](/00_includes/AWS-06-resultaat16.png "resultaat")

#### Terminate your instance.  
De 'instance selecteren > Instance state > Terminate instance'
![resultaat](/00_includes/AWS-06-resultaat17.png "resultaat")

### Gebruikte bronnen
https://aws.amazon.com/ec2/
https://aws.amazon.com/ec2/instance-types/
https://disaster-recovery.workshop.aws/en/services/compute/ec2.html

### Ervaren problemen
Weet niet hoe ik een SSH key kan toevoegen nadat instance is gemaakt, maar ik ga niet mogelijke erover doen en ging de instance opnieuw maken maar dit keer heb ik wel de 'Key pair' ingevuld dan werkt het wel

### Resultaat
Weten hoe een instance werkt en de opties die aangeboden worden. Een verbindgen maken met een SSH connectie via Powershell.
