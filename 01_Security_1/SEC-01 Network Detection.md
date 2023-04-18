# Network detection
[Geef een korte beschrijving van het onderwerp]

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht

### Scan the network of your Linux machine using nmap. What do you find?  
In ternimal typ `sudo apt  install nmap -y`  
Daarna typ `nmap www.google.com 
![resultaat](/00_includes/SEC-01-resultaat.png "resultaat")  
In dit geval hebben gekeken voor een verbinden met `www.google.com`

Om te kunnen binnen onze netwerk typ `sudo apt install net-tools`
Dan typ `ifconfig -a`
![resultaat](/00_includes/SEC-01-resultaat2.png "resultaat")
Mij prive ip-adres is 10.171.154.90

We gaan alle network scannen op 10.171.154.x dus dan type 
`nmap 10.171.154.*`
![resultaat](/00_includes/SEC-01-resultaat3.png "resultaat")
Hier zie ik een lijst met alle Host-IDs die verbonden zijn binnen het Linux Netwerk.

### Open Wireshark in Windows/MacOS Machine. Analyse what happens when you open an internet browser.   
(Tip: you will find that Zoom is constantly sending packets over the network. You can either turn off Zoom for a minute, or look for the packets sent by the browser between the packets sent by Zoom.)  

De Wireshark filter gebruikt `!(ip.addr >= 159.124.14.0)`
![resultaat](/00_includes/SEC-01-resultaat4.png "resultaat")
Deze records is wat ik  gekregen heb. De IP van 169.254.169.254 blijkt van AWS te zien. De Broadcast vraagt waar het gestuurd moet worden en daarna beantwoord het met 192.168.178.87. Andere vraag was ook van 192.168.178.143 dat is mij prive ip adres van mij laptop en daarna beantwoord het met 192.168.178.1 namelijke de gateway.

### Gebruikte bronnen
https://www.geeksforgeeks.org/nmap-command-in-linux-with-examples/

### Ervaren problemen
Geen

### Resultaat
De uitkomst van de screenshots met de juist outputs en het kunnen aflezen van pakketten die niet van Zoom zijn.
