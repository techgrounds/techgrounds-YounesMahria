# Firewalls
Verschillen termen van firewalls weten en het blokkeren van ports behalve SSH.

## Key-terms

### Stateful Firewall  
Het inspecteert alles wat in de datapakketten zitten, de data kenmerken en de communicatiekanalen. Verder kijkt het naar het gedrag van datapakketten als er iets niet klopt om ze als verdachte gegevens eruit filteren. Ook kan door de gedragspatronen te cataloiseren.

### Stateless Firewall  
Het maakt gebruik van de bron, bestemming en andere parameters van een datapakket om erachter te komen of de gegevens een bedreiging vormen. De vooraf ingestelde regels voor deze parameters moeten worden ingevoerd doro een beheerder of de fabrikant. Als een datapakket niet voldoet aan de regel, zal de dreiging geidentificeerd worden en vervolgens de bevatte gegevens blokkeren of beperken.


### Hardware Firewall  
Een fysieke apparateur die onafhankelijke werkt van de computer waardor het systeem filtert


### Software Firewall  
Een applicatieprogramma die binnen je computer werkt waardoor het gebruikt wordt voor pakketten die binnen en uit gaan.


## Opdracht  

### Installeer een webserver op je VM.  
Op Week 1 had ik een script geschereven.
`bash scripts/InstallHttpd.sh`
In het kort wat het doet:
```
sudo apt-get install -y apache2
sudo systemctl start apache2
sudo systemctl enable apache2
sudo systemctl status apache2  
```

### Bekijk de standaardpagina die met de webserver geïnstalleerd is.  
Typ http://18.157.179.30:58011/ in my webbrowser
![resultaat](/00_includes/SEC-02-resultaat01.png "resultaat")  
Zoals boven aangegeven "Apache2 Ubuntu Welcome Page"

### Stel de firewall zo in dat je webverkeer blokkeert, maar wel ssh-verkeer toelaat.  

De status van 'Ubuntu Firewall' (inactive voor de eerste keer).
```
sudo ufw status
```

Alle internet verkeer wordt geblokeerd.
```
sudo ufw default deny incoming
```

De ssh-verkeer toestaan.
```
sudo ufw allow OpenSSH
```

Nu zetten we de firewall aan
```
sudo ufw enable
```

### Controleer of de firewall zijn werk doet.  
Controleren door deze code te doen.
```
sudo ufw status verbose
```
![resultaat](/00_includes/SEC-02-resultaat2.png "resultaat")

Als ik nu weer probeer te laden dan krijg ik dat het niet bereikbaar is.
![resultaat](/00_includes/SEC-02-resultaat02.png "resultaat")


### Gebruikte bronnen
https://www.fortinet.com/resources/cyberglossary/stateful-vs-stateless-firewall
https://www.fortinet.com/resources/cyberglossary/hardware-firewalls-better-than-software
https://www.cyberciti.biz/tips/linux-iptables-4-block-all-incoming-traffic-but-allow-ssh.html
https://linuxconfig.org/how-to-deny-all-incoming-ports-except-ssh-port-22-on-ubuntu-18-04-bionic-beaver-linux

### Ervaren problemen
Verschillende mogelijkeheden waardoor deze eronder niet wat ik nodig had om het te kunnen doen.
```
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT
sudo ip6tables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo ip6tables -A OUTPUT -p tcp --sport 22 -j ACCEPT
```
Andere probleem was dat andere porten zoals 80 er nog steeds open waren.  Dit heb ik gedaan toen.
```
sudo ufw disable
sudo ufw reset
sudo ufw default deny incoming
sudo ufw allow ssh
sudo ufw enable
```
Daarna was alleen nog port 22 in de lijst.

Hoewel ik de opdracht eerder begrijp omdat ik te gefocuseed was in de linux vm had ik daarna op mij webbrowser gedaan om webpage te laden.

### Resultaat
Weten wat de verschillen zijn tussen de firewalls en hoe je ports kan blokkeren, resetten in Linux met UFW.
