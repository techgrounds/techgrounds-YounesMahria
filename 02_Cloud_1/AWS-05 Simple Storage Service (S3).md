# AWS-05 Simple Storage Service (S3)
Weten hoe S3/Simple Storage Service werkt.

## Key-terms

### S3 / Simple Storage Service  
Is een object gebaseerde opslag in een S3, dit wilt zeggen dat alle bestanden ongeacht van formaat (exe, jpeg, png) als objecten worden opgeslagen in een Bucket container. De namen voor de Buckets moeten globaal uniek blijven, maar dit telt ook mee wat de andere AWS accounts hebben. Er worden automatische tenmiste 3 duplicaties gemaakt voor elke objecten in de regio. Het is dus kosteneffectief en heeft gebruiksvriendelijke beheerfuncties:
1) Kosten Optimaliseren
2) Gegevens organiseren
3) Toegangscontroles configureren voor specifieke zakelijke,  organisatorische en nalevingsvereisten.
![resultaat](/00_includes/AWS-05-resultaat.png "resultaat")

### There are 4 storage classes:
Er worden 4 categorieën genoemd voor de storage classen met korte definitie ervan.

1) **S3 Standard / General purpose** 
	1) **S3 Standard** for frequently accessed data.  
	2) **S3 Standard-Infrequent Access (S3 Standard-IA)** for less frequently accessed data.  
	   
2) **S3 Intelligent-Tiering / Unknown or changing access**  
	1) **S3 Intelligent-Tiering** for automatic cost savings for data with unknown or changing access patterns. 
	   
3) **S3 One Zone / Infrequent access**  
	1) **S3 One Zone-Infrequent Access (S3 One Zone-IA)** for less frequently accessed data. 
	   
4) **S3 Glacier / Archive**  
	1) **S3 Glacier Instant Retrieval** for archive data that needs immediate access.
	2) **S3 Glacier Flexible Retrieval (formerly S3 Glacier)** for archive data that needs immediate access.
	3) **S3 Glacier Deep Archive (S3 Glacier Deep Archive)** for long-term archive and digital preservation with retrieval in hours at the lowest cost storage in the cloud.     

### **S3 Outposts** 
if you have data residency requirements that can’t be met by an existing AWS Region.


## Opdracht  

Voordat we beginnen moeten we eerste nog onze AWS Free Tier activeren. We gaan nu account maken ervoor door op 'Create a Free Account' te drukken.
![resultaat](/00_includes/AWS-05-resultaat3.png "resultaat")

We beginnen op https://aws.amazon.com/s3/
![resultaat](/00_includes/AWS-05-resultaat2.png "resultaat")

### Exercise 1:
- Create new S3 bucket with the following requirements:  

#### 1) Region: Frankfurt (eu-central-1) 
Om het te veranderen moet je rechts boven gaan op de huidige region klikken (staat naast je eigen naam) en dan 'Europe (Frankfurt)eu-central-1' selecteren.
![resultaat](/00_includes/AWS-05-resultaat4.png "resultaat")

We moeten eerste een bucket gaan aanmaken. We kunnen links boven ernaar zoeken. In dit geval is het 'S3'
![resultaat](/00_includes/AWS-05-resultaat5.png "resultaat")

Daarna kun je op 'Create bucket' drukken
![resultaat](/00_includes/AWS-05-resultaat6.png "resultaat")

Hier moet je de uniek naam geven voor je Bucket. ``younestechgrounds25april``
AWS region
``EU (Frankfurt) eu-central-1``

![resultaat](/00_includes/AWS-05-resultaat7.png "resultaat")
Nadat alles is ingevuld druk je op 'Create bucket'

#### 2) Upload a cat picture to your bucket.    
Selecteer de net aangemaakte bucket.
![resultaat](/00_includes/AWS-05-resultaat8.png "resultaat")

Onthoud dat bestanden allemaal als objecten worden behandeld dus.

Bij 'Objects > Upload'
![resultaat](/00_includes/AWS-05-resultaat9.png "resultaat")

Nu ga je het toevoegen bij 'Add files' en het bestand selecteren die opgeslagen staat in je eigen apparaat. Daarna op 'Upload'
![resultaat](/00_includes/AWS-05-resultaat10.png "resultaat")
*Bij 'Permissions' kan je ook het gelijke veranderen voor het toegang tot bepaalde 'Objecten URL'*

#### 3) Share the object URL of your cat picture with a peer. Make sure they are able to see the picture.  

Dit was de link (die niet meer werkt). 
https://younestechgrounds25april.s3.eu-central-1.amazonaws.com/screenshot-s3.png 

Maar....
![resultaat](/00_includes/AWS-05-resultaat11.png "resultaat")
Access Denied!

Er zijn twee oplossingen ervoor.

##### 1 - Presigned URL
Je kan tijdelijke toegang geven met 'Presigned URL' om deze te kunnen delen met andere peers. Je krijgt dan wel een extra lange URL erachert die als token key is. 'Object URL + token key'   

Objects actions > Share with a presigned URL
![resultaat](/00_includes/AWS-05-resultaat12.png "resultaat")

Vul de minuten of uren in en dan op 'Create presigned URL'
![resultaat](/00_includes/AWS-05-resultaat13.png "resultaat")

Als laaste druk je op 'Copy presigned URL'
![resultaat](/00_includes/AWS-05-resultaat14.png "resultaat")

#### 2 - Permissions  
Bij je **Bucket** moet je naar 'Permissions' gaan en dan op 'Edit' voor 'Block public access (bucket settings)' 
![resultaat](/00_includes/AWS-05-resultaat18.png "resultaat")

Zorg ervoor dat 'Block all public access' checkbox uitgevinkt is en dan pas op 'Save changes' drukken. 
![resultaat](/00_includes/AWS-05-resultaat19.png "resultaat")

Er komt nog een waarschuwing popup, lees goed door wat er staat en de type je het woord in en dan pas op 'Confirm' drukken. Nu kan je ook de objecten permissions veranderen.
![resultaat](/00_includes/AWS-05-resultaat20.png "resultaat")

Nadat je 'Screenshot' hebt geselecteerd, ga je naar 'Permissions > Edit'.
![resultaat](/00_includes/AWS-05-resultaat15.png "resultaat")

Zorg ervoor dat 'Read' is geselecteerd en dat je akkoord gaat ermee en dan op 'Save changes'.
![resultaat](/00_includes/AWS-05-resultaat16.png "resultaat")

Nu kan je 'Object URL' delen met andere peers zonder tijd limit.

### Exercise 2:  
- Create new bucket with the following requirements:  
#### 1) Region: Frankfurt (eu-central-1)  
**Een herhaling van Excercise 1:**

Om het te veranderen moet je rechts boven gaan op de huidige region klikken (staat naast je eigen naam) en dan 'Europe (Frankfurt)eu-central-1' selecteren.
![resultaat](/00_includes/AWS-05-resultaat4.png "resultaat")

We moeten eerste een bucket gaan aanmaken. We kunnen links boven ernaar zoeken. In dit geval is het 'S3'
![resultaat](/00_includes/AWS-05-resultaat5.png "resultaat")

Daarna kun je op 'Create bucket' drukken
![resultaat](/00_includes/AWS-05-resultaat6.png "resultaat")

Hier moet je de uniek naam geven voor je Bucket. ``younestechgrounds25april``
AWS region
``EU (Frankfurt) eu-central-1``

![resultaat](/00_includes/AWS-05-resultaat7.png "resultaat")
Nadat alles is ingevuld druk je op 'Create bucket'


#### 2) Upload the four files that make up AWS’ demo website. 
**Een gedeeltelijke herhaling van Excercise 1:**
 
Selecteer de net aangemaakte bucket.
![resultaat](/00_includes/AWS-05-resultaat8.png "resultaat")

Onthoud dat bestanden allemaal als objecten worden behandeld dus.

Bij 'Objects > Upload'
![resultaat](/00_includes/AWS-05-resultaat9.png "resultaat")

Nu ga je het toevoegen bij 'Add files' en het bestand selecteren die opgeslagen staat in je eigen apparaat. Daarna op 'Upload'
![resultaat](/00_includes/AWS-05-resultaat17.png "resultaat")
*Bij 'Permissions' kan je ook het gelijke veranderen voor het toegang tot bepaalde 'Objecten URL'*

#### 3) Enable static website hosting.  
Bij je bucket ga je naar de 'Propoties' en helemaal naar beneden scrollen.
![resultaat](/00_includes/AWS-05-resultaat23.png "resultaat")

Je ziet 'Static website hosting' staan en vervolgens druk je op 'Edit'
![resultaat](/00_includes/AWS-05-resultaat24.png "resultaat")

Bij 'Static website hosting' is het 'Enable'
Bij 'Hosting type' is het 'Host a static website'
Bij 'Index document' is het  'index.html'
Bij 'Error document - optional' is het 'error.html'
Daarna kan je op 'Save changes' drukken.
![resultaat](/00_includes/AWS-05-resultaat25.png "resultaat")

#### 4) Share the bucket website endpoint with a peer. Make sure they are able to see the website.  

Er zijn twee manieren om dat te kunnen doen.

#### 1 - Bucket Policy
Bij bucket moet je naar 'Permissions' gaan, zorg erover dat je 'Block public access (bucket settings)' uit staat als dat niet geval is. Dan bij 'Bucket Policy' kan je op 'Edit' drukken. 
![resultaat](/00_includes/AWS-05-resultaat26.png "resultaat")

Om achter te halen welke JSON code je nodig hebt kun je naar 'Policy explames' gaan om uitleg daarover te krijgen. In dit geval stond er duidelijke 'Setting permissions for website access' waarbij je de code ervoor krijgt. Alleen de bucket namen veranderen naar 'younestechgrounds25april' 

![resultaat](/00_includes/AWS-05-resultaat27.png "resultaat")

De JSON code hieronder is wat je toevoegt en dan vervolgens op 'Save changes' drukken.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::younestechgrounds25april/*"
        }
    ]
}
```

Nu kan ik de URL delen met mij peers. 
```
http://younestechgrounds25april.s3-website.eu-central-1.amazonaws.com/
```
*LET OP: De URL werkt niet meer omdat de bucket verwijderd is.*

#### 2 - Object - Public Access
Op je bucket kan je alles selecteren en naar 'Actions > Make public using ACL' zodat alle 4 files toegangelijke zijn.
![resultaat](/00_includes/AWS-05-resultaat21.png "resultaat")

Bovenaan krijg je weer een waarschuwing ervoor, als je op 'Make public' drukt, gaat alle 'Object URL' werken.
![resultaat](/00_includes/AWS-05-resultaat22.png "resultaat")

Nu kan ik de URL delen met mij peers. 
```
http://younestechgrounds25april.s3-website.eu-central-1.amazonaws.com/
```
*LET OP: De URL werkt niet meer omdat de bucket verwijderd is.*



### Gebruikte bronnen
https://aws.amazon.com/s3/
https://aws.amazon.com/s3/storage-classes/
https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteAccessPermissionsReqd.html

### Ervaren problemen
Wel altijd een alternative oplossing sneller kunnen vinden dan wat er gevraagd wordt, maar dan als nog 2 oplossingen kunnen vinden. Verder gemerkt dat ik veel screenshots heb gemaakt maar stapgewijst en laten zien wat ik deed is als nog beter.

### Resultaat
Het kunnen aanmaken van S3 Bucket, toegang geven voor Object URL zowel tijdelijke als altijd en toegang geven aan static websites met Bucket policy of alle files publieke toegang geven.
