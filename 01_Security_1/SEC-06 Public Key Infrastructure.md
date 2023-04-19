# Public Key Infrastructure
Werking van certificaten met X.509 en Public Key Infrastructure

## Key-terms

### **X.509**  
Is een standaardformaat voor **certificaten met openbare sleutel**, digitale documenten die cryptografische sleutelparen veilig koppelen aan identiteiten zoals websites, individuen of organisaties.

### Public Key Infrastructure  
Is een systeem waarmee uitgifte en beheer van digitale certificaten wordt gerealiseerd. PKI is de basis van de SSL/TLS technologie. PKI bestaat uit verschillende onderdelen, die door dezelfde of verschillende entiteiten verzorgd kunnen worden:

## Opdracht

### Create a self-signed certificate on your VM.
De eerste stap is om openssl te installeren.
```
sudo apt install openssl
```

Daarna kunnen we het doen as volgt.
```
openssl req -newkey rsa:4096 \
            -x509 \
            -sha256 \
            -days 3650 \
            -nodes \
            -out example.crt \
            -keyout cloudengineer10YM.key
```

![resultaat](/00_includes/SEC-06-resultaat.png "resultaat")

* `newkey rsa:4096` - Een nieuwe certificatie maken en 4096 bit RSA key (Standaard is 2048 bits) 
* `x509` - Een X.509 Certificate maken.
* `sha256` - Gebruikt 265-bit SHA (Secure Hash Algorithm).
* `days 3650` - How lang het geldig is te certificeren. 3650 dagen is 10 jaren lang.
* `nodes` - Een sleutel maken zonder een passphrase.
* `out example.crt` - De filenaam kiezen voor het nieuwe certificatie file
* `cloudengineer10YM.key` - De filenaam kiezen voor het nieuwe private key file.

### Analyze some certification paths of known websites (ex. techgrounds.nl / google.com / ing.nl).

Dit is de certificaat voor Techgrounds:
![resultaat](/00_includes/SEC-06-resultaat2.png "resultaat")

Dit is de certificaat voor Google:
![resultaat](/00_includes/SEC-06-resultaat3.png "resultaat")

Dit is de certificaat voor Ing:
![resultaat](/00_includes/SEC-06-resultaat4.png "resultaat")

### Find the list of trusted certificate roots on your system (bonus points if you also find it in your VM).

**Voor Windows in Powershell**
```
Get-Childitem cert:\LocalMachine\root |format-list
```
![resultaat](/00_includes/SEC-06-resultaat5.png "resultaat")

**In Windows zonder Powershell**  
Druk op Start/Windows Logo en typ `mmc`    
Selecteer Bestand > Module toevoegen/verwijderen
Selecteer Certificaten > Toevoegen
Selecteer Computeraccount
![resultaat](/00_includes/SEC-06-resultaat6.png "resultaat")

**Voor Linux in onze VM**  
Dit wordt gebruikt te zien dat het geinstalleerd is
```
 dpkg -l | grep ca-certificates
```
![resultaat](/00_includes/SEC-06-resultaat7.png "resultaat")

Naar de locaties gaan en daarna de alle certificates.pem files in een lijst zetten.
```
cd /etc/ssl/certs/
ls -al
```

![resultaat](/00_includes/SEC-06-resultaat8.png "resultaat")

### Gebruikte bronnen
https://www.ssl.com/nl/veelgestelde-vragen/wat-is-een-x-509-certificaat/
https://www.sslcertificaten.nl/support/Terminologie/Public_Key_Infrastructure_(PKI)
https://linuxize.com/post/creating-a-self-signed-ssl-certificate/
https://woshub.com/updating-trusted-root-certificates-in-windows-10/

### Ervaren problemen
Geen

### Resultaat
De termen leren kennen en weten waar je certicaties kan vinden op je windows desktop of power shell en linux vm via terminal.