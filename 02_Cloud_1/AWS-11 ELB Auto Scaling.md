# Elastic Load Balancing (ELB) & Auto Scaling
Een informate over ELB en Auto scaling.

## Key-terms

### Auto Scaling
**AMI (Amazon Machine Image)**  
    Een onderhouden en ondersteunde Image die informatie levert die nodig is om een 'instance' te starten. Het is een template met de ingevulde configuratie die je zelf ook kan aan maken en gebruiken. Je kan een AMI kopen,delen of verkopen van/aan andere gebruikers. Het bevat namelijke:
		1a) Een of meer Amazon Elastic Block Store snapshots of
		1b) Instance-store-backed AMIs of
		1c) Template voor root volume van de 'instance' (zoals OS, Application Server of Applications)
		2) Toestemmingen welke AWS accounts de AMI kan gebruiken voor het maken van 'instances'
		3) Een 'block device mapping' die specifieke volumes aan een 'instance' koppelen wanneer het opgestrat wordt.
	   
2) **CloudWatch**
    Een metriek waarmee je kijkt of je een 'instance' gaat *verwijderen* of *toevoegen.* Het verzamelt en verwerkt de onbewerkte gegevens van Amazon EC2 tot een leesbare, bijna realtime statistieken. Deze worden een periode van 15 maanden bijgehouden, zodat je toegang hebt tot deze historische informatie en een beter beeld krijgt hoe je webapplicatie of dienst presenteert. Standard stuurt EC2 elke 5-minuten periode naar CloudWatch. Je kan het veranderen naar elke 1-minute periode voor het gedetaileerd informatie voor je 'instance'.

### ELB  (Elastic Load Balancing)  
Elastic Load Balancing (ELB) verdeeld inkomend applicatie verkeer automatisch over meerdere doelen en virtuele apparaten in een of meer Availability Zones (AZ's).

1) **Application Load Balancer** 
	   Deze ELB gebruikt en werkt met HTTP en HTTPS protocols (layer 7-OSI Model).
   
2) **Network Load Balancer** 
	   Deze ELB gebruikt en werkt met TCP en UDP (layer 4 - OSI Model).

3) **Gateway Load Balancer** 
	   Deze ELB is een gateway naar je netwerk en als een 'load balancer'. Eerst wordt het verkeer naar een applicatie (van derden) om het te controleren, zoals een IDS/PIS of firewall. Nadat het pakket is geïnspecteerd gaat de Gateway Load Balancer als een Network Load Balancer-routering naar je applicaties. Gateway Load Balancer werkt op (lagen 3 en 4 van de OSI-stack).
   
4) **Classic Load Balancer** 
	   Deze ELB is verouderd en wordt niet aangeraden om het te gebruiken. AWS heeft (tot zover) bijna nooit gestopt met het ondersteunen ervan. Dit komt omdat anders de bestaande applicaties kunnen schaden.
   

## Opdracht

### Exercise 1:

#### Launch an EC2 instance with the following requirements:
   - Region: Frankfurt (eu-central-1)
   - AMI: Amazon Linux 2
   - Type: t3.micro
   -  Security Group: Allow HTTP
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
   - Wait for the status checks to pass.  
![resultaat](/00_includes/AWS-11-resultaat.png "resultaat")

#### Create an AMI from your instance with the following requirements:  
   - Image name: Web server AMI  

Ga naar 'AMI > Actions > Image and tempates > Create Image'
![resultaat](/00_includes/AWS-11-resultaat2.png "resultaat")

Bij 'Image Name' = 'Web server AMI'
![resultaat](/00_includes/AWS-11-resultaat3.png "resultaat")
Druk op 'Create image' 

Aan de linkerkant ga je naar 'AMIs'
![resultaat](/00_includes/AWS-11-resultaat4.png "resultaat")
Je ziet de net aangemaakt AMI op de lijst staan.

### Exercise 2:
#### Create an application load balancer... 
We moeten eerste een VPC weer aanmaken, zoals in de vorige opdracht en een EC2 instance maken ervan.

We kunnen nu gelijke gebruik maken van AMI die gemaakt is bij het vorige opdracht. Druk op 'Launch instance from AMI' en vervolg de stappen, vergeet niet de 'Security Policy' erbij te doen.
![resultaat](/00_includes/AWS-11-resultaat10.png "resultaat")


### ...with the following requirements:
   - Name: LabELB
   - Listener: HTTP on port 80
   - AZs: eu-central-1a and eu-central-1b
   - Subnets: must be public
   - Security Group:
	   - Name: ELB SG
	   - Rules: Allow HTTP access	     ![resultaat](/00_includes/AWS-11-resultaat7.png "resultaat")
	     *Herhaling van vorige opdracht*
   - Target Group:
	   - Name: LabTargetGroup   ![resultaat](/00_includes/AWS-11-resultaat8.png "resultaat")
	     Om het voor 'Auto Scaling' te doen bij onze 'Instance'.Bij 'VPC' = 'Lap VPC' (je eigen vpc selecteren.)
	     ![resultaat](/00_includes/AWS-11-resultaat12.png "resultaat")
	   - Targets: to be registered by Auto Scaling	     ![resultaat](/00_includes/AWS-11-resultaat9.png "resultaat")


Ga naar https://eu-central-1.console.aws.amazon.com/ec2/v2/home?region=eu-central-1#LoadBalancers en druk op 'Create load balancer'
![resultaat](/00_includes/AWS-11-resultaat5.png "resultaat")

We gaan 'Application Load Balancer' selecteren door op 'Create' te drukken.
![resultaat](/00_includes/AWS-11-resultaat6.png "resultaat")

Bij 'Load balancer name' = 'LabELB'
![resultaat](/00_includes/AWS-11-resultaat13.png "resultaat")

Bij 'VPC' = 'Lab VPC'
Selecteer beide mappings.
![resultaat](/00_includes/AWS-11-resultaat14.png "resultaat")

Bij 'Security groups' = 'ELB SG'
![resultaat](/00_includes/AWS-11-resultaat15.png "resultaat")

Bij 'Default Acount' = 'LabTargetGroup'
![resultaat](/00_includes/AWS-11-resultaat16.png "resultaat")
Dan druk je op 'Create load balancer'

### Exercise 3:
#### Create a Launch Configuration/Template for the Auto Scaling group. It has to be identical to the server that is currently running.   
https://eu-central-1.console.aws.amazon.com/ec2/home?region=eu-central-1#LaunchTemplates 

![resultaat](/00_includes/AWS-11-resultaat25.png "resultaat")

Bij 'Launch template name' = 'LaunchELBScale'
![resultaat](/00_includes/AWS-11-resultaat26.png "resultaat")

Bij 'AMI' = 'Web server AMI' die je eerder hebt gemaakt in de opdracht.
![resultaat](/00_includes/AWS-11-resultaat27.png "resultaat")
- Rest zelfde invullen als daarvoor  
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

Druk op 'Create template'
![resultaat](/00_includes/AWS-11-resultaat24.png "resultaat")
*Launch Template gebruikt, Launch Configuration was een oudere methode die niet meer wordt gebruikt.*

#### Create an auto scaling group with the following requirements:
https://eu-central-1.console.aws.amazon.com/ec2/home?region=eu-central-1#CreateAutoScalingGroup:launchTemplateId=lt-0285e87f330545bd2
   - Name: Lab ASG
     ![resultaat](/00_includes/AWS-11-resultaat17.png "resultaat")
   - Launch Configuration: Web server launch configuration
   - Subnets: must be in eu-central-1a and eu-central-1b
     ![resultaat](/00_includes/AWS-11-resultaat18.png "resultaat")
   - Load Balancer: LabELB
   - Group metrics collection in CloudWatch must be enabled
     ![resultaat](/00_includes/AWS-11-resultaat19.png "resultaat")
   - Group Size:
	   - Desired Capacity: 2
	   - Minimum Capacity: 2
	   - Maximum Capacity: 4
	   - Scaling policy: Target tracking with a target of 60% average CPU utilisation.
	     ![resultaat](/00_includes/AWS-11-resultaat20.png "resultaat")


![resultaat](/00_includes/AWS-11-resultaat21.png "resultaat")
Nu op 'Create Auto Scaling-group' drukken.


### Exercise 4:
   - Verify that the EC2 instances are online and that they are part of the target group for the load balancer.
     ![resultaat](/00_includes/AWS-11-resultaat28.png "resultaat")
   - Access the server via the ELB by using the DNS name of the ELB.
```
LabELB-1768272926.eu-central-1.elb.amazonaws.com
```
![resultaat](/00_includes/AWS-11-resultaat29.png "resultaat")

   - Perform a load test on your server(s) using the website on your server to activate auto scaling. There might be a delay on the creation of new servers in your fleet, depending on the settings on your Auto Scaling Group.
     
     
     Omdat ik al 4 had (wat de max is) had ik 2 geselecteerd en 'Deregister' zodat ik alleen 2 'Instance'     ![resultaat](/00_includes/AWS-11-resultaat34.png "resultaat")
     
     Nu heb ik alleen 2 Instance als targets staan.     ![resultaat](/00_includes/AWS-11-resultaat35.png "resultaat")
     
      Bij zelfde ELB url zie je nog steeds 'Current CPU Load: 0%' (of 1%) en dan druk je op 'Load Test' om het te beginnen.    ![resultaat](/00_includes/AWS-11-resultaat33.png "resultaat")
      
      Nu wordt de 'Current CPU Load: 100%' waardoor 1-2 nieuwe instances worden aangemaakt. Dit gaat tot 5 minuten duren.      ![resultaat](/00_includes/AWS-11-resultaat36.png "resultaat")
     
     Na lang wachten en elke minute op 'Load Test' drukken.     ![resultaat](/00_includes/AWS-11-resultaat37.png "resultaat")
     
     Nu heb ik er in totaal 4 Instance.     ![resultaat](/00_includes/AWS-11-resultaat38.png "resultaat")
     
     Later heb ik weer 2 inplaats van 4![resultaat](/00_includes/AWS-11-resultaat39.png "resultaat")
     
     --- 
     *Een andere manier die mogelijke is los van load test.*
     Selecteer de 4 overeenkomende instance en dan 'Instance State > Stop Instance' en dan tot 5 minuten wachten.![resultaat](/00_includes/AWS-11-resultaat30.png "resultaat")
     
     Nu is een extra bijgekomen...     ![resultaat](/00_includes/AWS-11-resultaat31.png "resultaat")
     
     Toen nog een extra bijgekomen!     ![resultaat](/00_includes/AWS-11-resultaat32.png "resultaat")



### Gebruikte bronnen
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch.html
https://aws.amazon.com/cloudwatch/faqs/
https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html
https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/
https://medium.com/codex/configuring-and-testing-auto-scaling-in-aws-ec2-60a1434b0eae

### Ervaren problemen
Opdrachten opnieuw moeten doen toen werkte het wel, kan zijn dat ik ergens een type foute had gedaan maar kwam niet achter bij welke deel.

### Resultaat
Leren hoe Auto scalling werkt