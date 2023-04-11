# Network Devices
De netwerkapparaten en hun relatie met de OSI-Model.


-   Netwerkapparaten  
-   Het OSI model in relatie tot deze netwerkapparaten  


## Key-terms

### Modem  
Het is een afkorting voor  Modulator Demodulator. Dit is noodzakkelijke onderdeel om toegang te kunnen krijgen tot het internet. Het vertaald de internetsignaal van je provider, zodat al je apparaten het kunnen gebruiken. Dus het zorgt ervoor een verbidingen met het internet via de provider.

> OSI-Model: Datalinklaag (Data Link Layer) - Laag 2

### Router  
Het zorgt ervoor dat meedere apparaten het internet thuis kan gebruiken. Het is een  communicatie tussen alle apparaten die is gebouwd door kabels of draadloos op het netwerk. 

**Let op: Vaak krijg je al 2 in 1 van je providers dat zijn modem en router in 1 apparaat. **

> OSI-Model: Fysiekelaag (Physical Layer) - Laag 1
> OSI-Model: Datalinklaag (Data Link Layer) - Laag 2
> OSI-Model: Netwerklaag (Network Layer)   - Laag 3

### Switch  
Een veerdeelkastje waar alle kabels aangesloten worden tussen de computers. Dit is zeer geschikt om met grote groep te gamen.

De voordelen:  
* Geen vertraging.
* Iedere heeft zijn eigen port.

De nadelen:  
* Veel kabels

> OSI-Model: Datalinklaag (Data Link Layer) - Laag 2
> OSI-Model: Netwerklaag (Network Layer)   - Laag 3

### Repeaters  
Een apparaat dat je WiFi-signaal versterkt. 

De voordelen:  
* Geen kabels nodig.
* Alleen stop contact nodig. 
* Niet ingewikkeled te instellen
* Geschikt voor simpele taken

De nadelen:  
* Snelheid wordt minder 
* Niet echt geschikt voor gamen of streamen.

> OSI-Model: Fysiekelaag (Physical Layer) - Laag 1

### Access point  
Het is een apparaat dat een WLAN of draadloos lokaal netwerk creëert. Het maakt verbinding via een Ethernet-kabel naar een bedrade router, switch of hub. Het stuur een WiFi-signaal naar een bepaald gebieden.  Geschikt voor groot gebouw waar de signal van router niet wordt bereikt.

De voordeel:  
* Hogere capaciteit voor je wifi dan een repeater.

> OSI-Model: Fysiekelaag (Physical Layer) - Laag 1
> OSI-Model: Datalinklaag (Data Link Layer) - Laag 2

## Opdracht

### Benoem en beschrijf de functies van veel voorkomend netwerkapparatuur

[Zie Key-terms](#Key-terms)


### De meeste routers hebben een overzicht van alle verbonden apparaten, vind deze lijst. Welke andere informatie heeft de router over aangesloten apparatuur?

De andere informatie die op mij 'router' staat.
* Device naam (Apparatuurnaam):  De naam van apparatuur.
* MAC Address: De unieke ID van het hardware.
* IP Address (Lokaal): Op welke lokaal IP address het heeft en verbonden is met poort.
* Speed (Mbps): De snelheid die het kan hebben.
* Connected to: Welke port via het kabel of WiFi is het verbonden.
![resultaat](/00_includes/NTW-02-resultaat.png "resultaat")
*De informatie is eruit gefilteerd vanwege privacy*

### Waar staat je DHCP server op jouw netwerk? Wat zijn de configuraties hiervan?

Het staat onder Advanced settings > DHCP
![resultaat](/00_includes/NTW-02-resultaat2.png "resultaat")

De volgende configuraties zijn.  
* DHCPv4 server:  
  'This sections allows you to configure how the Connect Box assigns IPv4 addresses. It is configured to be a DHCP (Dynamic Host Configuration Protocol) server by default. This provides the TCP/IP configuration for all connected devices.'

* Reserved IP addresses:  
  'Attached devices'
  Dus welke apparaten verbonden zijn.

* Add reserved rule:  
Een vaste lokale IP address reserveren voor apparaturen.

* Reserved list:  
Een lijst zien met de geserveerde IP address voor de apparaturen.


### Gebruikte bronnen
https://www.kliksafe.nl/blogs/techniek/verschil-router-accesspoint-repeater/
https://www.brunel.net/nl-nl/faq/it/router
https://www.linksys.com/nl/what-is-a-wifi-access-point.html
Eigen router ip link.

https://www.spiceworks.com/tech/networking/articles/modem-vs-router/
https://www.ptindustrieelmanagement.nl/layer-2-vs-layer-3-netwerk-switches-wat-is-het-verschil/
https://www.freecodecamp.org/news/osi-model-networking-layers-explained-in-plain-english/

### Ervaren problemen
Niet de access point verwaren met de SSID. De juist OS-model vinden voor elke netwerkapparteur.

### Resultaat
De termen kunnen uitleggen en het vinden op welke OSI-modellen liggen. Verder zit schreenshots bij voor de benodige vragen.
