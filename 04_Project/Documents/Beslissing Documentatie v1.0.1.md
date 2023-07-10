## Doel  
Het doel van deze documentatie is om de beslissingen en redenen achter het gekozen ontwerp en de implementatie van de infrastructuur te documenteren.

## Context  
In dit project hebben we te maken met verschillende eisen met betrekking tot de infrastructuur. We willen ervoor zorgen dat we aan deze eisen voldoen en tegelijkertijd binnen de gestelde deadline blijven. De gehele infrastructuur gaat gebruik maken van VPC. Hiermee kunnen wordt er EC2-instance gemaakt waarbij veel andere services met elkaar verbonden worden.

## Beslissingen voor de eisen  
Hier worden de beslissingen genomen voor de genoemde eisen, welke AWS service we gaan gebruiken en waarom we deze gaan gebruiken.

### 1. Alle VM disks moeten encrypted zijn.  
De Amazon Elastic Block Store (EBS) heeft een ingebouwde encrypted optie. Wanneer je aangeeft om dat te gebruiken wordt het versleuteld met AWS Key Management Service-sleutel (KMS). 

Sevices:
1) AWS Key Management Service (KMS)
2) Amazon Elastic Block Store (EBS)

### 2. De webserver moet dagelijks gebackupt worden. De backups moeten 7 dagen behouden worden.  
De AWS Backup is specifiek ontworpen voor het beheren en automatiseren van back-up en herstel van AWS-resources. Hiermee kunnen we makkelijke inplannen dat het elke dag een backup maakt met een levensduur van 7 dagen. Je kan het later heel makkelijke de opties wijzingen naar nieuwe eisen. 

Sevices:
1) AWS Backup

### 3. De webserver moet op een geautomatiseerde manier geïnstalleerd worden.  
De AWS CloudFormation helpt het maken van de hele infrastructuur as code. We kunnen veel configuratie invullen en daarbij tijdens het maken ervan, kunnen we ook de UserData voor de EC2-instance aanvullen voor welke softwares geïnstalleerd worden. 
   
   Sevices:
   1) AWS CloudFormation


### 4. De admin/management server moet bereikbaar zijn met een publiek IP.  
Om ervoor zorgen dat het toegankelijke is via het internet, moeten we Elastic IP addres gebruiken ervoor. Dit stelt beheerders in staat om op afstand verbinding te maken met de server en de benodigde administratieve taken uit te voeren. Door een Elastic IP-adres toe te wijzen aan de server, blijft het publieke publiek IP-adres hetzelfde, waardoor toegankelijkheid consistente is. De beveiligingsmaatregelen worden later opgenomen.
   
Services:
1) Elastic IP addres

### 5. De admin/management server moet alleen bereikbaar zijn van vertrouwde locaties (office/admin’s thuis).  
Hiervoor kunnen we firewallregels gebruiken op het instance niveau genaamd Security Groups. Met de juiste configuratie zorgt ervoor dat het alleen toegankelijke is vanuit vertrouwde bronnen, zoals het kantoor en de thuislocaties van de beheerders. Hiermee minimaliseer je het risico van ongeautoriseerde toegang tot de server.

   Sevices:
   1)  Security Groups

### 6. De volgende IP ranges worden gebruikt: 10.10.10.0/24 & 10.20.20.0/24  
In het huidige diagram hebben we 2 Availability Zone iedere met een publiek subnet voor elke vpc.

Availability Zone 1a: 10.10.10.0/24
Availability Zone 1b: 10.20.20.0/24

In het huidige diagram hebben we 2 VPC en iedere heeft 2 Availability Zone waarbij iedere 1 publiek subnet heeft. 

VPC1 - Availability Zone 1a en 1b: 10.10.10.0/24
VPC2 - Availability Zone 1a en 1b: 10.20.20.0/24

### 7. Alle subnets moeten beschermd worden door een firewall op subnet niveau.  
Hiervoor wordt Network ACL gebruikt om dat te kunnen beheren. Die is namelijk de firewall op het subnet niveau.

Service:
1) Network ACL
   
### 8. SSH of RDP verbindingen met de webserver mogen alleen tot stand komen vanuit de admin server.  
Hier wordt de Security Groups verder gebruikt. Dit keer gaan wij ook de twee porten aan de eis stellen om een verbinding te maken tussen Webserver en Admin Server. Hiervoor kunnen eisen dat de IP Adres van het Admin server alleen kan via het twee poorten. Hiermee komt
1) SSH-verkeer (poort 22) 
2) RDP-verkeer (poort 3389)

Sevices:
1)  Security Groups
   

### 9. Wees niet bang om verbeteringen in de architectuur voor te stellen of te implementeren, maar maak wel harde keuzes, zodat je de deadline kan halen.

De huide architectuur ziet er als volgt eruit:
![AWS Architectuur Huidige Situatie](/04_Project/img/AWS%20Architectuur%20Huidige%20Situatie.png "AWS Architectuur Huidige Situatie")

We gaan aantal dingen veranderen en nemen de voorgestelde eisen mee.

Ten eerste wat gaat er veranderd worden is om van 2 naar 1 region te gaan. Gezien voor het SLA 99% als een eis is gesteld kunnen we 2 VPCS in 1 Region zetten. 

De tweede verandering is gebruik maken van Auto Scaling Groups en Elastic Load Balancer voor AZs. Dat wilt zeggen als volgt:
- Auto-Scaling: Wanneer meer verkeer kunnen we meer instance aanmaken voor Webserver alleen. Dit is dus alleen voor VPC 1 omdat verkeer bij VPC2 nooit veranderd.
- Multi-AZ configuratie: Wanneer een AZ uitvalt dan is de andere nog beschikbaar.
- Elastic Load Balancer: Wanneer AZ1a uitvalt kunnen we overschakelen naar AZ1b of AZ1c. Hierdoor zal het tijdje duren voordat het uit


	![AWS Architectuur Huidige Situatie](/04_Project/img/AWS%20Architectuur%20Nieuwe%20Ontwerp.png "AWS Architectuur Huidige Situatie")

- Ontwerp v1.0 




### 10. Nieuwe eisen 





### 11. Nieuwe architectuur v1.1 ontwerp