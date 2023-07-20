## Node.js installeren

1) Ga naar https://nodejs.org/ en download LTS versie ervan.
2) Open de file en begin met het installeren.
3) Na het installeren moet je de PC opnieuw opstarten.

## AWS CDK Installeren

Ga naar de 'Ternimal' van 'Visual Studio Code':  
```
npm install -g aws-cdk
pip install boto3
pip install cryptography
pip install cdk-create-ami
```


aws-cdk: Hierbij wordt de nieuwste release van cdk geïnstalleerd.
cryptography: Is een 3rd party tool die ervoor zorgt voor het aanmaken van RSA Keys bestanden. 

**LET OP: zorg ervoor dat je alle key files in 'rsakeys' folder veilig bewaard en ze daarna weghaalt. Nooit de project folder commit naar de github met de key files.** 

Maak en open de nieuwe map:  
```
mkdir The_MVP_Project
cd The_MVP_Project/
```

Initialize een nieuwe CDK project:
```
cdk init --language python
```

Daarna:
```
pip install -r requirements.txt
python.exe -m pip install --upgrade pip
```

Het kan zijn dat je dit moet gaan regelen.
```
```

Voor de SSH verbinding vanaf je Management naar de Webserver moet je de volgende codes uitvoeren. Zorg wel eerst ervoor dat je in de juiste folder zit met je keys.
```
eval `ssh-agent -s`
ssh-add management_private_key.pem app_private_key.pem
```

De IP adressen zijn altijd random dus die moet je zelf opvragen bij de verantwoordelijke die toegang heeft die informatie. Bij AWS Management Console kan je naar de EC2 Instance gaan om de twee ips te krijgen. 

Vervang de 'public ip'  van de Management Instance.
Vervang de 'private ip' van de Webserver Instance

```
ssh -J Administrator@<public ip> ec2-user@<private ip>
```

Dit is de test voor de Webserver om verbinding te maken met de RDS Database.

Om de 'rds endpoint' en 'wachtwoord' moet je naar de AWS Secret Manager gaan.  https://eu-central-1.console.aws.amazon.com/secretsmanager/listsecrets?region=eu-central-1

	Je kan nu MySQL connectie maken met de volgende code, zorg ervoor dat je de "rds endpoint" ermee.
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.html

```
sudo yum install mariadb
mysql -h <rds endpoint> -P 3306 -u admin -p
```

https://docs.aws.amazon.com/lambda/latest/dg/services-rds-tutorial.html
mkdir package
pip install pymysql


pip install py7zr


```
cd package
zip -r ../lambda_function.zip .
```