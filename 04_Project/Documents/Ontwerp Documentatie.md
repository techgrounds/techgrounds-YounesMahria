## 1. Infrastructuurontwerp:

### 1.1 Netwerkarchitectuur:

- Er worden twee Amazon Virtual Private Clouds (VPCs) opgezet: VPC-A voor het publieke subnet en VPC-B voor het private subnet.
- Het publieke subnet (10.10.10.0/24) zal externe toegang mogelijk maken via een Internet Gateway en Network Address Translation (NAT) voor de private subnetten.
- Het private subnet (10.20.20.0/24) zal interne resources hosten zonder directe toegang vanaf het internet.

### 1.2 Beveiliging:

- Er wordt een Network Access Control List (NACL) geconfigureerd op subnetniveau om het inkomende en uitgaande verkeer te beheren voor zowel het publieke als het private subnet.
- In het publieke subnet wordt toegang tot SSH- en RDP-verbindingen alleen toegestaan vanaf de admin server.

## 2. Opslagontwerp:

### 2.1 VM-diskencryptie:

- AWS KMS-sleutels worden gebruikt om alle VM-disks binnen de infrastructuur te versleutelen.
- Een KMS-sleutelbeheerbeleid wordt geconfigureerd om de toegangscontrole tot de sleutels te beheren.

### 2.2 Back-upstrategie:

- Dagelijkse back-ups worden geïmplementeerd met behulp van geautomatiseerde scripts.
- Een back-upscript wordt geconfigureerd om regelmatig snapshots te maken van de gegevens op de webserver en deze snapshots worden bewaard gedurende 7 dagen.

## 3. Implementatie- en beheerstrategie:

### 3.1 Geautomatiseerde installatie van de webserver:

- AWS CloudFormation wordt gebruikt om de webserver-infrastructuur te implementeren en te beheren.
- Een CloudFormation-template wordt ontwikkeld om de benodigde AWS-resources, zoals EC2-instanties, beveiligingsgroepen en load balancers, op te zetten.

### 3.2 Beheer van admin/management server:

- De admin/management server wordt geconfigureerd met een publiek IP-adres voor externe toegang.
- Toegang tot de admin/management server is beperkt tot vertrouwde locaties, zoals het kantoor en de thuislocaties van de beheerders.




----

1. Inleiding:
- Beschrijf het doel van de ontwerpdocumentatie en geef een overzicht van de vereisten die worden behandeld.

2. Vereistenoverzicht:
- Geef een samenvatting van elke vereiste en leg uit waarom het belangrijk is voor het systeem.

3. Architectuurdiagram:
- Maak een diagram dat de architectuur van het systeem illustreert.
- Toon de verschillende componenten, zoals de webserver, admin server, beveiligingsgroepen en andere relevante services.
- Laat de netwerkconnectiviteit en communicatiestromen tussen de componenten zien.

4. Vereiste 1: Alle VM disks moeten encrypted zijn:  
- Beschrijf hoe je dit vereiste hebt geïmplementeerd.
- Verwijs naar de AWS KMS-sleutel die wordt gebruikt voor diskencryptie.
- Geef aan hoe de encryptiestatus van de disks kan worden geverifieerd.

5. Vereiste 2: De webserver moet dagelijks gebackupt worden. De backups moeten 7 dagen behouden worden:  
- Beschrijf de backupstrategie die je hebt geïmplementeerd.
- Verwijs naar de gebruikte backupservice of -tool.
- Geef aan hoe je de backupretentie van 7 dagen hebt geconfigureerd.

6. Vereiste 3: De webserver moet op een geautomatiseerde manier geïnstalleerd worden:   
- Leg uit hoe je de geautomatiseerde installatie hebt opgezet.
- Verwijs naar de gebruikte tool of technologie, zoals AWS CloudFormation of AWS CDK.
- Beschrijf eventuele configuratie- of installatiescripts die worden gebruikt.

7. Vereiste 4: De admin/management server moet bereikbaar zijn met een publiek IP:  
- Beschrijf hoe je een publiek IP hebt toegewezen aan de admin/management server.
- Verwijs naar de gebruikte AWS-service, zoals EC2.
- Leg uit hoe de netwerkconfiguratie is geconfigureerd om het publieke IP-toegang mogelijk te maken.

8. Vereiste 5: De admin/management server moet alleen bereikbaar zijn van vertrouwde locaties:
- Beschrijf hoe je de toegangsbeperking hebt geïmplementeerd.
- Verwijs naar de gebruikte beveiligingsgroepen en hun configuratie.
- Geef aan hoe de vertrouwde locaties zijn gedefinieerd, zoals specifieke IP-adressen of IP-ranges.

9. Vereiste 6: De volgende IP-ranges worden gebruikt: 10.10.10.0/24 & 10.20.20.0/24:  
- Leg uit dat de opgegeven IP-ranges privé IP-ranges zijn en niet direct toegankelijk zijn vanaf het openbare internet.
- Vermeld dat NAT kan worden gebruikt om indirecte toegang mogelijk te maken.

10. Vereiste 7: Alle subnets moeten beschermd worden door een firewall op subnetniveau: 
- Beschrijf hoe je Network ACLs hebt geconfigureerd om subnet-level firewalls te implementeren.


10. Vereiste 8: SSH- of RDP-verbindingen met de webserver mogen alleen tot stand komen vanuit de admin server:
- Beschrijf hoe je deze beperking hebt geïmplementeerd.
- Leg uit dat je gebruik hebt gemaakt van beveiligingsgroepen om inkomend verkeer te controleren.
- Verwijs naar de beveiligingsgroepen van zowel de webserver als de admin server.
- Specificeer dat alleen verkeer van de admin server wordt toegestaan op de SSH- of RDP-poorten van de webserver.

11. Monitoring en Logging:
- Beschrijf hoe je monitoring en logging hebt opgezet voor het systeem.
- Verwijs naar AWS-services zoals CloudWatch voor monitoring en CloudTrail voor logboekregistratie.
- Bespreek welke aspecten worden gemonitord, zoals systeemprestaties, beveiligingsgebeurtenissen en fouten.
- Leg uit hoe je waarschuwingen configureert en hoe loggegevens worden opgeslagen en geanalyseerd.

12. High Availability en Schaalbaarheid: 
- Bespreek hoe je hebt gezorgd voor hoge beschikbaarheid en schaalbaarheid van de webserver.
- Verwijs naar het gebruik van AWS Elastic Load Balancer (ELB) voor het verdelen van het verkeer.
- Beschrijf hoe je Auto Scaling hebt geconfigureerd om de capaciteit van de webserver automatisch aan te passen aan de vraag.

13. Beveiligingsmaatregelen:
- Beschrijf de algemene beveiligingsmaatregelen die je hebt genomen voor het systeem.
- Noem het belang van het regelmatig bijwerken van softwarepatches en het implementeren van sterke wachtwoorden.
- Bespreek het belang van het beperken van gebruikersrechten en het implementeren van beveiligingspraktijken zoals de "least privilege"-benadering.

14. Back-up- en herstelprocedures:
- Beschrijf de back-up- en herstelprocedures die zijn geïmplementeerd.
- Verwijs naar de eerdere vermelding van het dagelijks back-uppen van de webserver en het behouden van de backups gedurende 7 dagen.
- Leg uit hoe je de back-upbestanden veilig opslaat en hoe je het herstelproces test.

15. Conclusie:
- Eindig de ontwerpdocumentatie met een conclusie die de belangrijkste punten samenvat.
- Moedig aanvullende vragen of opmerkingen aan en bied ondersteuning voor verdere assistentie.