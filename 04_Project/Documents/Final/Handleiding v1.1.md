## Handleiding 

### Node.js installeren
1. Ga naar [https://nodejs.org/](https://nodejs.org/) en download de LTS-versie.
2. Open het gedownloade bestand en start de installatie.
3. Na de installatie moet je de computer opnieuw opstarten.

### AWS CDK Installeren
1. Open de 'Terminal - bash' van 'Visual Studio Code'.
2. Voer de volgende commando's uit om de volgende 5 pakketten te installeren:
```bash
npm install -g aws-cdk
pip install boto3
pip install pymysql
pip install cryptography
pip install cdk-create-ami
```
 Hier is een korte uitleg van de geïnstalleerde pakketten:
- **aws-cdk:** AWS Cloud Development Kit (CDK) voor het schrijven van nieuwe AWS resource.
- **boto3:** AWS Software Development Kit (SDK), andere functions die niet bij CDK horen zoals controleren van een bestaand resource.

Hier is een korte uitleg van de geïnstalleerde pakketten:
- **aws-cdk:** AWS Cloud Development Kit (CDK) voor het schrijven van nieuwe AWS resources.
- **boto3:** AWS Software Development Kit (SDK) voor andere functies die niet bij CDK horen, zoals het controleren van bestaande resources.

De 3rd-party tools zijn van externe partijen die losstaan van AWS:
- **pymysql:** Nodig voor het instellen van je MySQL met de Lambda-functie voor het post-deployment-script.
- **cryptography:** Dit is een 3rd-party tool die wordt gebruikt voor het aanmaken van RSA Keys-bestanden.
- **cdk-create-ami:** Voor het maken van een AMI (Amazon Machine Image) - Optioneel.

Nadat je alles hebt geïnstalleerd, maak je een nieuwe folder aan:
```bash
mkdir The_MVP_Project cd The_MVP_Project/
```    
**LET OP:** De folder moet leeg blijven!

Initialiseer een nieuw CDK-project met de Python-taal:
```bash
cdk init --language python
```

Installeer de vereiste packages:
```shell
pip install -r requirements.txt python.exe -m 
pip install --upgrade pip
```

Nadat dit gelukt is, zet je alle bestanden die je van ons hebt ontvangen in de 'The_MVP_Project'-folder.

### Variables 
Bij het bestand `'_variables.py'` moet je nog de juiste IP's vervangen met de voorbeelden: 
**OFFICE_IPS:** Vul hier de IP's van je werkomgeving 
**HOME_IPS:** Vul hier de IP's van je thuiswerkers.

**LET OP:** Gevoelige informatie mag niet worden geüpload naar GitHub. De admin moet de lijst apart bewaren en verwijderen voordat er wordt gecommit.

Voordat je het gaat deployen, moet je eerst de volgende code uitvoeren.
```shell
cdk synth
```
Nadat alles is doorgelopen, zou je geen foutmeldingen moeten krijgen.

Nu ga je de AWS-omgeving deployen:
```shell
cdk deploy --all --require-approval never
```
**LET OP:** Hierdoor sla je alle prompt-vragen over!

De keypairs zijn aangemaakt. Je kunt de public key terugvinden in de AWS-console. In de 'rsakeys'-folder heb je de private keys.

**Let op:** Zorg ervoor dat je alle private key-bestanden veilig bewaart in de 'rsakeys'-folder en verwijder ze daarna. Commit nooit de project-folder naar GitHub met de key-bestanden. Je hebt hier een waarschuwing over gekregen.

### Verbinding naar de Webserver vanaf/via Management server
```
eval `ssh-agent -s
ssh-add management_private_key.pem app_private_key.pem
``` 
- Vraag de IP-adressen op bij de verantwoordelijke die toegang heeft tot die informatie. Je kunt de twee IP-adressen vinden in de AWS Management Console bij de EC2 Instance.
- 
- Vervang de 'public IP' van de Management Instance en de 'private IP' van de Webserver Instance in de volgende code:
```shell
ssh -J Administrator@3.71.11.255 ec2-user@<private IP>
```

### Testen van de Webserver-RDS Databaseverbinding

Ga naar de AWS Secret Manager ([https://eu-central-1.console.aws.amazon.com/secretsmanager/listsecrets?region=eu-central-1](https://eu-central-1.console.aws.amazon.com/secretsmanager/listsecrets?region=eu-central-1)) om de 'rds endpoint' en 'wachtwoord' op te halen.

Op de Terminal:
```bash
sudo yum install mariadb 
```

Maak een MySQL-verbinding met de volgende code, waarbij je de "rds endpoint" gebruikt:
```
mysql -h <rds endpoint> -P 3306 -u admin -p`
```
**Uitgebreide Documentatie:**  Voor meer informatie [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.html)

