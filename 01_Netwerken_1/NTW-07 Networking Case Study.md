# Networking case study
Een network diagram maken

## Key-terms

### Active Directory
is een hiërarchische structuur waarin informatie over objecten op het netwerk wordt opgeslagen. Het slaat bijvoorbeeld gebruikersaccounts en geeft andere geautoriseerde gebruikers op het zelfde netwerk toegang tot deze informatie met Active Directory Domain Services (AD DS).


### Azure Active Directory
is een cloud identiteits- en toegangsbeheerserice. Het geeft toegang tot externe resources, zoals Microsoft 365, Azure Portal en duizenden andere SaaS-toepassingen.


## Opdracht

### In this case study you take the role of a network administrator setting up a network in the new office of a small e-commerce company. Of course there are multiple ways to go about this problem, but this company has specifically said that network security is extremely important to them.
* The office contains the following devices:
* A web server where our webshop is hosted
* A database with login credentials for users on the webshop
* 5 workstations for the office workers
* A printer
* An AD server
* A file server containing internal documents

As a network administrator you get to choose which networking devices get used.

#### Design a network architecture for the above use case.
![resultaat](/00_includes/NTW-07-resultaat.png "resultaat")

#### Explain your design decisions
* De Web Server is een webshop voor de klanten waarbij het een Publieke IP krijgt. Die is verbonden met het Database met zijn eigen Publieke IP Adress om de gegevens van klanten te kunnen lezen. Het is direct verbonden met het Router die dan naar het Firewall gaat voordat het internet is bereikt of andersoms voor in komende paketten.
* De Active Directory Server is verbonden met Switch daar wordt gekeken naar de geautoseeride toegang.
* De 5 Workstations zijn verbonden met het switch, die hebben toegang naar de File Server en de Printer.
* De File Server verstuurt data naar de Printer om documenten te kunnen printen.
* De Firewall heeft security policies voor welke verbinden er wel en niet er doorheen mogen.

### Na de [Beer:30 - Network Architecture Review](https://www.youtube.com/@SecureState)
![resultaat](/00_includes/NTW-07-resultaat2.png "resultaat")
* De 5 Workstations en 1 Printer worden apart verbonden met 1 switch die naar de Internal Router gaat. 
* De 1 File Server word verbonden met 1 switch en die naar de Internal Router gaat. 
* De Internal Router met Nat-gateway ingebouw gaat naar de Firewall en die gaat naar het Internet uiteindelijke
* De Database gaat eerste door een AD Server en dan pas Web Server.
* De Web Server gaat direct naar de Firewall voordat het na de internet gaat.

### Gebruikte bronnen
https://learn.microsoft.com/nl-nl/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview
https://learn.microsoft.com/nl-nl/azure/active-directory/fundamentals/active-directory-whatis


### Ervaren problemen
Er waren veel mogelijkeheden om het te kunnen maken en soms tewijfel je of het op deze manier hoort. Ik heb het gehouden om een structuur te focussen en niet te mogelijke erover nadenken. 

Na de video te hebben bekeken zag ik hoe het anders moet en hoe dichtbij in de buurt zat.

### Resultaat
Een scheme kunnen maken gebaseerd van de wensen en het kunnen inzien de andere mogelijkeheid die beter werkt.