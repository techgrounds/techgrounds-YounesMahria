
# User Stories v1.0

### 1) Als team willen wij duidelijk hebben wat de eisen zijn van de applicatie.

| |   |
|---|---|
|Epic|Exploratie|
|Beschrijving|Je hebt al heel wat informatie gekregen. Er staan al wat eisen in dit document genoemd, maar deze lijst is mogelijk incompleet of onduidelijk. Het is belangrijk om alle onduidelijkheden uitgezocht te hebben voordat je groot werk gaat verzetten.|
|Deliverable|Een puntsgewijze omschrijving van alle eisen|

De voorgestelde eisen zijn als volgt.

### Noodzakelijke eisen
Hier volgt de 9 noodzakelijke eisen die gesteld zijn met beschrijvingen:

### 1) Alle VM disks moeten encrypted zijn.
 AWS Key Management Service-sleutel (KMS) voor het maken van een KMS-sleutel. Dit kan gedaan worden via AWS Management Console, AWS CLI of AWS SDKs.
 
 Om een Amazon Elastic Block Store (EBS) kunnen we een Amazon Machine Image (AMI) gebruiken ervoor. Hierbij komt ook andere voorgesteld selecties zoals Instance type, user date etc.
 
 Dan moet de Amazon Elastic Block Store (EBS) geconfigureerd worden met de KMS-sleutel tijdens het maken ervan. Die wordt geautomatiseerd met AMI erbij vooraf.
 
 We kunnen encryptiestatus verifiëren, aangezien we met python script gaan werken via AWS CDK. Zal een code gebruikt worden ervoor.
 
   Sevices:
   1) AWS Key Management Service (KMS)
   2) Amazon Elastic Block Store (EBS)
   3) Amazon Machine Image (AMI)

### 2) De webserver moet dagelijks gebackupt worden. De backups moeten 7 dagen behouden worden.

   Een Amazon CloudWatch Event Rule maken met de tijdstip en trigger voor het activeren.
   
   Een AWS Lambda functie maken die wordt geactiveerde door de Amazon CloudWatch Events.
   
   Verder zal AWS Lambda deze functie gebruik van maken.
   - create-snapshot
   - describe_snapshots
   - delete_snapshot
   
   Sevices:
   1) Amazon EBS-snapshots
   2) Amazon CloudWatch Events
   3) AWS Lambda

### 3) De webserver moet op een geautomatiseerde manier geïnstalleerd worden.

   Hiervoor moet een AWS CloudFormation gebruikt worden waarbij alle configuratie wordt ingevuld.
   
   Sevices:
   1) AWS CloudFormation

### 4) De admin/management server moet bereikbaar zijn met een publiek IP.

We gaan Amazon EC2-instance maken/gebruiken met een publieke subnet.  Een Elastic IP zou worden eraan toegevoegd. 
   
   Sevices:
   1) Amazon EC2-instance


### 5) De admin/management server moet alleen bereikbaar zijn van vertrouwde locaties (office/admin’s thuis).

We gaan Amazon EC2-instance maken/gebruiken met een publieke subnet. 
   
   Sevices:
   1) Amazon EC2-instance

### 6) De volgende IP ranges worden gebruikt: 10.10.10.0/24 & 10.20.20.0/24

Hoewel het onduidelijke is welke prive en publieke subnets zijn is het meestal geval dat 1 voor elke er is. 

Public: 10.10.10.0/24
Prive: 10.20.20.0/24
      
   Sevices:
   1) Amazon EC2-instance

### 7) Alle subnets moeten beschermd worden door een firewall op subnet niveau.

Hiervoor wordt Network ACL gebruikt om dat te kunnen beheren. Die is alleen beschikbaar op het subnet niveau.

   
### 8) SSH of RDP verbindingen met de webserver mogen alleen tot stand komen vanuit de admin server.

Hier wordt de Security Groups gebruikt. alleen inkomende verkeer van de admin server.

Port:
- SSH-verkeer (poort 22) 
- RDP-verkeer (poort 3389)
   
### 9) Wees niet bang om verbeteringen in de architectuur voor te stellen of te implementeren, maar maak wel harde keuzes, zodat je de deadline kan halen.

De huide architectuur ziet er als volgt eruit:
![AWS Architectuur Huidige Situatie](/04_Project/img/AWS%20Architectuur%20Huidige%20Situatie.png "AWS Architectuur Huidige Situatie")

We gaan aantal dingen veranderen.     

#### Alle services de uiteindelijke nodig zijn als volgt:
1) AWS Key Management Service (KMS)
2) Amazon Elastic Block Store (EBS)
   - Amazon EBS-snapshots 
3) Amazon Machine Image (AMI)
4) Amazon CloudWatch Events
5) AWS Lambda
6) AWS CloudFormation
7) Amazon EC2-instance


### 2) Als team willen wij een duidelijk overzicht van de aannames die wij gemaakt hebben.

| |   |
|---|---|
|Epic|Exploratie|
|Beschrijving|Je hebt al heel wat informatie gekregen. Mogelijk zijn er vragen die geen van de stakeholders heeft kunnen beantwoorden. Je team moet een overzicht kunnen produceren van de aannames die je daardoor maakt.|
|Deliverable|Een puntsgewijs overzicht van alle aannames|

### 3) Als team willen wij een duidelijk overzicht hebben van de Cloud Infrastructuur die de applicatie nodig heeft.

| |   |
|---|---|
|Epic|Exploratie|
|Beschrijving|Je hebt al heel wat informatie gekregen. En al een ontwerp. Alleen in het ontwerp ontbreken nog zaken als IAM/AD. Identificeer deze extra diensten die je nodig zal hebben en maak een overzicht van alle diensten.|
|Deliverable|Een overzicht van alle diensten die gebruikt gaan worden.|


### 4) Als klant wil ik een werkende applicatie hebben waarmee ik een veilig netwerk kan deployen. 

| |   |
|---|---|
|Epic|v1.0|
|Beschrijving|De applicatie moet een netwerk opbouwen dat aan alle eisen voldoet. Een voorbeeld van een genoemde eis is dat alleen verkeer van trusted sources de management server mag benaderen.|
|Deliverable|IaC-code voor het netwerk en alle onderdelen|

  
### 5) Als klant wil ik een werkende applicatie hebben waarmee ik een werkende webserver kan deployen.

| |   |
|---|---|
|Epic|v1.0|
|Beschrijving|De applicatie moet een webserver starten en deze beschikbaar maken voor algemeen publiek.|
|Deliverable|IaC-code voor en webserver en alle benodigdheden|

  
### 6) Als klant wil ik een werkende applicatie hebben waarmee ik een werkende management server kan deployen.

| |   |
|---|---|
|Epic|v1.0|
|Beschrijving|De applicatie moet een management server starten en deze beschikbaar maken voor een beperkt publiek.|
|Deliverable|IaC-code voor een management server met alle benodigdheden|

### 7) Als klant wil ik een opslagoplossing hebben waarin bootstrap/post-deployment script opgeslagen kunnen worden.

| |   |
|---|---|
|Epic|v1.0|
|Beschrijving|Er moet een locatie beschikbaar zijn waar bootstrap scripts beschikbaar worden. Deze script moeten niet publiekelijk toegankelijk zijn.|
|Deliverable|IaC-code voor een opslagoplossing voor scripts|

  
### 8) Als klant wil ik dat al mijn data in de infrastructuur is versleuteld

| |   |
|---|---|
|Epic|v1.0|
|Beschrijving|Er wordt veel gehecht aan de veiligheid van de data at rest en in motion. Alle data moet versleuteld zijn.|
|Deliverable|IaC-code voor versleuteling voorzieningen|

### 9) Als klant wil ik iedere dag een backup hebben dat 7 dagen behouden wordt  

| |   |
|---|---|
|Epic|v1.0|
|Beschrijving|De klant wil graag dat er een backup beschikbaar is, mocht het nodig zijn om de servers terug te brengen naar een eerdere staat. (Zorg ervoor dat de Backup ook daadwerkelijk werkt)|
|Deliverable|IaC-code voor backup voorzieningen|


### 10) Als klant wil ik weten hoe ik de applicatie kan gebruiken.

| |   |
|---|---|
|Epic|v1.0|
|Beschrijving|Zorg dat de klant kan begrijpen hoe deze de applicatie kan gebruiken. Zorg dat het duidelijk is wat de klant moet configureren voor de deployment kan starten en welke argumenten het programma nodig heeft.|
|Deliverable|Documentatie voor het gebruik van de applicatie|

- Het maken van stap voor stap Documentatie hoe alles werkt.
- Elke applicatie wordt step gewijzigd uitgelegd. 

### 11) Als klant wil ik een MVP kunnen deployen om te testen.

| |   |
|---|---|
|Epic|v1.0|
|Beschrijving|De klant wil zelf intern je architectuur testen voordat ze de code gaan gebruiken in productie. Zorg ervoor dat er configuratie beschikbaar is waarmee de klant een MVP kan deployen.|
|Deliverable|Configuratie voor een MVP deployment|

- Een script die hele infrastructuur.
- Een knop om alles te deployen.

# Aanpak
Hier beschrijf ik mij eigen schema aan met deadlines die ik zelf zou willen aanhouden.

Er worden 11 user stories genoemd:
- Team, heeft 3 User stories: Die gaan over de duidelijkheid.
- Klant, heeft 8 User stories: Die gaan over de wensen en eisen voor het app v1.0.

1) Als team willen wij duidelijk hebben wat de eisen zijn van de applicatie.
2) Als team willen wij een duidelijk overzicht van de aannames die wij gemaakt hebben.
3) Als team willen wij een duidelijk overzicht hebben van de Cloud Infrastructuur die de applicatie nodig heeft.
4) Als klant wil ik een werkende applicatie hebben waarmee ik een veilig netwerk kan deployen. 
5) Als klant wil ik een werkende applicatie hebben waarmee ik een werkende webserver kan deployen.
6) Als klant wil ik een werkende applicatie hebben waarmee ik een werkende management server kan deployen.
7) Als klant wil ik een opslagoplossing hebben waarin bootstrap/post-deployment script opgeslagen kunnen worden.
8) Als klant wil ik dat al mijn data in de infrastructuur is versleuteld
9) Als klant wil ik iedere dag een backup hebben dat 7 dagen behouden wordt  
10) Als klant wil ik weten hoe ik de applicatie kan gebruiken.
11) Als klant wil ik een MVP kunnen deployen om te testen.


# Tijdplanning
Eerste moet goed door genomen wat bij elke user stories moet gaan gebeuren en welke oplossingen er zijn. 

Voorlopig planning is als volgt:
5 June: Het maken van een planning
6-16 June: Het maken van user case 4-7 
17-26 June: Het maken van user case 8-11
27 June: App v1.0 afronden
28-29 June:  App v1.0 doornemen en bug fixes indien nodig.
