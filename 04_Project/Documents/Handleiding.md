## Node.js installeren

1) Ga naar https://nodejs.org/ en download LTS versie ervan.
2) Open de file en begin met het installeren.
3) Na het installeren moet je de PC opnieuw opstarten.


## AWS CDE Installeren

Ga naar de 'Ternimal' van 'Visual Studio Code':  
```
npm install -g aws-cdk
```

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