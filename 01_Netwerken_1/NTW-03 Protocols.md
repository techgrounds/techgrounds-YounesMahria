# Protocols
De relaties tussen elke protocols met hun OSI laag.

## Key-terms

Die worden in het kort bij het opdracht aangegeven.

## Opdracht

### Identify several other protocols and their associated OSI layer. Name at least one for each layer.

#### 7. Toepassingslaag (Application  Layer)  
De protocols zijn:  
* HTTP
* SMTP
* DHCP
* FTP
* Telnet
* SNMP
* SMPP

#### 6. Presentatielaag (Presentation Layer)  
De protocols zijn:  
* XDR
* TLS
* SSL
* MIME

#### 5. Sessielaag (Session Layer)  
De protocols zijn:  
- STMP
- FTP
- NetBIOS
- Socks
- RPC
- PPTP
- SAP
- L2TP

#### 4. Transportlaag (Transport Layer)  
De protocols zijn:  
* Transmission Control Protocol (TCP)
* UDP
* SPX
* DCCP
* SCTP

#### 3. Netwerklaag (Network Layer)  
De protocols zijn:  
- IP (E-mailverkeer gebruikt dit mestaal als TCP voer IP)
- Internet Protocol (IPv4)
- Internet Protocol (IPv6)
- ICMP
- X.25
- RIP
- OSPF
- IPX
- AppleTalk
- ICMP
- IPSec
- IGMP

#### 2. Datalinklaag (Data Link Layer)  
De protocols zijn:  
- Ethernet
- PPP
- ARP
- CSLIP
- HDLC
- IEEE.802.3
- X-25
- SLIP
- ATM
- SDLS
- PLIP

#### 1. Fysiekelaag (Physical Layer)  
De protocols zijn:  
- DSL
- ISDN
- Bluetooth
- USB
- Ethernet
- PON
- OTN
- IEEE.802.11 
- IEEE.802.3
- L431
- TIA 449

### Figure out who determines what protocols we use and what is needed to introduce your own protocol.

Er worden deze groepen genoemd die verantwoordelijke waren van de ontwikkeling en standaardisatie ervan. Ze hoeven niet exclusief vertandwoordelijke zijn voor de ontwikkeling ervan.
-   [The Institute of Electrical and Electronics Engineers](https://www.ieee.org/) (IEEE)  
	* Ethernet
	* Wi-Fi
	* Bluetooth
	* ZigBee

-   [The Internet Engineering Task Force](https://www.ietf.org/) (IETF)
	* TCP/IP
	* HTTP
	* DNS
	* FTP
	* SMTP
	* POP
	* IMAP
	* SIP

-   [The International Organization for Standardization](https://www.iso.org/home.html) (ISO)
	* OSI-Model
	* ISO 9000
	* ISO 14001
	* ISO 27001

-   [The International Telecommunications Union](https://www.itu.int/en/Pages/default.aspx) (ITU)
	* H.264
	* G.711
	* G.729
	* V.92
	* V.44

-   [The World Wide Web Consortium](https://www.w3.org/) (W3C)
	* HTML
	* XML
	* CSS
	* SOAP
	* WSDL
	* OWL
	* RDF

Er zijn aantal regels die je moet volgen om een nieuwe protocol te kunnen ontwikkelen en het introduceren ervan. Bij IETF moet je aantal stappen doorlopen.

1) Maak een account bij IETF
2) Lees de documenten van Internet-Draft door.
3) Vul het document van Internet-Draft in via IETF Datatracker Submission Tool
4) Het zal beoordeeld worden door aantal groepen die experts zijn op het gebied.
5) Als je voorstel geaccepteerd is dan wordt het uitgewerkt tot een RFC (Request for Comments).

### Look into wireshark and install this program. Try and capture a bit of your own network data. Search for a protocol you know and try to understand how it functions.

Op mijn Wifi worden vooral alleen maar UDP 99% en QUIC %1.  Dus voor deze ga ik de UDP protocol pakken waarvan ik bij Transportlaag (Laag 4) zit. 

De Afkomst (Source) of Bestemming (Destination) wordt aangeven zo kan het Afkomst van 159.124.7.158 (Zoom IP) naar Bestemming van Mij Lokale IP Adress dus ik download gegevens van Zoom naar mij Computer. Andersom is het dat ik upload gegevens van mij Computer naar Zoom.
De gegevens bestaat vooral uit Videobeeld met Audio die mijn webcam opneemt maar ook kunnen andere gegevens zijn zoals nieuwe tekstberichten.
`315921	780.588593	159.124.7.158	19x.xxx.xxx.xxx	UDP	1065	8801 → 55332 Len=1023`
![resultaat](/00_includes/NTW-03-resultaat.png "resultaat")

Nu staat er ook meer informatie eronder aan. Om ze in het kort door te nemen.
* Frame 315921: Dit is gewoon de ID die program zelf heeft aangegeven is tijdens het opnemen van pakketen.
* Ethernet II: Via welke netwerk apparteuren ging het die aangegeven worden met een MAC-address
* Internet Protocol Version 4: Ik gebruik IPv4 en niet IPv6 dus vandaar zie je de IPv4 addressen.
* Src Port: Afkomst ging via port 8801 naar de Bestemming via port 55332
* Data (1023 byes): Hoe groot de pakket was.
![resultaat](/00_includes/NTW-03-resultaat2.png "resultaat")

In het algemene over UDP: Het wordt gebruikt voor tijdnoods gegevensoverdracht zoals DNS-zoekopdracht, online gaming en video streamen. Waarbij dateverlies niet een zeer belangerijkerol speelt om het 100% correct te hebben, er kunnen aantal dataverlies zijn in zeer kleine %.

### Gebruikte bronnen
https://www.techopedia.com/definition/24961/osi-protocols
https://www.comptia.org/content/guides/what-is-a-network-protocol
https://www.iana.org/
https://www.ietf.org/how/ids/
https://www.ietf.org/standards/rfcs/
https://www.spiceworks.com/tech/networking/articles/user-datagram-protocol-udp/

### Ervaren problemen
Er zijn zo veel protocols die benoemd worden dat het veel is, er waren oud en nieuw genoemd.

### Resultaat
Het kunnen vinden welke protocolen bij welke lagen erbij horen en hoe ze in het algemeen werken.
