# Passwords
Beveiliging van de wachtwoorden

## Key-terms

### Hasing  
Is een wiskundige functie die inputgegevens van variabele grootte omzet in een vaste grootte van uitvoergegevens. Het idee is om de gegevens te versleuten met behulp van het hasing-algoritme, zodat het niet mogelijke is om de oorspronkelijke gegevens terug te krijgen. Alleen om te controleren of deze overeenkomen met een eerder opgeslagen hashwaarde.

### Rainbow Table  
Het zijn tabellen met wachtwoorden en hun gehashte waarde. Als je dus  een hash waarde hebt kan je kijken bij welke wachtwoord erbij hoort. Vaak zijn ze beperkte tot 8 tekens, dus als je wachtwoord langer is dan 8 tekens is het meteen een stuk veiliger. Het is een feite een vorm van een woordenboekaanval

### MD5  
Het staat voor Message Digest Algoritmh 5 en is een cryptografische hashfunctie ontworpen in 1991. Met deze functie kan je een gegeven waarde veranderen in een andere waarde die uit 32 letters en cijfers bestaat, die niet meer terug valt te veranderen.

### SHA1  
Het staat voor Secure Hash Algoirthm 1 is veel betere manier vergelijken met MD5. Het gebruikt andere formula waardoor het uit 40 letters en cijfers bestaat.

### Salted  
Een waarde zoals “dn55as3dv(#83220” wordt achter je wachtwoord geplakt  en daarna pas door een hashfunctie zoals MD5, hierdoor wordt je wachtwoord een stuk langer. Maar als elke gebruiker de zelfde salt gebruikt kan de hacker na twee wachtwoorden het kraken. Om dat weer tegen te gaan gebruikt sommige websites voor iedere gebruiker een eigen salt.



## Opdracht

### Find out what hashing is and why it is preferred over symmetric encryption for storing passwords.
Omdat symmetirc encryption is echt bedoel voor het sleuten en het onsleuten van gegevens. Bij Hashing is het een niet-omkeerbaar en dat betekend dat het niet mogelijke is om je oorsponkelijke gegevens te verkrijgen.

### Find out how a Rainbow Table can be used to crack hashed passwords. 
Omdat het een vorm van een woordenboekaanval is, waarbij je een grote database met voorgedefinieerde hashwaarden hebt. Hierdoor kan je snel de oorspronkeijke wachtwoorden vinden die overeenkomen met de gehaste waarden. De korter het is des sneller het wordt geraden.

**Tekst**
```
Zelfde
```

**MD5**
```
95e7674f843d1135c63181523d07721f
```

### Below are two MD5 password hashes. One is a weak password, the other is a string of 16 randomly generated characters. Try to look up both hashes in a Rainbow Table.

**MD5 Password hashes**
```
03F6D7D1D9AAE7160C05F71CE485AD31
03D086C9B98F90D628F2D1BD84CFA6CA
```

**De resultaat**
![resultaat](/00_includes/SEC-07-resultaat.png "resultaat")

Deze werd exact match als MD5
```
03F6D7D1D9AAE7160C05F71CE485AD31
```

Deze werd het niet gevonden
```
03D086C9B98F90D628F2D1BD84CFA6CA
```

### Create a new user in Linux with the password 12345. Look up the hash in a Rainbow Table.

**Nieuwe gebruiker maken**
```
sudo adduser tgusereasypassword
12345
```

**MD5 Hash**
```
827ccb0eea8a706c4c34a16891f84e7b
```

**SHA1 Hash**
```
8cb2237d0679ca88db6464eac60da96345513964
```

**Hash zoeken**  
De hash kun je vinden met
```
cat /etc/shadow
```

**Output**
![resultaat](/00_includes/SEC-07-resultaat2.png "resultaat")

```
tgusereasypassword:$6$YCIlvXLWjSyOFWIK$c2JNsxzmV7D93WogL2kSy3L05syLn6mEvB4D19tg1NspZGKSTJgEqJM8GUwWK.i7iOLh.b38JDwjG4SIyHVgn0:19467:0:99999:7:::
```


**Gebruikersnaam**
```
tgusereasypassword
```

**De Hash Methode (SHA-512)** 
```
$6
```

**Salted**
```
$YCIlvXLWjSyOFWIK
```

**SHA-512**
```
$c2JNsxzmV7D93WogL2kSy3L05syLn6mEvB4D19tg1NspZGKSTJgEqJM8GUwWK.i7iOLh.b38JDwjG4SIyHVgn0
```

**Aantal dagen sinds 1 Jan 1970**
```
19467
```


**Minimaal dagen voordat je wachtwoord weer kan veranderen / 0 = uit**
```
0
```

**Maximaal dagen hoe lang je wachtwoord geldig is**
```
99999
```

**Aantal dagen voordat je waarschuwing krijgt om het te veranderen**
```
7
```

De laaste twee (Inactief en Verlopen) zijn leeg.

**Rainbow Table**  
![resultaat](/00_includes/SEC-07-resultaat3.png "resultaat")
Kan niet want alle wachtwoorden bestaat samen uit verschillende salten met verschillende sha-512. Dit betekend dat het gewoon onmogelijke is om het te cracken met zoveel mogelijkeheden.  Ik zou een Rainbow Table moeten maken met alle hash op die specifieke salt.

### Despite the bad password, and the fact that Linux uses common hashing algorithms, you won’t get a match in the Rainbow Table. This is because the password is salted. To understand how salting works, find a peer who has the same password in /etc/shadow, and compare hashes.

**Vergelijken**

**Mij**
```
c2JNsxzmV7D93WogL2kSy3L05syLn6mEvB4D19tg1NspZGKSTJgEqJM8GUwWK.i7iOLh.b38JDwjG4SIyHVgn0
```

**Quincy**
```

```

**Roan**
```

```

**Jon**
```

```

Omdat ze andere salt hebben krijgen we ook andere SHA-512 hash outputs. 


### Gebruikte bronnen  
https://crackstation.net/
https://medium.com/geekculture/hashed-passwords-rainbow-tables-and-salted-hashes-simply-explained-1736d431af78
https://cybr.com/certifications-archives/hash-tables-rainbow-table-attacks-and-salts/
https://www.timdehoog.nl/2011/11/26/wachtwoorden-md5-sha1-salt-hash-en-rainbow-tables/
https://www.techtarget.com/whatis/definition/rainbow-table
https://www.youtube.com/watch?v=irQlWaH0LPQ
https://www.cyberciti.biz/faq/understanding-etcshadow-file/
https://www.drchaos.com/post/understanding-rainbow-tables
https://security.stackexchange.com/questions/233695/why-people-say-that-salt-helps-to-prevent-rainbow-table-attack

### Ervaren problemen
Geen

### Resultaat
Het verschillen kennen en hoe Rainbow Table werkt.
