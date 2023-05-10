# Files, AppServices, CDN, DNS, Database
Vertellen hoe andere AWS services werken namelijke: Elastic Beanstak, Cloudfront, Route53, EFS, RDS en Aurora.

## Key-terms


### [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)
AWS Elastic Beanstalk implementeert webapplicaties zodat u zich kunt concentreren op uw bedrijf.
![resultaat](/00_includes/AWS-13-resultaat6.png "resultaat")

#### Vragen voor theoretisch onderzoek:
- ##### Waar is Elastic Beanstalk voor?
  AWS Elastic Beanstalk is een service voor het implementeren en schalen van webapplicaties en -services. Het ondersteunt webapplicaties die zijn geschreven in veel populaire talen en frameworks. Er zijn geen of minimale codewijzigingen nodig om van ontwikkelmachine naar de cloud te gaan. Ontwikkelingsopties voor het implementeren van uw webapplicaties zijn **Java, .NET, Node.js, PHP, Ruby, Python, Go en Docker.**
  
  #### Use cases:
  ##### 1) Start snel webapplicaties:  
  Implementeer binnen enkele minuten schaalbare webapplicaties zonder de complexiteit van het inrichten en beheren van de onderliggende infrastructuur. 
  ##### 2) Maak mobiele API-backends voor uw applicaties:  
  Gebruik je favoriete programmeertaal om mobiele API-backends te bouwen, en Elastic Beanstalk beheert patches en updates.
  ##### 3) Herplatform kritieke bedrijfsapplicaties:  
  Migreer stateful applicaties van de legacy-infrastructuur naar Elastic Beanstalk en maak veilig verbinding met uw privénetwerk.
  
- ##### Hoe past/vervangt 'Elastic Beanstalk' in een on-premises setting?
  Je uploadt je code en Elastic Beanstalk handelt automatisch de implementatie af - van capaciteitsvoorziening, load balancing en automatisch schalen tot het bewaken van de gezondheid van de applicatie. 
  
- ##### Hoe kan ik 'Elastic Beanstalk' combineren met andere [diensten](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.html)?  
  Je kan de volgende diensten van AWS combineren:
  1) [**AWS CloudFormation:**](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions-otherkeys.html) Voegt de inhoud van configuratiebestanden toe aan de AWS CloudFormation-sjabloon die uw omgeving ondersteunt, zodat u andere AWS CloudFormation-secties kunt gebruiken om geavanceerde taken in uw configuratiebestanden uit te voeren.
     
  2) [**Amazon EC2 Instances:**](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.ec2.html) Wanneer u een webserveromgeving maakt, maakt AWS Elastic Beanstalk een of meer Amazon Elastic Compute Cloud (Amazon EC2) virtuele machines, ook wel Instances genoemd.
     
  3) [**S3 Buckets:**](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.S3.html) Opslaan van uw applicatiebestanden en servelogbestanden.
     
  4) [**Amazon Cloudwatch:**](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.as.html) Integratie ervan voor het monitoringdashboard en alarmen instellen. Het komt met de Auto scaling groep die 2 alarms heeft ingesteld.
     
  5) [**Amazon RDS:**](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.RDS.html) Om een ​​relationele database op te zetten, te bedienen en te schalen.
     
  6) **Elastic Load Balancing / [Auto Scaling:**](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.as.html) Het bevat een Auto Scaling groep die de Amazon EC2-instanties in uw omgeving beheert.

  
- ##### Wat is het [verschil](https://aws.amazon.com/elasticbeanstalk/faqs/) tussen 'Elastic Beanstalk' en andere gelijksoortige diensten?  
  De meeste bestaande applicatiecontainers of platform-as-a-service-oplossingen verminderen weliswaar de hoeveelheid programmeerwerk die nodig is, maar verminderen de flexibiliteit en controle van ontwikkelaars aanzienlijk. Ontwikkelaars worden gedwongen te leven met alle vooraf door de leverancier bepaalde beslissingen, met weinig tot geen mogelijkheid om de controle over verschillende delen van de infrastructuur van hun applicatie terug te nemen. Met AWS Elastic Beanstalk behouden ontwikkelaars echter de volledige controle over de AWS-bronnen die hun applicatie aandrijven. Als ontwikkelaars besluiten dat ze sommige (of alle) elementen van hun infrastructuur willen beheren, kunnen ze dit naadloos doen door de beheermogelijkheden van Elastic Beanstalk te gebruiken.
  


### [CloudFront](https://aws.amazon.com/cloudfront/)
Amazon CloudFront is een content delivery network (CDN)-service die is gebouwd voor hoge prestaties, beveiliging en gemak voor ontwikkelaars.
![resultaat](/00_includes/AWS-13-resultaat5.png "resultaat")

#### Vragen voor theoretisch onderzoek:
- ##### Waar is 'Amazon CloudFront' voor?
  Het is een *Content Delivery Network (CDN)* dat wordt gebruikt om statische en dynamische webcontent snel (lage latentie) en veilig te leveren aan eindgebruikers.
  
  #### Use cases:
  ##### 1) Lever snelle, veilige websites:  
  Bereik kijkers over de hele wereld in milliseconden met ingebouwde datacompressie, edge-computingmogelijkheden en versleuteling op veldniveau. 
  ##### 2) Versnel de levering van dynamische inhoud en API's:  
  Optimaliseer de levering van dynamische webcontent met de speciaal gebouwde en feature-rijke AWS wereldwijde netwerkinfrastructuur die edge-terminatie en WebSockets ondersteunt.
  ##### 3) Stream live en on-demand video:  
  Start streams snel, speel ze consistent af en lever video van hoge kwaliteit aan elk apparaat met AWS Media Service en AWS Elemental-integratie.  
  ##### 4) Verspreid patches en updates:  
  Schaal automatisch om software, gamepatches en IoT over-the-air (OTA) updates op schaal te leveren met hoge overdrachtssnelheden.
  
- ##### Hoe past/vervangt 'Amazon CloudFront' in een on-premises setting?  
  In een on-premises setting, waarbij je je eigen infrastructuur beheert en onderhoudt, kun je nog steeds gebruikmaken van Amazon CloudFront om content snel en veilig te leveren aan eindgebruikers. Wanneer je een CloudFront-distributie maakt, kun je een aangepaste oorsprong opgeven, zoals een webserver in je on-premises datacenter. CloudFront haalt vervolgens de content op van de aangepaste oorsprong en levert deze aan eindgebruikers via het CloudFront-netwerk. CloudFront kan dus worden gebruikt als aanvulling op een on-premises infrastructuur om content snel en veilig te leveren aan eindgebruikers. Het vervangt echter niet de on-premises infrastructuur zelf.

  
- ##### Hoe kan ik 'Amazon CloudFront' combineren met andere diensten?  
  Je kan de volgende diensten van AWS combineren:
  1) **Amazon S3**: CloudFront kan worden geïntegreerd met Amazon S3 om content op te slaan en te leveren. Wanneer je een CloudFront-distributie maakt, kun je een Amazon S3-bucket selecteren als de oorsprong voor je content. CloudFront haalt vervolgens de content op uit de S3-bucket en levert deze aan eindgebruikers via het CloudFront-netwerk.
     
  2) **AWS Lambda**: Met AWS Lambda@Edge kun je aangepaste code uitvoeren in reactie op CloudFront-gebeurtenissen. Dit stelt je in staat om content aan te passen of te genereren in real-time, op basis van de kenmerken van het verzoek of de gebruiker.
     
  3) **Amazon Route 53**: Amazon Route 53 is een DNS-service die kan worden gebruikt om verkeer naar je CloudFront-distributie te routeren. Je kunt een aangepaste domeinnaam registreren bij Route 53 en deze gebruiken om verkeer naar je CloudFront-distributie te leiden.
     
  4) [**Amazon EC2:**](https://dx1572sre29wk.cloudfront.net/security/200_labs/200_cloudfront_for_web_application/1_config_cloudfront/) om content snel en veilig te leveren aan eindgebruikers. Wanneer je een CloudFront-distributie maakt, kun je een Amazon EC2-instantie selecteren als de oorsprong voor je content. CloudFront haalt vervolgens de content op uit de EC2-instantie en levert deze aan eindgebruikers via het CloudFront-netwerk.
  
  
- ##### Wat is het [verschil](https://aws.amazon.com/cloudfront/getting-started/?nc=sn&loc=4) tussen 'Amazon CloudFront' en andere gelijksoortige diensten?
  >**How does CloudFront compare to the traditional web services model?**
  >
  >**Let's compare the CDN model to the traditional web serving model.**  
  >Suppose you are serving a graphic file from a traditional web server. Your end-users can easily navigate to a URL which returns an image, as an example. If your web server is in Seattle, Washington, USA, and an end user makes a request to this URL from Austin, Texas, USA, the request will be routed to ten different networks before the image was retrieved. While this is not an unusually high number of requests, it does illustrate how much work is needed to retrieve even a single image.  
  >
  >This is where CloudFront can help to distribute your data. You can dramatically decrease the routing needed if you serve this image using CloudFront. The download distribution would detect where a request is being made and copy the file to a nearby edge location.  
  >
  >CloudFront improves performance and latency, reducing the time it takes to load the first byte of an object. This high data transfer rate allows the same file to be delivered to another user without latency. For that user, it will be served from the same edge location. You also get increased reliability and availability because there's no longer a central point of failure. Copies of your object will now be held in edge locations around the world.
  

### [Route53](https://aws.amazon.com/route53/)
Amazon Route 53 is een zeer beschikbare en schaalbare Domain Name System (DNS) webservice. Route 53 verbindt gebruikersverzoeken met internetapplicaties die op AWS of on-premises draaien.
![resultaat](/00_includes/AWS-13-resultaat4.png "resultaat")

#### Vragen voor theoretisch onderzoek:
- ##### Waar is 'Route 53' voor?
  Het is een zeer beschikbare en schaalbare Domain Name System (DNS) webservice. Route 53 verbindt gebruikersverzoeken met internetapplicaties die op AWS of on-premises draaien.
  
  #### Use cases:
  ##### 1) Beheer netwerkverkeer wereldwijd:  
  Creëer, visualiseer en schaal complexe routeringsrelaties tussen records en beleidsregels met gebruiksvriendelijke wereldwijde DNS-functies.. 
  ##### 2) Bouw applicaties met een hoge beschikbaarheid:  
  Stel routeringsbeleid in om reacties vooraf te bepalen en te automatiseren in geval van een storing, zoals het omleiden van verkeer naar alternatieve beschikbaarheidszones of regio's.
  ##### 3) Stel privé-DNS in:  
  Wijs aangepaste domeinnamen toe en krijg toegang tot uw Amazon Virtual Private Cloud (VPC). Gebruik interne AWS-bronnen en -servers zonder DNS-gegevens bloot te stellen aan het openbare internet. 
  
- ##### Hoe [past](https://aws.amazon.com/route53/features/#Functionality) 'Route 53' in een on-premises setting?  
  Binnen enkele minuten kan je aan de slag met de eenvoudige interface voor je webservices. De DNS-records zijn georganiseerd in "gehoste zones" die u configureert met de API van Route 53. Het is mogelijke om je domein over te zetten van een andere DNS-service naar Route 53. 
  
- ##### Hoe kan ik 'Route 53' [combineren](https://aws.amazon.com/route53/features/) met andere diensten?
  Je kan de volgende diensten van AWS combineren:
  1) **AWS CloudWatch**: 
     
  2) **Amazon CloudFront:** Wanneer u Amazon CloudFront gebruikt om uw website-inhoud te leveren, hebben bezoekers van uw website nu toegang tot uw site in de zone apex (of "root domain"). Uw site kan bijvoorbeeld worden geopend als voorbeeld.com in plaats van www.voorbeeld.com.
     
  3) **Amazon ELB Integration:** Amazon Route 53 is geïntegreerd met Elastic Load Balancing (ELB).
     
  4) **S3 Zone Apex Support:** Visitors to your website hosted on Amazon S3 can now access your site at the zone apex (or "root domain").
  
- ##### Wat is het verschil tussen 'Route 53' en andere gelijksoortige diensten?
  De andere soort gelijke dienste en mogelijkheiden om DNS-records voor je domeinen te beheren zijn: 
  1) Google Public DNS 
  2) OpenDNS
  3) Cloudflare DNS
  De grootste verschil is dat Route 53 werkt gemakkelijker met andere AWS-dienstenen. Het heeft geadvanceerd voor het monitoren van de gezondheid en prestaties van uw applicatie  ,webservers en andere bronnen.  


### [EFS](https://aws.amazon.com/efs/)
Amazon Elastic File System (EFS) groeit en krimpt automatisch terwijl je bestanden toevoegt en verwijdert zonder dat beheer of provisioning nodig is.
![resultaat](/00_includes/AWS-13-resultaat3.png "resultaat")
https://aws.amazon.com/efs/faq/

#### Vragen voor theoretisch onderzoek:
- ##### Waar is ['Elastic File System (EFS)'](https://aws.amazon.com/efs/faq/) voor?
  Het) is ontworpen om serverloze, volledig elastische bestandsopslag te bieden waarmee u bestandsgegevens kunt delen zonder opslagcapaciteit en -prestaties in te richten of te beheren. Met een paar selecties in de AWS Management Console kunt u bestandssystemen maken die toegankelijk zijn voor Amazon Elastic Compute Cloud (EC2)-instanties, Amazon-containerservices (Amazon Elastic Container Service [ECS], Amazon Elastic Kubernetes Service [EKS] en AWS Fargate) en AWS Lambda werken via een bestandssysteeminterface (met behulp van standaard bestands-I/O-API's van het besturingssysteem). Ze ondersteunen ook de volledige semantiek van toegang tot het bestandssysteem, zoals sterke consistentie en bestandsvergrendeling. 
  
  #### Use cases:
  ##### 1) Vereenvoudig DevOps:  
  Deel code en andere bestanden op een veilige, georganiseerde manier om de flexibiliteit van DevOps te vergroten en sneller te reageren op feedback van klanten.
  ##### 2) Moderniseer applicatie-ontwikkeling:  
  Houd vol en deel gegevens uit uw AWS-containers en serverloze applicaties met nul beheer vereist.
  ##### 3) Verbeter contentmanagementsystemen:  
  Vereenvoudig persistente opslag voor werklasten van moderne contentmanagementsystemen (CMS). Breng uw producten en diensten sneller, betrouwbaarder en veiliger op de markt tegen lagere kosten. 
  ##### 4) Versnel datawetenschap:  
  Amazon EFS is gemakkelijker te gebruiken en te schalen en biedt de prestaties en consistentie die nodig zijn voor machine learning (ML) en big data-analyseworkloads.
  
- ##### Hoe [past](https://aws.amazon.com/efs/faq/#On-premises_access) 'Elastic File System (EFS)' in een on-premises setting?
  U kunt uw Amazon EFS-bestandssystemen op uw lokale servers koppelen en bestandsgegevens van en naar Amazon EFS verplaatsen met behulp van standaard Linux-tools en -scripts of AWS DataSync. De mogelijkheid om bestandsgegevens van en naar Amazon EFS-bestandssystemen te verplaatsen, maakt drie gebruiksscenario's mogelijk.
  
  1) Gegevens van on-premises datacenters migreren naar permanent verblijf in EFS-bestandssystemen.
  2) Cloud bursting-workloads ondersteunen om uw applicatieverwerking naar de cloud te verplaatsen. U kunt gegevens van uw lokale servers verplaatsen naar uw Amazon EFS-bestandssystemen, deze analyseren op een cluster van EC2-instanties in uw Amazon VPC en de resultaten permanent opslaan in uw Amazon EFS-bestandssystemen of de resultaten terugzetten naar uw on-premises lokale servers.
  3) Periodiek uw lokale bestandsgegevens naar Amazon EFS kopiëren om back-up- en noodherstelscenario's te ondersteunen.
  
  ##### Hoe vervangt 'Elastic File System (EFS)' in een on-premises setting?
  Door gebruik te maken van andere AWS diensten zoals VPC met EC2 instanties. Je moet wel volledige overstappen om alleen AWS diensten te gebruiken of je bouwt de omgeving op begin erin. Hierdoor krijg je geen hoge latentie vanwege de afstand tussen jouw on-premises datacentrum en AWS VPC.
  
- ##### Hoe kan ik 'Elastic File System (EFS)' combineren met andere diensten?  
  Je kan de volgende diensten van AWS combineren.
  1) Amazon EC2
  2) Amazon ECS
  3) Amazon EKS
  4) AWS Fargate
  5) AWS Lambda
  
- ##### Wat is het verschil tussen 'Elastic File System (EFS)' en andere gelijksoortige diensten?
  **Bij AWS** heb je ook de optie voor S3 en EBS, belangrijkste verschil tussen deze diensten is hoe ze gegevens opslaan en hoe ze toegang bieden tot die gegevens. 
1) **Amazon EFS:** biedt gedeelde toegang tot gegevens met behulp van een traditioneel bestandsdelingsmachtigingenmodel en hiërarchische directorystructuur via het NFSv4-protocol.
2) **Amazon S3:** slaat gegevens op als objecten en biedt toegang via een API.
3) **Amazon EBS:** biedt directe bloktoegang tot gegevens vanaf een enkele EC2-instance.
4) **Azure File Storage:** maakt gebruik van het standaard server message block (SMB)-protocol. Amazon EFS maakt gebruik van het NFSv4-protocol voor toegang tot gegevens. 
  
#### Vragen voor praktisch onderzoek:
- ##### Waar kan ik 'Elastic File System (EFS)' vinden in de console?
- ##### Hoe zet ik 'Elastic File System (EFS)' aan?
- ##### Hoe kan ik 'Elastic File System (EFS)' koppelen aan andere resources?
  Zie het opdracht die ik gemaakt van EFS onderaan.
  

### [RDS](https://aws.amazon.com/rds/)
Amazon Relational Database Service (Amazon RDS) is een verzameling beheerde services die het opzetten, bedienen en schalen van databases in de cloud eenvoudig maakt. Kies uit zeven populaire engines - Amazon Aurora met MySQL-compatibiliteit, Amazon Aurora met PostgreSQL-compatibiliteit, MySQL, MariaDB, PostgreSQL, Oracle en SQL Server - en implementeer on-premises met Amazon RDS op AWS Outposts.
![resultaat](/00_includes/AWS-13-resultaat2.png "resultaat")

#### Vragen voor theoretisch onderzoek:
- ##### Waar is ['Amazon Relational Database Service (Amazon RDS)'](https://aws.amazon.com/rds/features/) voor?
 Het is een beheerde relationele databaseservice die zeven bekende database-engines biedt 
 1) Amazon Aurora MySQL-Compatible Edition
 2) Amazon Aurora PostgreSQL-Compatible Edition
 3) MySQL
 4) MariaDB
 5) PostgreSQL
 6) Oracle 
 7) Microsoft SQL Server
 
 Dit betekent dat de code, applicaties en tools die u vandaag al gebruikt met uw bestaande databases, kunnen worden gebruikt met Amazon RDS. Amazon RDS voert routinematige databasetaken uit, zoals provisioning, patching, back-up, herstel, foutdetectie en reparatie.
  
##### Hoe past 'Amazon Relational Database Service (Amazon RDS)' in een on-premises setting?
  Zoals eerder aangeven kan het werken met deze 5 voor on-premises:
 1) MySQL
 2) MariaDB
 3) PostgreSQL
 4) Oracle 
 5) Microsoft SQL Server

##### Hoe vervangt 'Amazon Relational Database Service (Amazon RDS)'  in een on-premises setting?
Zoals eerder aangeven kan het werken met deze 2 die on-premises vervangt:
1) Amazon Aurora MySQL-Compatible Edition
2) Amazon Aurora PostgreSQL-Compatible Edition
  
##### Hoe kan ik 'Amazon Relational Database Service (Amazon RDS)'  combineren met andere diensten?  
  Je kan de volgende diensten van AWS voor je combineren.
  1) AWS Aurora
  Deze volgenden diensten zijn buiten van AWS om maar wel mogelijke:
  1) MySQL
  2) MariaDB
  3) PostgreSQL
  4) Oracle
  5) Microsoft SQL Server
  
##### Wat is het verschil tussen 'Amazon Relational Database Service (Amazon RDS)'  en andere gelijksoortige diensten?
Het belangrijkste verschillen tussen deze services is hoe ze gegevens opslaan en hoe ze toegang bieden tot die gegevens. 
1) **Amazon RDS:** biedt ondersteuning voor meerdere database-engines, waaronder Amazon Aurora, MySQL, MariaDB, Oracle Database, SQL Server en PostgreSQL 
2) **Microsoft Azure SQL Database:** biedt ondersteuning voor de SQL Server-database-engine 2. 
3) **Google Cloud SQL:** biedt ondersteuning voor MySQL en PostgreSQL 
  
  
#### Vragen voor praktisch onderzoek:
- ##### Waar kan ik 'Amazon Relational Database Service (Amazon RDS)' vinden in de console?
- ##### Hoe zet ik 'Amazon Relational Database Service (Amazon RDS)' aan?
- ##### Hoe kan ik 'Amazon Relational Database Service (Amazon RDS)' koppelen aan andere resources?
  Zie het opdracht die ik gemaakt van Amazon Relational Database Service (Amazon RDS) onderaan.
  

### [Aurora](https://aws.amazon.com/rds/aurora/)
Amazon Aurora biedt ingebouwde beveiliging, continue back-ups, serverloze rekenkracht, tot 15 leesreplica's, geautomatiseerde multiregionale replicatie en integraties met andere AWS-services.
![resultaat](/00_includes/AWS-13-resultaat.png "resultaat")

#### Vragen voor theoretisch onderzoek:
- ##### Waar is[ 'Amazon Aurora'](https://aws.amazon.com/rds/aurora/features/) voor?
  Het is een r**elationele databaseservice** die de snelheid en beschikbaarheid van hoogwaardige commerciële databases combineert met de eenvoud en kosteneffectiviteit van open-sourcedatabases. Aurora is volledig compatibel met MySQL en PostgreSQL, waardoor bestaande applicaties en tools zonder aanpassingen kunnen worden uitgevoerd.
  
- ##### Hoe past / vervangt 'Amazon Aurora' 'Amazon Aurora' in een on-premises setting?
  Dat is niet mogelijke om het als on-premises te kunnen gebruiken vandaar bieden ze het ook een migraties aan voor PostgreSQL en MySQL. Hierdoor wordt je on-premises volleidge vervangen en overgezegt op Amazon Aurora. Hiervoor moet je RDS on Outpost gebruiken. Het is een onderdeel van RDS als een optie voor PostgreSQL en MySQL.
  
- ##### Hoe kan ik 'Amazon Aurora' combineren met andere diensten?  
  Je kan de volgende diensten van AWS voor je combineren.
  1) AWS RDS (Blue/Green Deployments)
  2) AWS Outposts
  3) AWS CloudWatch


- ##### Wat is het verschil tussen 'Amazon Aurora' en andere gelijksoortige diensten?  
  Het belangrijkste verschillen tussen deze services is hoe ze gegevens opslaan en hoe ze toegang bieden tot die gegevens. 
1) **Amazon Aurora:** biedt ondersteuning voor meerdere database-engines, waaronder Amazon Aurora, MySQL, MariaDB, Oracle Database, SQL Server en PostgreSQL 
2) **Microsoft Azure SQL Database:** biedt ondersteuning voor de SQL Server-database-engine 2. 
3) **Google Cloud SQL:** biedt ondersteuning voor MySQL en PostgreSQL 
  
  
#### Vragen voor praktisch onderzoek:
- ##### Waar kan ik 'Amazon Aurora' vinden in de console?
- ##### Hoe zet ik 'Amazon Aurora' aan?
- ##### Hoe kan ik 'Amazon Aurora' koppelen aan andere resources?
  Zie het opdracht die ik gemaakt van Amazon Aurora onderaan.
  
  

## Opdracht  

### Use EFS to make Standard Storage Class on your VPC on two AZ Public subnets. Mount the EFS to your ES2 Instance.
Na Opdrachten van AWS10 te hebben gedaan dan doe als volgt.

https://eu-north-1.console.aws.amazon.com/efs?region=eu-north-1#/file-systems

Na druk je op 'Create file system'
![resultaat](/00_includes/AWS-13-resultaat7.png "resultaat")

We gaan 'Customize' doen en niet 'Create'
![resultaat](/00_includes/AWS-13-resultaat8.png "resultaat")

Bij 'Name' = 'Lab EFS'
Bij 'Storage class' = 'Standard'
Bij 'Automatic backups' = 'Off/Unchecked' (voorkomen voor onverwachte kosten bij aws free tier)
![resultaat](/00_includes/AWS-13-resultaat9.png "resultaat")

Bij 'Virtual Private Cloud (VPC)' = 'Lab VPC'
Bij 'Mount targets > Subnet ID' = 'Public(s)'
Bij 'Mount targets > Security groups' = 'ELB SG'
![resultaat](/00_includes/AWS-13-resultaat10.png "resultaat")
*Dit is meer aangeven als dat het beschikbaar is op deze AZ en Subnets ervan. Dus dit zou niet werken op Private als die er niet tussen in staan.* 

Bij 'File system policy _- optional_' = 'Prevent root access by default*'
![resultaat](/00_includes/AWS-13-resultaat16.png "resultaat")

Bij 'Review and create' controleren en dan op 'Create' drukken.

Nu is de 'EFS' aangemaakt dus we gaan op 'Lab EFS' drukken om het te openen.
![resultaat](/00_includes/AWS-13-resultaat11.png "resultaat")

We kunnen op 'Attach' drukken
![resultaat](/00_includes/AWS-13-resultaat12.png "resultaat")

Het geeft instructies voor het 'Mount via DNS' of 'Mount via IP'
![resultaat](/00_includes/AWS-13-resultaat13.png "resultaat")

We gaan weer terug naar een van onze 'Instance' bij 'EC2' die op Public subnet staat. Dus op 'Connect' en daarna weer op 'Connect' 
![resultaat](/00_includes/AWS-13-resultaat14.png "resultaat")
*Als je een error krijgt betekent dat je firewall het blokeert of dat je niet de juiste instellingen hebt gedaan bij VPC voor Internet gateway of NAT*

Terug bij 'EC2 - Console'
We gaan het proberen om het te 'Mount' en deze code proberen zoals aangeven boven aan. 

Ket kan zijn dat je dit moet nog gaan uitvoeren.
```
sudo yum install -y amazon-efs-utils
```


```
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-0f0ef8f3b732760b7.efs.eu-central-1.amazonaws.com:/ efs
```

Zoals verwacht krijgen we een error. namenlijke 'please install botocore first'
![resultaat](/00_includes/AWS-13-resultaat15.png "resultaat")

We gaan 'botocore' installeren/upgrade
```
sudo pip3 install botocore --upgrade
```
![resultaat](/00_includes/AWS-13-resultaat17.png "resultaat")

Nu krijg je waarschijnlijke weer een andere problem 'mount point efs does not exist'
![resultaat](/00_includes/AWS-13-resultaat18.png "resultaat")

Onthoud bij vorige opdracht toen we ook gingen 'Mount' doen, je moet ook een nieuwe folder maken dus:
```
mkdir efs
```

Nu nog keer proberen:
```
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-0f0ef8f3b732760b7.efs.eu-central-1.amazonaws.com:/ efs
```

Weer een andere probleem, dit keer is het een 'failed due to timeout' om dit te kunnen oplossen gaan we als volgt doen.

Terug naar 'EC2 > Security Groups'
Bij 'Inbound rules > Edit inbound rules > Add rules' dan moet je 'NTS' toevoegen met zelfde waardes als 2 andere.
![resultaat](/00_includes/AWS-13-resultaat21.png "resultaat")

Bij 'Outbound rules > Edit outbound rules > Add rules' dan moet je 'NTS' toevoegen met zelfde waardes als 2 andere.
![resultaat](/00_includes/AWS-13-resultaat22.png "resultaat")

Terug bij 'EC2 - Console'
Nu krijg je geen foutmelding meer en de 'Mount' is geslaagd!
![resultaat](/00_includes/AWS-13-resultaat23.png "resultaat")

We kunnen zien dat de EFS ook op de lijst staat:
```
df -h
```
Mounted on =  'home/ec2-user/efs' 
Filesystem =  '127.0.0.1' 
Size = '8.0E' (0used/8.0E Availble) 
![resultaat](/00_includes/AWS-13-resultaat24.png "resultaat")

AWS heeft er gekozen om het als 8.0E te laten zien omdat het elastic is. Je betaald hoeveel data je gebruikt.

Je kan ook deze code gebruiken om het te verifiëren.
```
mount -t nfs4
```

![resultaat](/00_includes/AWS-13-resultaat25.png "resultaat")

### Make 1GB file on your EFS Mount and confirm that EFS increased in size. 

Om een file aan te maken krijg we weer zelfde probleem met 'Permission denied' Dit zou je snel kunnen oplossen met:
```
sudo chown `whoami` /home/ec2-user/efs/
```
*zorg ervoor dat je een map terug bent van /efs/ > cd ..*

Dit keer gaat het niet werken:
`chown: changing ownership of ‘/home/ec2-user/efs/’: Operation not permitted`

Terug bij 'EFS > Lab EFS' 
Bij 'File system policy > Edit > Clear > Save' zodat het leeg staat
Deze probleem kwam omdat een of beide aan stonden:
1) Prevent root access by default 
2) Enforce read-only access by default
![resultaat](/00_includes/AWS-13-resultaat26.png "resultaat")

Terug bij 'EC2 - Console'
We moeten het unmounten en weer mounten dus
```
sudo umount /home/ec2-user/efs/
sudo mount -t efs -o tls fs-0f0ef8f3b732760b7:/ efs
```

Nu moet de volgende codes wel werken
```
sudo chown `whoami` /home/ec2-user/efs/
cd efs/
echo "techgrounds" >> test.txt
ls -l
```

Terug bij 'EFS > Lab EFS'
We zien bij 'Metered size' nog '6.0Kib' staan
![resultaat](/00_includes/AWS-13-resultaat27.png "resultaat")

Terug bij 'EC2 - Console'
We zien ook bij console het nog aangeven wordt met '6.0K'
![resultaat](/00_includes/AWS-13-resultaat28.png "resultaat")

We gaan weer terug in 'efs' folder om een dummy file te maken:
```
fallocate -l 1G test.img
```

of

```
openssl rand -out sample.txt -base64 $(( 2**30 * 3/4 ))
```

Na een tijdje zie je dat '1.02GiB' is geworden.
![resultaat](/00_includes/AWS-13-resultaat29.png "resultaat")

### Create a Access Point
Terug bij 'EFS > Lab EFS' 
Dit komt door de 'Access points' nog leeg staan dus druk op 'Create access point'.
![resultaat](/00_includes/AWS-13-resultaat19.png "resultaat")

Bij 'Name' = 'Lab EFS Access'
![resultaat](/00_includes/AWS-13-resultaat20.png "resultaat")

### Create RDS that's connected to your EC2 Instance on your VPC.
We beginnen met het maken met een RDS (Database)
https://eu-north-1.console.aws.amazon.com/rds/?region=eu-north-1#

Om te beginnen druk je op 'Create database'
![resultaat](/00_includes/AWS-13-resultaat30.png "resultaat")

We gaan 'Standard create' selecteren om een nieuwe database te maken.
![resultaat](/00_includes/AWS-13-resultaat31.png "resultaat")

Bij 'Engine type' = 'PostgreSQL' (eigenlijke Aurora, maar geen free tier)
Bij 'DB instance size' = 'Free tier'
Bij 'DB instance identifier' = 'lab-db-id' 
Bij 'Master username' = 'eigen naam' met 'Auto generate a password' aan gevinkt.
![resultaat](/00_includes/AWS-13-resultaat32.png "resultaat")

Bij 'Compute resource' = 'Connect to an EC2 computer resource'
Bij 'EC2 Instance' = 'Web server' (de Instance we vorige opdracht gebruiken, public subnet 2 / 10.0.2.0)
![resultaat](/00_includes/AWS-13-resultaat33.png "resultaat")

Nu druk je op 'Create Database'

Als je dit ziet dan druk je op 'Close' om verder te gaan.
![resultaat](/00_includes/AWS-13-resultaat34.png "resultaat")

Let op deze waarschuwing die er komt!
![resultaat](/00_includes/AWS-13-resultaat35.png "resultaat")

Je krijgt deze 3 informatie te zien.
Master username = younes
Master password = 31banl6sNFIaHK440WtN
Endpoint = jdbc:postgresql://lab-db-id-instance-1.cnplp6iqjoyy.eu-central-1.rds.amazonaws.com:5432/lab-db-id
![resultaat](/00_includes/AWS-13-resultaat36.png "resultaat")

Nu heb ik een postgreSQL gemaakt!

---
### Create Aurora that's connected to your EC2 Instance on your VPC.

![resultaat](/00_includes/AWS-13-resultaat45.png "resultaat")

We gaan 'Standard create' selecteren om een nieuwe database te maken.
![resultaat](/00_includes/AWS-13-resultaat46.png "resultaat")

Bij 'Engine type' = 'Aurora (PostgreSQL Compatible)'
Bij 'Available versions' = 'Aurora PostgreSQL (Compatible with PostgreSQL 14.7)'
![resultaat](/00_includes/AWS-13-resultaat47.png "resultaat")

Bij 'Templates' = 'Dev/Test'
![resultaat](/00_includes/AWS-13-resultaat51.png "resultaat")

Bij 'DB cluster identifier' = 'lab-db-id' 
Bij 'Master username' = 'eigen naam' met 'Auto generate a password' aan gevinkt.
![resultaat](/00_includes/AWS-13-resultaat40.png "resultaat")

Bij 'DB instance class' = 'Burstable classes > db.t3.medium'
![resultaat](/00_includes/AWS-13-resultaat44.png "resultaat")

Bij 'Availability & durability' = 'Don't create an Aurora Replica'
![resultaat](/00_includes/AWS-13-resultaat48.png "resultaat")

Bij 'Compute resource' = 'Don't to an EC2 computer resource'
Bij 'Network' = 'IPv4'
Bij 'Virtual Private VPC' = 'je default VPC'
Bij 'Public access' = 'yes'
Bij 'VPC security group' = 'create new of choose existing'
Bij 'Availability Zone' = 'eu-central-1a'
![resultaat](/00_includes/AWS-13-resultaat41.png "resultaat")

Bij 'Alles hier onderaan' = 'uitgevinkt'
![resultaat](/00_includes/AWS-13-resultaat43.png "resultaat")

Bij 'Initial database name' = 'labdbtechbase'
![resultaat](/00_includes/AWS-13-resultaat50.png "resultaat")

Dan druk op 'Create database'

Als je dit ziet dan druk je op 'Close' om verder te gaan.
![resultaat](/00_includes/AWS-13-resultaat34.png "resultaat")

Je krijgt deze 3 informatie te zien.
Master username = younes
Master password = QxBvPitXZeO0ePJg1NZe
Endpoint = lab-db-id.cluster-cnplp6iqjoyy.eu-central-1.rds.amazonaws.com
![resultaat](/00_includes/AWS-13-resultaat52.png "resultaat")

Nu heb ik een Aurora (PostgreSQL Compatible) gemaakt!

---
#### Use SQL workbench to connect to your RDS.  
*Als je nog niet hebt gedaan, installeer 'PostgreSQL' waarbij het paar minuten kan duren voordat het klaar is.*

Ga naar Database dasboard: https://eu-central-1.console.aws.amazon.com/rds/home?region=eu-central-1#databases

Selecteer 'lab-db-id-instance-1'
Endpoint = lab-db-id-instance-1.cnplp6iqjoyy.eu-central-1.rds.amazonaws.com
Port = 5432
![resultaat](/00_includes/AWS-13-resultaat53.png "resultaat")

Selecteer 'Configuration'
DB-name = 'labdbtechbase'
![resultaat](/00_includes/AWS-13-resultaat54.png "resultaat")

URL bestaat uit
```
jdbc:postgresql://ENPOINT:PORT/DB-name
```

Dus volledige URL:
```
jdbc:postgresql://lab-db-id.cluster-cnplp6iqjoyy.eu-central-1.rds.amazonaws.com:5432/labdbtechbase
```

Username = younes
Password = QxBvPitXZeO0ePJg1NZe

![resultaat](/00_includes/AWS-13-resultaat55.png "resultaat")

Dus volledige URL:
```
jdbc:postgresql://lab-db-id.cluster-cnplp6iqjoyy.eu-central-1.rds.amazonaws.com:5432/labdbtechbase
```

Resultaat:
![resultaat](/00_includes/AWS-13-resultaat56.png "resultaat")
*URL is van een andere database url maar rest is het zelfde.*

### Gebruikte bronnen
https://aws.amazon.com/elasticbeanstalk/
https://aws.amazon.com/cloudfront/
https://aws.amazon.com/route53/
https://aws.amazon.com/efs/
https://aws.amazon.com/rds/
https://aws.amazon.com/rds/aurora/

https://aws.amazon.com/efs/faq/
https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html
https://computingforgeeks.com/mount-aws-efs-file-system-on-ec2/
https://docs.aws.amazon.com/cli/latest/reference/rds/index.html

https://aws.amazon.com/getting-started/hands-on/create-connect-postgresql-db/

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.html

https://aws.amazon.com/elasticbeanstalk/details/

### Ervaren problemen  
Troubleshooting bij EFS maar kwam snel tot de oplossingen terecht. 

Bij RDS/Auroa krijg ik steeds een fout melding "SQL State = 08001" einde van de dag, hierdoor kon ik niet vinden waar de probleem precies lag maar kwam volgende dag er snel achter dat het kwam door de 'Security group' instellingen en nog 'PostgreSQL' open moest. 

![resultaat](/00_includes/AWS-13-resultaat57.png "resultaat")

### Resultaat
Weten hoe andere AWS services werken namelijke: Elastic Beanstak, Cloudfront, Route53, EFS, RDS en Aurora.

