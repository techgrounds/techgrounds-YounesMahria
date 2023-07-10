## Node.js installeren

1) Ga naar https://nodejs.org/ en download LTS versie ervan.
2) Open de file en begin met het installeren.
3) Na het installeren moet je de PC opnieuw opstarten.


## AWS CDE Installeren

Ga naar de 'Ternimal' van 'Visual Studio Code':  
```
npm install -g aws-cdk
pip install cryptography
```

aws-cdk: Hierbij wordt de nieuwste release van cdk geinstalleerd.
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
```

Het kan zijn dat je dit moet gaan regelen.
```
python.exe -m pip install --upgrade pip
```