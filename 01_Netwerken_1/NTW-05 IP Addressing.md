# IP Addressing
De werking van het IP Addressen en de mogelijkeheden die er zijn.

## Key-terms

### IP adressen  
Elke apparateur die verbonden is met het netwerk krijgt een IP adres als een communcatie middel. Ze weet waar de internet pakketen naar toe moeten gaan als hun bestemming met hun eigen afkomst. 
  
### IPv4 en IPv6  
De IPv4 zijn opgesplits in 4 punten zoals 0.0.0.0. De waarde ervan is 0-255 waarvan ze Base 10 gebruiken. Elke van hun gebruiken 8-bit binary. Het zijn 32-bits nummers dus de mogelijkeheden zijn 2^32 = 4.294.967.296 dus bijna 4.3 miljard.

De IPv6 zijn opgesplits in 8 dubbele punten zoals: 2532:08d9:65e3:4ed8:f6f7:917c:1a19:a1a5. De waarde ervan is 0000-ffff waarvan ze Base 16 gebruken. De ffff = 65535. Het zijn 128-bits nummers dus de mogelijkeheden zijn 2^128 = 3,4028236692093846346337460743177e+38 dus 340 undecillion. 

De IPv5, ja 5 bestaat ook! Ze waren ermee bezig maar kwamen achter dat het ook zelfde problemen zou krijgen dat het ook 32-bits en base 10 gebruikte. Sinds IPv6 al in ontwikkeling was werd ontwikkeling IPv5 stop gezet wordt het nooit als standard werd gepubliceerd.
  
### Public en Private IPs  
De Public IPs zijn de IP addressen die nodig is voor het internet verkeer, dat is de IP address dat je krijgt van je ISP waardoor jij de enige bent met deze IP address op het internet. 

De Private IPs zijn de IP addressen die prive zijn in je eigen netwerk. Je apparteuren krijgen allemaal een Private IP adress die mestaal met 192.168. beginnen.  Het maakt niet uit of andere mensen zelfde IP adressen gebruiken want ze zitten niet in je eigen netwerk. De engine wat uit maakt dat je apparteuren niet zelfde IP krijgen.
  
### NAT  
De Network Address Translating (NAT) is een adresvertaling tussen de lokale netwerken en het internet.
  
### Statische en dynamische adressen  
Bij een statische adres wilt zeggen dat je een vaste IP adres hebt en die wordt niet veranderd.   

Bij een dynamische adres wilt zeggen dat je geen vaste IP adres hebt want die kan iedere keer veranderen bij een nieuwe verbinden zoals resetten van internet.


## Opdracht

### Ontdek wat je publieke IP adres is van je laptop en mobiel op wifi.  
Voor Laptop en Mobiel: verschillende websites zoals https://www.whatsmyip.org/

### Zijn de adressen hetzelfde of niet? Leg uit waarom.  
Ze zijn zelfde omdat ze beide verbonden zijn met het thuis Wifi, mijn mobieletelefoon zou wel een andere publieke IP hebben als ik de wifi uit zet.
   
### Ontdek wat je privé IP adres is van je laptop en mobiel op wifi.  
Op mijn laptop kan ik naar:
1) Start 
2) Type `cmd` en open Command Prompt
3) Type `ipconfig` en druk op enter
![resultaat](/00_includes/NTW-05-resultaat.png "resultaat")   

Voor mijn mobieletelefoon
1) Settings
2) About Phone
3) Status Information

**Mijn Laptop**
IPv4: 192.168.178.144
IPv6: fe80::3215:4cb8:8587:6686%35

**Mijn Mobiele**
IPv4: 192.168.178.31
IPv6: fe80::fe50:bb9f:4bb4:4e91
   
### Zijn de adressen hetzelfde of niet? Leg uit waarom.  
Nee, want elke apparatuur krijgt een aparte ip adres automatisch toegekend.
   
### Verander het privé IP adres van je mobiel naar dat van je laptop. Wat gebeurt er dan?  
De melding is nog steeds "Connected" verbinden van mijn mobiel probeert verbinden te maken er waren wel twee mogelijke uitkomst i.v.m. mobiel netwerk

A) Als mobiel netwerk uit is dan blijft het proberen maar de laden gaat zeer langzaam!
B) Als mobiel netwerk aan is dan na tijdje wordt de Wifi verbinden verbroken en wordt het via mobiel netwerk geprobeerd!
   
### Probeer het privé IP adres van je mobiel te veranderen naar een adres buiten je netwerk. Wat gebeurt er dan?  
Totaal geen verbinden wanneer ik het verander naar 212.63.55.22 krijg melding van "Connected without internet" dus verbonden met mij router maar geen toegang naar internet mogelijke.

### Gebruikte bronnen
https://www.networkworld.com/article/3588315/what-is-an-ip-address-and-what-is-your-ip-address.html
https://www.networkworld.com/article/3254575/what-is-ipv6-and-why-aren-t-we-there-yet.html
https://www.dnsbelgium.be/nl/nieuws/heerlijk-helder-verdwenen-ipv5
https://www.socallinuxexpo.org/sites/default/files/presentations/Why%20IP%20Versions%20and%20Why%20do%20I%20care.pdf


### Ervaren problemen
Geen

### Resultaat
De verschillen te kunnen onderscheiden tussen publieke en prive adress op je local netwerk en meer weten over de ontwikkelen van IPv4, IPv5 en IPv6.

