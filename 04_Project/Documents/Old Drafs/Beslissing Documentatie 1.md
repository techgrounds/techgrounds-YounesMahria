## Doel:

Het doel van deze documentatie is om de beslissingen en redenen achter het gekozen ontwerp en de implementatie van de infrastructuur te documenteren.

## Beslissingen:

1) AWS Key Management Service (KMS)
2) Amazon Elastic Block Store (EBS)
   - Amazon EBS-snapshots 
3) Amazon Machine Image (AMI)
4) Amazon CloudWatch Events
5) AWS Lambda
6) AWS CloudFormation
7) Amazon EC2-instance

1. **AWS CloudFormation:** We hebben ervoor gekozen om AWS CloudFormation te gebruiken voor de implementatie en het beheer van onze infrastructuur. Dit is gebaseerd op de volgende redenen:
    
    - CloudFormation biedt een gestandaardiseerde en herhaalbare manier om infrastructuur op te zetten en te beheren.
    - Het stelt ons in staat om de infrastructuur-as-code-aanpak te volgen, waardoor we de volledige controle hebben over de configuratie en de mogelijkheid om wijzigingen te beheren via versiebeheer.
    - CloudFormation integreert goed met andere AWS-services en biedt mogelijkheden voor automatisering en schaalbaarheid.

2. **Gebruik van AWS Elastic Load Balancer (ELB):** We hebben besloten om AWS Elastic Load Balancer te gebruiken voor de load balancing van onze webserver-instanties. Dit is gebaseerd op de volgende redenen:
    
    - ELB biedt hoge beschikbaarheid en schaalbaarheid, waardoor we het verkeer effectief kunnen verdelen over meerdere instanties.
    - Het biedt ingebouwde health checks om de status van de instanties te controleren en verkeer alleen naar gezonde instanties te leiden.
    - ELB is een beheerde service van AWS, wat betekent dat we ons geen zorgen hoeven te maken over het beheer en onderhoud van de load balancer-infrastructuur.

3. **Gebruik van AWS RDS voor databasebeheer:** We hebben gekozen voor Amazon RDS als ons beheerde databasesysteem vanwege de volgende redenen:
    
    - RDS biedt eenvoudige implementatie en beheer van relationele databases, waardoor we minder tijd hoeven te besteden aan handmatige configuratie en optimalisatie.
    - Het biedt automatische schaalbaarheid en back-upmogelijkheden, waardoor we ons kunnen richten op de ontwikkeling van onze applicatie in plaats van op het beheer van de database-infrastructuur.
    - Met RDS hebben we toegang tot geavanceerde databasefuncties en kunnen we verschillende database-engines gebruiken die het beste bij onze behoeften passen.