## Doel

Het doel van deze documentatie is om de beslissingen en redenen achter het gekozen ontwerp en de implementatie van de infrastructuur te documenteren.

## Context

In dit project hebben we te maken met verschillende eisen met betrekking tot de infrastructuur. We willen ervoor zorgen dat we aan deze eisen voldoen en tegelijkertijd binnen de gestelde deadline blijven. De gehele infrastructuur maakt gebruik van VPC. Hiermee kunnen EC2-instances gemaakt worden waarbij veel andere services met elkaar verbonden worden. Als er vragen zijn over de eisen, stel ik een voorstel voor om te kijken of het anders kan of dat het niet noodzakelijk is.

## Beslissingen voor de eisen

Hier worden de beslissingen genomen voor de genoemde eisen, welke AWS-service we gaan gebruiken en waarom we deze gaan gebruiken. Ook worden de nieuwe eisen van v1.1 eronder gezet.

### 1. Alle VM-disks moeten geëncrypteerd zijn.

**Oplossing:** De Amazon Elastic Block Store (EBS) heeft een ingebouwde optie voor encryptie. Wanneer je aangeeft dat je het wilt gebruiken, wordt het versleuteld met een AWS Key Management Service (KMS)-sleutel. Bij het CDK is het simpel genoeg met deze lijn. `volume=autoscaling.BlockDeviceVolume.ebs(20, encrypted=True)`

**Services:**

1. Amazon Elastic Block Store (EBS)
2. KMS

### 2. De webserver moet dagelijks geback-upt worden. De backups moeten 7 dagen bewaard blijven.

**Oplossing:** AWS Backup is specifiek ontworpen voor het beheren en automatiseren van back-ups en herstel van AWS-resources. Hiermee kunnen we eenvoudig plannen dat er dagelijks een backup wordt gemaakt met een bewaartermijn van 7 dagen. Later kunnen we de configuratie eenvoudig aanpassen aan nieuwe eisen.

**Voorstel:** Gezien de website wordt gemaakt door een ander team waarbij geen nieuwe data op de Webserver Instance staan, is dit niet handig. Beter zou zijn om een backup te maken van de RDS Database omdat daar dagelijks nieuwe data komt te staan en de Management server omdat de omgeving toch kan veranderen of aangepast worden.

**Services:**

1. AWS Backup

### 3. De webserver moet op een geautomatiseerde manier geïnstalleerd worden.

**Oplossing:** AWS CloudFormation helpt bij het maken van de hele infrastructuur als code. Hiervoor maken we gebruik van AWS CDK2 waarbij het in Python is geschreven. We raden af om geen gebruik te maken van CDK1 omdat er geen support meer is en wordt geadviseerd om te migreren naar CDK2. Door `cdk synth` en `cdk deploy --all` uit te voeren, wordt je hele infrastructuur inclusief webserver geïnstalleerd en gelanceerd.

**Services:**

1. AWS CDK2 - In Python geschreven
2. AWS SDK - boto3 voor het controleren en verwijzen naar resources.
3. AWS CloudFormation - Wordt automatisch omgezet bij CDK synth/deploy.

### 4. De admin/management server moet bereikbaar zijn met een publiek IP.

**Oude oplossing:** Om ervoor te zorgen dat het toegankelijk is via het internet, moeten we een Elastic IP-adres gebruiken. Dit stelt beheerders in staat om op afstand verbinding te maken met de server en de benodigde administratieve taken uit te voeren. Door een Elastic IP-adres toe te wijzen aan de server, blijft het publieke IP-adres consistent, waardoor toegankelijkheid consistent blijft. De beveiligingsmaatregelen worden later opgenomen.

**NIEUWE EIS 1.1:** De webserver mag niet meer "naakt" op het internet benaderbaar zijn. De klant wil het liefst dat er een proxy tussen komt en dat de server geen publiek IP-adres meer heeft.

**Nieuwe Oplossing:**

- Webserver: Deze wordt nu in een privé-subnet geplaatst. Hierbij zit een Load Balancer en een 'Target Group' erachter. Je gebruikt de DNS van de 'Load Balancer' om bij de webserver te komen. Hiervoor moet je een 'Listener' hebben waarbij verkeer op poort 443 / https naar een van de beschikbare webservers wordt geleid.
- Management server: Voor toegang heb je een bestaande RDP-verbinding nodig en moeten de IP-adressen van het werk en thuis toegevoegd zijn om verbinding te kunnen maken. Ook heb je de keypair nodig voor het wachtwoord.

**Services:**

1. Load Balancer
2. Target Group
3. Security Group
4. Key Pairs

### 5. De admin/management server moet alleen bereikbaar zijn vanuit vertrouwde locaties (kantoor/admin’s thuis).

**Oplossing:** Hiervoor kunnen we firewallregels gebruiken op het instance niveau genaamd Security Groups. Met de juiste configuratie zorgen we ervoor dat de server alleen toegankelijk is vanuit vertrouwde bronnen, zoals het kantoor en de thuislocaties van de beheerders. Hiermee minimaliseren we het risico van ongeautoriseerde toegang tot de server.

**Services:**

1. Security Groups

### 6. De volgende IP-ranges worden gebruikt: 10.10.10.0/24 & 10.20.20.0/24

**Oplossing:** app_prd_vpc:

- IP: 10.10.10.0/24
- Subnets:
    - 1 Publiek (load balancer)
    - 1 Privé (webserver).

management_prd_vpc:

- IP: 10.20.20.0/24
- Subnets:
    - 1 Publiek (management server)

### 7. Alle subnets moeten beschermd worden door een firewall op subnet niveau.

**Oplossing:** Hiervoor wordt Network ACL gebruikt om dat te kunnen beheren. Deze fungeert als de firewall op het subnet niveau.

**Services:**
1. Network ACL

### 8. SSH- of RDP-verbindingen met de webserver mogen alleen tot stand komen vanuit de management server.

**Oplossing:** Hiervoor wordt Security Groups verder uitgebreid. Deze keer stellen we ook de twee poorten als eis om een verbinding te maken tussen de webserver en de management server. De management server kunnen we gebruiken als Bastion / Jump box en hiermee wordt de verbinding verder gezet naar de webserver.

**Poorten:**
1. SSH-verkeer (poort 22) vanaf het IP-adres van de management server.
2. RDP-verkeer (poort 3389) vanaf het IP-adres van de management server.

**Services:**
1. Bastion / Jump box
2. Security Groups

### 9. Mocht een gebruiker via HTTP verbinding maken met de load balancer dan zou deze verbinding automatisch geüpgraded moeten worden naar HTTPS. Hierbij moet de verbinding beveiligd zijn met minimaal TLS 1.2 of hoger.

**Oplossing:** Met de 'Load Balancer' kunnen we een andere 'Listener' eraan toevoegen. Deze keer wordt het verkeer dat binnenkomt op poort 80 automatisch omgeleid naar poort 443. Om dit te kunnen doen, is er ook een certificaat nodig.

**BELANGRIJK:** De huidige werkwijze wordt een eigen certificaat aangemaakt. Je bent zelf verantwoordelijk voor het opstellen van het juiste certificaat.

**Services:**
1. Load Balancer - Listener
2. Certificatie - Zelf toegewezen.

### 10. De webserver moet met enige regelmaat een ‘health check’ ondergaan. Mocht de webserver deze health check falen, dan moet de server automatisch hersteld worden. Mocht de webserver onder aanhoudende belasting komen te staan, dan moet er een tijdelijke extra server opgestart worden. De klant denkt dat er nooit meer dan 3 servers in totaal nodig zijn gezien de gebruikersaantallen in het verleden.

**Oplossing:** We kunnen gebruik maken van een 'Auto Scaling Group' voor de webserver waarbij we aangeven dat als de CPU-belasting hoger is dan 80%, er een nieuwe webserver instance wordt gestart. Hiervoor kunnen we een health check toevoegen. Bij 'Target Groups' en geven we aan welke 'Load Balancer' we gaan gebruiken. Die 'Load Balancer' is al gekoppeld aan de 'Auto Scaling Group' van de webserver. Elke 5 minuten wordt gecontroleerd of de health check nog goed is. Sneller dan 5 minuten leidt tot meer kosten.

**Services:**
1. Auto Scaling Group
2. Target Group
3. Load Balancer

### 11. Wees niet bang om verbeteringen in de architectuur voor te stellen of te implementeren, maar maak wel harde keuzes, zodat je de deadline kunt halen.

De huidige architectuur ziet er als volgt uit:![AWS Architectuur Huidige Situatie](/04_Project/img/AWS%20Architectuur%20Huidige%20Situatie.png "AWS Architectuur Huidige Situatie")

We gaan een aantal dingen veranderen en nemen de voorgestelde eisen mee met de eerder voorgesteld oplossing in het diagram.


![AWS Architectuur Huidige Situatie](/04_Project/img/AWS%20Architectuur%20Nieuwe%20Ontwerp.png "AWS Architectuur Nieuwe Situatie")
Ontwerp v1.0 - Van tevoren uitgaan welke services nodig zijn


![AWS Architectuur Huidige Situatie](/04_Project/img/AWS%20Architectuur%20Nieuwe%20Ontwerpv1.1.png "AWS Architectuur Nieuwe Situatie")
Ontwerp v1.1 - Aangepaste ter hand van het huidige infrastructuur. 
