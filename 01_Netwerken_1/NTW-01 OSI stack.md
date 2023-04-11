# OSI stack
Uitleg geven over de OSI Model en TCP/IP Model.


## Key-terms



## Opdracht
Het bestuderen van de volgende kenmerken
-   The OSI model and its uses.
-   The TCP/IP model and its uses.

### Wat is een OSI Model?  
Het staat voor Open System Interconnection Model (OSI Model) waarbij door International Organization for Standardization (ISO) als poging tot een standaardiseren. OSI Model is een conceptueel kader voor een communicatiestandaards die niet afhankelijke zijn van fabrikanten. Het OSI-referentiemodel zelf is geen concrete netwerkstandaard omdat het abstracte vorm geeft welke  operaties worden geregeld.

Door het complexe netwerkcommunicaties proces wordt het in zeven lagen uitgelegd waarbij elke laag een specifieke taken worden uitgevoerd door communicaties tussen twee apparteren. 
- Communicatieregeling.
- De adressering van het doelsystem.
- Omzetten van datapakketten in fysieke signalen.


Dat lukt echt alleen als zich aan de protocellen regels aanhouden die aansluiten op afzonderlijke lagen. 

### De 7 lagen van OSI Model
![resultaat](/00_includes/NTW-01-resultaat.png "resultaat")

### Toepassingsgeoriënteerde lagen (Software / Upper Layers)
----
#### 7. Toepassingslaag (Application  Layer)
Heeft direct contact met toepassingen zoals webbrowsers of e-mailprogramma's waarij gegevens worden uitgewisseled. Het brengt verbinding met de lagere niveaus tot stand en houdt functies voor toepassingen gereed. 

E-mailprogramma Voorbeeld:
- Gebruiker schrijft een bericht in gmail.
- Dit bericht wordt in deze laag geladen in vorm van een datapakket.
- Extra informatie wordt toegevoegd in vorm van een 'Inkapselen(Application Header)'.
- Deze header bevat pakket gegevens die afkomstig zijn van een e-mailprogramma.
- *Daarnaast wordt het protocol bepaald dat gebruikt wordt voor de overdracht van de e-mail op de toepassingslaag (in het geval van een e-mail meestal SMTP).*


#### 6. Presentatielaag (Presentation Layer)  
Een centrale taak bij de netwerkcommunicatie is ervoor te zorgen dat gegevens in standaardformaten worden overgedragen. In deze laag wordt he vertaald van lokale weergeven naar een gestandaardiseerde formaten.

E-mailoverdracht Voorbeeld:
- Bepaald hoe het bericht moet worden wergeven.
- Het datapakket wordt aangevuld met een 'Presentation Header'.
- Deze header bevat infromatie over hoe de e-mail 
	- Gecodeerd (NL meestal ISO 8859-1 (Latin-1) of ISO 8859-15).
	- Formaat als bijlagen aanwezig zijn (JPEG, MPEG4 etc).
	- Hoe gegevens gecomprimeerd of versleuteld zijn (SSL/TLS).
Daardoor kan het doelsysteem de formaat van de e-mail begrepen en het bericht correct weergegeven.


#### 5. Sessielaag (Session Layer)  
De centrale taak in de sessielaag wordt volbracht en het regelen van de verbinding tussen de twee eindsystemen of ook wel communicatielaag genoemd. 
- Speciale regel- en controlemechanismen actief die het tot stand komen
- Onderhouden en beëindigen van de verbinding regelen. 

E-mailgegevens Voorbeeld:
- Extra informatie nodig dat wordt door de 'Seassion Header' toegevoegd.

De applicatieprotocollen die houden zich zelf met de sessie bezig of zijn net als HTTP toestandsloos:
- STMP
- FTP
- NetBIOS
- Socks
- RPC

Het TCP/IP-Model dat concurreert met het OSI-model vat daarom OSI lagen 5,6 en 7 tot een application layer.

----


### Hart van OSI (Heart of OSI) 
----
#### 4. Transportlaag (Transport Layer)  
De schakel tussen de toepassingsgeoriënteerde en de transportgeoriënteerde lagen.  

Hier wordt de volgende aspecten gerealiseerd.
- De logische end-to-endverbinding.
- Het overdrachtskanaal.
- Tussen de communicerende systemen

E-mailgegevens Voorbeeld:
- Het datapakket bevat alle headers van toepassingsgeoriënteerde lagen is uitgebreid.
- Deze laag vult het met een 'Transport Header'

De gestandaardiseerde netwerkprotocollen als TCP of UDP worden gebruikt. Bepaald viw welke poorten toepassingen op het doelsysteem kunnen worden aangestuurd. De datapakket ook een bepaalde toepassing toegewezen.

Verschillende bronnen beschouwen het of de upper layer of de lower layer. Hoewel meer recent is dat het niet meer van beide toe behoort en zijn eigen layer benaming krijgt. 

----


### Transportgeoriënteerde lagen (Hardware / Lower Layers)
----
#### 3. Netwerklaag (Network Layer)  
Het bereikt de gegevensoverdracht het internet. Hier worden eindapparaten logisch geadresseerd waarvan eenduidig IP-adres toegewezen.

E-mailgegevens Voorbeeld:
- Datapakket krijgt 'Network Header' toegevoeged
- Deze bevat informatie over de routering en de controle van de gegevensstroom.

De computersystemen maken gebruiken van de internetstaandards als:
- IP (E-mailverkeer gebruikt dit mestaal als TCP voer IP)
- ICMP
- X.25
- RIP
- OSPF

#### 2. Datalinklaag (Data Link Layer)  
Heeft de functies voor:  
- Het herkennen van fouten.  
- Het verhelpen van fouten.  
- Het voorkomen van overdrachtsfouten door de gegevensstroom te controleren.  

Het Datapakket omgeven door een frame van data link header en data link trail:
- Application
- Presentation
- Session
- Transpor
- Network Header

De MAC-Adressen wordt gebruikt voor toegang tot het medium wordt geregeld door protocolllen:
- Ethernet
- PPP


#### 1. Fysiekelaag (Physical Layer)  
De bits van datapakket worden omgezet in een fysiek signaal dat bij het overdrachtsmedium past. Deze signaal kan alleen overgedragen worden via een medium als:
- Koperdraad
- Glasvezel
- De lucht

Het interface naar het overdrachtsmedium wordt bepaaltd door Protocollen en normen:
- DSL
- ISDN
- Bluetooth
- USB
- Ethernet
----

Dus de OSI-Model helpt met het beschreven van netwerk architectuur of het oplossen van netwerk problemen.



### Wat is een TCP/IP model?  
Het staat voor Transmission Control Protocol/Internet Protocol. Het regelt de communcaties tussen  de computers bij het uitwisselen van gegevens. Het is een van de belangrijkste protocollen voor gegevensoverdracht op het internet. Daarbij moet het ervoor zorgen dat het met succes, zonder fouten of haperingen en in de juiste volgorde worden ontvangen. 

Dit is hoe TCP een verbinding tot stand brengt tussen twee computers (een proces dat bekend staat als een "three-way handshake"):

> 1.  De ene computer (de zender) stuurt een eerste bericht naar de ontvangende computer met het formele verzoek een verbinding tot stand te brengen. Dit staat bekend als een SYN-bericht (afkorting voor synchroniseren).
> 2.  De ontvangende computer moet dan een bevestiging van de SYN sturen (een zogenaamd SYN-ACK bericht). 
> 3.  Ten slotte moet de verzender de bevestiging bevestigen (bekend als een ACK RECEIVED-bericht).

Nadat deze drie stappen met succes zijn voltooid, kan de gegevensoverdracht beginnen. 


### De vier lagen van TCP/IP Model
----
### 1. Toepassingslaag  
De toepassingen zoals webbrowsers en omvat verdere protocollen zoals:
- **HTTPS**: Hypertext transfer protocol. Transfer date in form of text,audio or video.
- **SMTP**: Simple Network Management Protocol, Send date to another email adress.
- **DNS**: Domain Name System, Identify the connection to host to the internet uniquely.
- **Telnet**: Terminal Network, Connection between local and remote computer.
- **FTP**: File Transfer Protocol, Transmitting Files between 2 computers.


### 2. Transportlaag  
Na het ontvangen van toepassingen gegegevens wordt het hier gecommuniceerd. Er wordt gekeken naar welke port het moet waarbij de pakketten in stukjes gesneden worden met hun eigen header. De header bevat instructies over hoe de payload van het pakket moet worden afgeleverd.

Het is verandertwoordelijke van gegevens die over netwerk worden verzonden:
- Betrouwbaarheid
- Stroomcontroler
- Correctie


### 3. Internetlaag  
Elk pakket wordt voorzien met herkomst- en bestemmings IP-addressen die de Internet Protocol gebruiken. 


### 4. Netwerklaag  
Hier wordt de gegevens omgezet in elektrische impulsen en de wereld in gestuurd. Het behandelt informatie zoals MAC (Media Access Control) die ervoor zorgen dat elk pakket naar de juiste computer gaan. 

> Het is combinatie van Fysiekelaag (Physical Layer) en Datalinklaag (Data Link Layer) OSI Model.

----

### De Onderscheiding
Hoewel ze zelfde lijken te zijn zit er toch aantal verschillen er tussen. Zo is het bij

#### Zelfde
- Communicatie tussen computers over een netwerk.

#### Verschillen
- OSI heeft 7 lagen en TCP/IP heeft 4 lagen.
- OSI is Abstracte en Theoreitsch benadering van netwerkcommunicatie. Elke laag heeft een specifieke functie en is duidelijke gescheiden van de andere lagen.
- TCP/IP is pragmatisch van aard en beschrijft lagen van de belangrijkste protocollen die gebruikt worden.

### Overeenkomen
Dit is een overzicht hoe de lagen met elkaar overeenkomen. 
![resultaat](/00_includes/NTW-01-resultaat2.png "resultaat")



### Gebruikte bronnen
https://www.strato.nl/server/wat-is-het-osi-model/
https://www.ict-ruyters.nl/it-kennisbank/ict-begrippenlijst/tcp-ip-model/
https://massive.io/nl/bestandsoverdracht/wat-is-transmissie-controle-protocol-tcp/
https://www.simplilearn.com/tutorials/cyber-security-tutorial/what-is-tcp-ip-model

https://www.javatpoint.com/computer-network-tcp-ip-model

https://vitolavecchia.altervista.org/main-differences-between-the-iso-osi-model-and-tcp-ip/

https://linuxhint.com/network-osi-layers-explained/
https://www.novell.com/documentation/suse91/suselinux-adminguide/html/ch14.html
https://www.oreilly.com/library/view/linux-network-administrators/1565924002/ch01s02.html

https://www.techtarget.com/searchnetworking/definition/OSI
https://www.techtarget.com/searchnetworking/definition/TCP-IP



### Ervaren problemen
Veel lezen en het goed en duidelijke vertalen in het engelse. Er waren gewoon te veel informatie waarbij ik het gewoon simple wil houden. Daarbij was ook een meiningverschil met laag 4 upper  layer, lower layer of geen van beide maar heart of OSI.

### Resultaat
Het kunnen begrijpen en beter uitleggen wat OSI Model en TCP/IP Model.
