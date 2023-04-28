# AWS Global Infrastructure
Algemene informatie hoe de AWS Global Infrastructure werkt.

## Key-terms  

### Latentie  
Het is de vertragingstijd die nodig is om gegevens van de ene naar de andere locaties binnen een netwerk te verplaatsen. Het wordt gementen in millieseconds dus dat betekend lager is sneller en hoger is langzamer. Het wordt beïnvloed door verschillende factoren. Zoals de snelheid en bandbreedte van een netwerk.

## Opdracht

### What is an AWS Availability Zone?  
Het zijn **beschikbaarheidszones** die in meerdere locaties zijn binnen in dezelfde AWS-regio. Ze zijn ontworpen voor: 
- Geïsoleerd te zijn van storingen in andere **Availability Zone**
- Goedkope netwerkconnectiviteit 
- Lage latentie naar andere **Availability Zone**

### What is a Region?  
Het is verzameling in een geografischgebieden waarbij elke **regio** geïsoleerd en onafhankelijk is.  Elke **regio** bestaat uit meedere Availability Zones (meestal 3).

Veder biedt het deze voordelen op:
- Fouttolerantie
- Stabiliteit
- Weerstand

De lijst ervan zijn (niet alles genoemd):
* **Noord-Amerika:**
  - Oregeon
  - Northern Virginia
  - Northern California
  - Ohio
  
* **Europa:**
  - Ireland
  - Frankfurt
  - London
  - Paris

* **Azië-Pacific:**
  - Singapore
  - Tokyo
  - Seoul

- **Australia:**
  - Sydney
  - Melbourne

* **Midden-Oosten:**
  - Bahrain
  - UAE

- **Afrika:**  
  - Cape Town

* **Zuid-Amerika:**
  - São Paulo
  

### What is an Edge Location?  
Een Edge-locaties zijn tientallen AWS-datacenters die zijn ontworpen om services te leveren met de laagst mogelijke latentie. Ze staan verspreid over de hele wereld en dichterbij de gebruikers dan *Regions en Availability Zones*.  Het biedt de volgende functies aan:

- **CloudFront** 
  Het gebruikt kopieën van de inhoud die in de cache opgeslagen zijn. Dit zorgt ervoor dat de inoud dichterbij en sneller kan worden geleverd aan de gebruikers.
  
- **Route 53**
  Het is een DNS service voor de Edge Location die ervoor zorgt dat de DNS-query sneller kunnen worden opgeslot.
  
- **Web Application Firewall en AWS Shield**
  Het filteren van ongewenst verkeer om zo snel mogelijk te stoppen.

### Why would you choose one region over another? (e.g. eu-central-1 (Frankfurt) over us-west-2 (Oregon)).  
In zeer makkelijke reden te noemen is namelijke dat de afstand naar Frankfurt veel dicterbij is dan Oregon vanaf Nederland.  Dat heeft te maken met Latentie.

Er kunnen nog drie andere belangerijke reden zijn voor het kiezen van een Regio. In zijn algemeen heb je deze 4 reden:
- **Latentie** 
  Een betere gebruikerservaring vanwege de afstand tussen de gebruikers wat eerder werd genoemd. Het kan de communicatiekwaliteit verbeteren, aangezien netwerkpakketten minder uitwisselingspunten hebben om doorheen te reizen.

- **Wet** 
  Naleven van een lokale wetgeving in dat land van de gegevens die worden opgeslagen.
  
- **Kosten** 
  Elke regio is anderes gesprijsd wat ervoor zorgt kostenverlaging.
  
- **Diensten en functies** 
  De grotere regio's zijn meestl de eersten die nieuwere services, funcites en softwarereleases aanbieden. Kleinere regio's krijgen deze niet op tijd.


### Gebruikte bronnen
https://aws.amazon.com/about-aws/global-infrastructure/
https://docs.aws.amazon.com/sap/latest/general/arch-guide-architecture-guidelines-and-decisions.html
https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/RegionsAndAZs.html
https://www.lastweekinaws.com/blog/what-is-an-edge-location-in-aws-a-simple-explanation/
https://www.capterra.nl/glossary/603/latency
https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/
https://aws.amazon.com/about-aws/global-infrastructure/regions_az/?p=ngi&loc=2

### Ervaren problemen
Geen problemen ervaren door de documentatie goed door te nemen.

### Resultaat
Het kunnen beschreven hoe AWS Global Infrastructure werkt in het kort.
