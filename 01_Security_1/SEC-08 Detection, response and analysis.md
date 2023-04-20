# Detection, response and analysis
De stappenplan voor cyberaanval.

## Key-terms

### Hackreactie strategie (Hack response strategies.)
is een documentie plan om snel en effectief te regeageren op een hack of een cyberaanl voor een organisatie.  Het bestaat uit 3 fases namelijke.

### 1. Detectie (Detection)  
---- 
De eerste stap om het te stoppen en het voorkomen voor meedere pogingen. Zoals Wireshark die helpt met het scannen van je internet verkeer. Het gebruikt

#### 1.1 Intrusiedetectie (Intrusion Detection systems)    
Een Intrusiedetectie (IDS) is het proces waarbij uw netwerkverkeer wordt bewaakt en geanalyseerd op tekenen van mogelijke inbraken, zoals pogingen tot misbruik en incidenten die een onmiddellijke bedreiging voor uw netwerk kunnen vormen.

#### 1.2 Inbraakpreventie (Intrusion Prevention Systems)    
Een Inbraakpreventie (IPS) is het proces waarbij inbraken worden gedetecteerd en vervolgens de gedetecteerde incidenten worden gestopt, meestal door packetdrops of sessies te beëindigen. 

### 2. Disaster Recovery Plan (DRP)  
---- 
Het is een gestructureerde document aanpak die beschrijf hoe een bedrijf snel het werk kan hervatten na een ongeplande incident.

#### 2.1 Reactie (Response)  
Het snelle reactie op een aanval, om te proberen de schade te beperken. De manier om dat te beperken is afhangelijke wat voor aanval het is. Nadat je weet hoe je het kan stoppen kan je beginnen met het herstel fase, waar je probeert om alle systems weer online zien te krijgen en inventariseert de aangerichte schade.

#### 2.2 Analysis (Analyse) 
Een document maken wat je geleerd hebt van het aanval en harden van je system om te voorkomen dat deze aanvallen gebeueren. Soms is het simple as OS updating van je servers.

#### 2.2.1 Disaster Recovery 
is een service en oplossingen die in staat is om de functioneren van het bedrijfsprocess door te laten gaan wanneer een aanval voorkomt.

##### 2.2.1.1 Disaster Recovery as a Service 
De herstel omegeving is een volledig spiegel van uw hoofd omgeving. Wanneer de hoofd omegeving onbereikbaar is door een aanval, kan je verder werken in de herstel omgeving.

##### 2.2.1.2 RPO
Recovery Point Objective (RPO) is de maximal acceptable hoeveel dataverlies je kwijt bent tijdens de aanval. 

##### 2.2.1.3 RTO  
Recovery Time Objective (RTO) is de maximaal acceptable tijd voor hoe lang het duurt voordat je weer online bent.

#### 2.2.2 Systems hardening
Wordt gebruikt om zo veel mogelijke veiligheidsrisico's te elmineren.  Bij besturingssysteem wordt de overbodige functies en/of software uit te zetten of verwijderen van het systeem. 
Bijvoorbeelden:
1. Strengere wachtwoordbeleid
2. Toegang tot bestanden en directories
3. Systeemrechten
4. Kernalparameters
5. Netwerkinstellingen
6. Verwijderen/Uitschakelen van onndige gebruiker-accounts
7. Patch/Updatebeleid


## Opdracht

### A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?  
De RPO is de meeste recent beschikbaar backup gebruiken. Hierbij wordt dagelijkse backups gemaakt. Dus hun maximal acceptable hoeveel dataverlies is niet meer dan 1 dag. 

### An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?   
De RTO is om het ongeveer in 8 minuten weer online te zijn. Dat is het automatische aanzetten van de backup web server en daarna de newest vesie pullen uit GitHub.

 
### Gebruikte bronnen
https://www.techtarget.com/searchdisasterrecovery/definition/disaster-recovery-plan
https://cloudian.com/guides/disaster-recovery/disaster-recovery-solutions-top-5-types-and-how-to-choose/
https://itsec.group/blog-post-responding-to-cyberattack.html
https://www.orangecyberdefense.com/nl/blog/managed-detection-response/hoe-u-de-juiste-balans-vindt-tussen-preventie-detectie-en-response
https://www.juniper.net/nl/nl/research-topics/what-is-ids-ips.html
https://sps.nl/nieuws/wat-is-systeem-hardening/
https://databyte.nl/inspiratie/kennisbank/rpo-en-rto/
https://databyte.nl/diensten/draas/

### Ervaren problemen
Het goed onderscheiden tussen zo veel verschillende termen, maar de meer je over leest des beter ik het zag wat ik moets doen. Ik zag dat ik het voor mijzelf niet te moeilijke moest makken.

### Resultaat
Het kunnen begrijpen over begrippen voor het cyberaanval en het analyseren van de RTO en RPO.