## 1. Infrastructuurontwerp:

### 1.1 Netwerkarchitectuur:

- **Amazon Virtual Private Clouds (VPCs):** 2 VPC's opgezet in een Region (Frankfurt):
- VPC 1 - De app-prd-vpc (10.10.10.0/24):
    - Subnets:
        - Private: Webserver en Aurora RDB
        - Publiek Subnet: Load Balancer
- VPC 2 - De management-prd-vpc (10.20.20.0/24):
    - Subnet:
        - Publiek: Management Server (Bastion).
- **Availability Zones:** 2

### 1.2 Beveiliging:

- **AWS CDK2:** Omdat CDK1 sinds begin juni 2023 niet meer wordt ondersteund, inclusief beveiligingsupdates, raden we het af. Daarom hebben we voor CDK2 gekozen.
- **Network Access Control List (NACL):** De Beveiliging op subnet-niveau om het inkomende en uitgaande verkeer te kunnen beheren.
- **Security Groups:**  De Beveiliging op VPC-niveau om het inkomende en uitgaande verkeer te kunnen beheren.
- **SSH en RDP:** Alleen toegestaan vanaf de management server.
- **Load Balancer:** Voor het bereiken van de webserver die op een private subnet zit. De DNS ervan is nodig voor de configuratie. Hierbij zit ook een Target Group eraan vast die nodig is voor de juiste verwijzing naar de webserver(s).
- **Listener - HTTP naar HTTPS:** Alle HTTP-verbindingen worden automatisch omgezet in HTTPS. De Listener helpt hierbij.
- **Certificatie:** Je hebt je eigen domein nodig met het juiste certificaat dat je zelf moet aanvragen via de 'AWS Certificate Manager'. De huidige werkwijze is dat we een eigen certificaat maken met TLS 1.2 of hoger voor testdoeleinden.
- **Key Pairs:** Voor de webserver en de management server om verbinding te kunnen maken binnen het besturingssysteem. Je moet bij de verantwoordelijke partij vragen om die key pairs. Ze worden aangemaakt en in je folder toegevoegd. 

### 1.3 Health Checks

- **Auto Scaling Group:** Wanneer de belasting op de CPU 80% of hoger is, wordt er een nieuwe webserver opgestart, waarbij er maximaal 3 zijn. Als de belasting afneemt, worden er nieuwe webservers verwijderd totdat er nog maar 1 overblijft. Je kunt dit terugzien bij 'Monitoring'.
- **Target Group:** Het is gekoppeld aan de Load Balancer die een verwijzing heeft naar de webservers. Er wordt elke 5 minuten gecontroleerd of de Health Status 'Pass' is.

## 2. Opslagontwerp:

### 2.1 VM-diskencryptie:

- **AWS KMS:** Bij het coderen kun je eenvoudig aangeven met 'encrypted=True'. De KMS-sleutel kun je vinden in je AWS Console, wanneer je naar KMS gaat.

### 2.2 Back-upstrategie:

- **AWS Backup:** Dagelijkse back-ups worden gemaakt om 10 uur 's nachts voor de Management server.
- **Aurora RDB:** Dagelijkse back-ups worden gemaakt om 10 uur 's nachts. Dit is de webserverdatabase.
- **Instellingen:** Voor beide wordt een dagelijkse back-up gemaakt om 22 uur 's nachts. De bewaartermijn is dan ook 7 dagen, waarna ze worden verwijderd.

## 3. Implementatie- en beheerstrategie:

### 3.1 Geautomatiseerde installatie van de webserver:

- **CDK + Userdata:** Tijdens het deployen wordt de webserver automatisch gestart. Hiervoor moet je wel zelf je website erop zetten; je zou een zipbestand met je webinhoud in dezelfde folder moeten plaatsen.

### 3.2 Beheer van de management server:

- **RDS:** De management server is beschikbaar met een publieke RDS-bestand die je in bezit hebt/krijgt.
- **Security Group:** De toegang tot de management server is beperkt tot vertrouwde locaties, zoals het kantoor en de thuislocaties van de beheerders. Hiervoor heb je de IP-adressen van deze locaties nodig.

### 4. Installaties

- De handleiding documenteert stap voor stap wat je allemaal moet doen om het goed te kunnen installeren en op te zetten.