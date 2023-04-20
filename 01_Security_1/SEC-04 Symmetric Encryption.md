# Symmetric encryption
Uitleg en werking van Sysmmetric Encryption gebruiken.

## Key-terms

### Symmetrical encryption  
Is een type codering waarbij één (geheime) sleutel wordt gebruikt om elektronische gegevens zowel te coderen als te decoderen. De sleutel moeten worden uitgewisseeld tussen de entiteiten die via deze codering communiceren zodat het gebruikt wordt voor het decoeringsproces.

### Cryptography  
Is een methode om communicatie en informatie te beschermen door middel van codes. Hierdoor kan het alleen gelezen of verwerkt worden voor diegene informatie bestemd is.

### Caesar cipher    
Is een eenvoudige methode om berichten te coderen. Het is een vervangingsmethode waarbij letters in het alfabet met een vast aantal spaties worden verschoven om een coderingsalfabet te verkrijgen. Dus een verschuiving van 1 codeert een A als een B, B als een C enz.

## Opdracht


### Find one more historic cipher besides the Caesar cipher.

* **Enigma Code**  
Deze codeerapparaat werd door de Duitse troepen gebruikt tijdens WO II om hun uitzendingen te coderen.

### Find two digital ciphers that are being used today. 
* **Symmetric key encryption**  
Gebruikt een enkele sleutel om de gegevens zowel te versleutelen als te ontsleutelen. Het maakt bediening eenvoudiger en zorgt ervoor dat gegevens zeer snel kunnen worden versleuteld en ontsleuteld. Het is wel abosluut noodzakelijke dat de sleutel zelf veilig wordt bewaard.

* **Asymmetric key encryption**  
Het bestaat uit twee complementaire delen, namelijke **Openbare sleutel**kan door idereen worden gebruikt om een versleutelde berichten te coderen. **Privésleutel** is in staat om de berichten te decoderen en te lezen. Het wordt vaak gebruikt bij het versleutelen van gegevens en voor digitale handtekeningen.

* **Hybrid Encryption**
Het is een combinatie van symmetric (voor de snelheid en gemak) en asysmmetric (effectiviteit) key encryption voor het coderen en decoderen. 

* **Hasing**  
Het proces van het omzetten van gegevens van willekeurige grootte in een unieke vaste grootte. Een veelgebruikte techniek in de informatietechnologie met name in beveiligingsgerelateerde toespassingen.


### Send a symmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key you share with them. Try to think of a way to share this encryption key without revealing it to everyone. You are not allowed to use any private messages or other communication channels besides the public Slack channel. Analyse the shortcomings of symmetric encryption for sending messages.

Je kan het heel lastig maken voor de team en de rest van medestudent. Om eracher te komen wat heb ik gedaan zonder dat verklappen maakt het moelijke om het te ontcijferen. Hoe dan ook als een van mij team het kraakt dan zouden andere het ook kunnen doen. Dit heeft meer te makken met, als het makkelijk is dan kan iedereen het maar als het moelijke is dan weet niemand het of niet iedereen van mij teamleden.

![resultaat](/00_includes/SEC-04-resultaat.png "resultaat")

**Encrypted Text (Github)**
```
G8sNA+z6SKoX2vSqYIgl+Na7T3eNmBuhvL0rlBg71DI=           
```

**Secrety Key (Github)**
```
0f6c9baadcc122716d03cbdf9f3e7491
```

of

**Encrypted Text (Slack)**
```
G8sNA+z6SKoX2vSqYIgl+Na7T3eNmBuhvL0rlBg71DI=           
```
*Was vergeten dat slack file ging verandere dus die krijgt een andere En*


**Secrety Key (Slack)**
```
0f6c9baadcc122716d03cbdf9f3e7491
```
*Dus dan heb je een andere Secret key ook*


**Output**
```
Succes! Je zag weet ik deed :)
```

**Resultaat van Quincy**  
![resultaat](/00_includes/SEC-04-resultaat3.png "resultaat")



## Team 3 - Week 2

### Quincy  
**Encrypted Text**
```
IAvqsOk8eDSM3/D/Sxu2BGpVCPs+F8MIIz0zl8FxfIcAH+tG3uZ7aqoKQpSvkf/LKIhlqh/x/vlR4RYQUrtN7lWyqd1MYVJrgmq17ngT8RhiUhlllSNLFr+f+k1BB1a1dr7bdlPJw5C9eQw91o9szVJoV5KRypwBzLbUHznuV+s=
```

![resultaat](/00_includes/SEC-04-resultaat2.png "resultaat")
**Alt text**
```
Dhhyvt ullt ql kl tvlpal vt kpa kl lujyfwalu. Ola ollma avjo olslthhs nllu avlnlcvlnkl dhhykl? Vm nh ql avjo ql apqk clyzwpsslu?. Hjo ub ql avjo oply ilua. Kl whzzwoyhzl pz uplagvzwljphhsol 7Shift
```

**Output**
```
Waarom neem je de moeite om dit de encrypten. Het heeft toch helemaal geen toegevoegde waarde? Of ga je toch je tijd verspillen?. Ach nu je toch hier bent. De passphrase is nietzospeciaalhe 7Labym
```

**Secrety Key**
```
nietzospeciaalhe
```

**Output**
```
Wow je hebt echt de moeite genomen om dit de decrypten. ik vind dat je nu toegang mag hebben tot mijn vrienden lijst.
```
![resultaat](/00_includes/SEC-04-resultaat4.png "resultaat")


### Roan  
**Encrypted Text**
```
479LoYIFrikwp3HwX7P3uuSoqiQkfGHUjqhvdcnJBQI=
```

**Secrety Key**
```
secretpassword01
```

**Output**
```
Security through obscurity.
```
![resultaat](/00_includes/SEC-04-resultaat5.png "resultaat")


### Jon  
**Encrypted Text**
```
bMqDO7kRwNPkyBNpcNV15pQWwC7oNQ5NGkZFo7r5yi4=
```

**Secrety Key**
```
TAKEAREGULARPAWS
```

**Output**
```
Purrrfect decryption !!
```
![resultaat](/00_includes/SEC-04-resultaat6.png "resultaat")

### Gebruikte bronnen
https://www.cryptomathic.com/news-events/blog/symmetric-key-encryption-why-where-and-how-its-used-in-banking
https://www.techtarget.com/searchsecurity/definition/cryptography
https://brilliant.org/wiki/caesar-cipher/
https://interestingengineering.com/innovation/11-cryptographic-methods-that-marked-history-from-the-caesar-cipher-to-enigma-code-and-beyond
https://www.insightsforprofessionals.com/it/security/types-of-encryption-protect-your-data
https://www.techopedia.com/definition/1779/hybrid-encryption
https://www.devglan.com/online-tools/aes-encryption-decryption

### Ervaren problemen
Het kunnen vinden van een manier om de sleutel door te geven zonder dat andere erachter komen. De vraag voelde als een strikvraag waarbij het onmogelijke is en dat was de bedoeling. Je kan het goed verstoppen als je wilt, maar wanneer ze erachter komen waar het verstopt is kunnen ze binnen komen. De volgende opdracht was uit eindelijke de oplossing voor het probleem.

### Resultaat
De verstopt sleutels van teamngenoten en andere kunnen vinden en het ontcijferen ervan. Het weten van verschillende methodes.
