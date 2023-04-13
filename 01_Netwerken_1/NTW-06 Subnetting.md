# Subnetting
Hoe een subnet werkt.

## Key-terms  

### Subnets  
Een deelnetwerk binnen een netwerk. Het is slimmer manier op elke verdieping een eigen netwerk maken. Daardoor kan je een IP-adres splitsen. Het eerste deel wordt gebruikt om het subnet te identificeren  en de overblijvende bits vormen het Host-ID die elke computer krijgt.
![resultaat](/00_includes/NTW-06-resultaat.png "resultaat")

De subnetten wordt ook gesplits in 3 klassen waarvan 2 klassen niet gebruikt wordt voor het prive netwerk.

**Klassa-A:**  255.0.0.0 dan is de eerste octal 0-127 (0.0.0.0 - 127.255.255.255)
**Klassa-B:**  255.255.0.0 dan is de eerste octal 128-191 (128.0.0.0 -191.255.255.255)
**Klassa-C:**  255.255.255.0 dan is de eerste octal 192-223 (192.0.0.0 - 223.255.255.255)
**Klassa-D:** Geen, is voor multicasting (224.0.0.0 – 239.255.255.255)
**Klassa-E:** Geen, is voor experimentele doeleinden (240.0.0.0 – 255.255.255.255)

### LAN  
Een Local Area Network (LAN) het zorgt ervoor dat minimaal 2 apparaten met elkaar kunnen communiceren binnen het lokaal netwerk. Dit zorgt ervoor dat het sneller gaat met uitwisselen van gegevens.


## Opdracht  

### 1 private subnet dat alleen van binnen het LAN bereikbaar is. Dit subnet moet minimaal 15 hosts kunnen plaatsen.  

Dit is de diagram voor 1 prive subnet binnen het Lan bereikbaar is omdat er geen NAT-gataway zit.
![resultaat](/00_includes/NTW-06-resultaat2.png "resultaat")

### 1 private subnet dat internet toegang heeft via een NAT gateway. Dit subnet moet minimaal 30 hosts kunnen plaatsen (de 30 hosts is exclusief de NAT gateway).  

Dit is de diagram voor 1 prive subnet met internet toegang via een NAT gateway waardoor er geen toegang mogelijke is dat buiten komt van het internet.
![resultaat](/00_includes/NTW-06-resultaat3.png "resultaat")


### 1 public subnet met een internet gateway. Dit subnet moet minimaal 5 hosts kunnen plaatsen (de 5 hosts is exclusief de internet gateway).  

Dit is 1 public subnet met een internet gateway.
![resultaat](/00_includes/NTW-06-resultaat4.png "resultaat")

### Gebruikte bronnen
https://www.providercheck.nl/kennisbank/bericht/wat-is-subnet
https://nordvpn.com/nl/blog/subnetmasker-berekenen/
https://spinware.nl/kennisbank/wat-is-een-lan-verbinding/
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html

### Ervaren problemen
Goed erover nagedacht hoe de diagram eruit zou moeten zien maar hield het gewoon zeer simple genoeg hoe ik het had begrepen. 

### Resultaat
Het kunnen uitleggen hoe een subnet werkt een diagrams ervan kunnen tekeningen.
