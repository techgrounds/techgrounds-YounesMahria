## Inleiding:

Deze beslissingsdocumentatie beschrijft de genomen beslissingen met betrekking tot de infrastructuurvereisten voor het AWS-project. Het doel is om de infrastructuur op een gestructureerde en geautomatiseerde manier op te zetten, waarbij wordt voldaan aan de vereisten voor beveiliging, schaalbaarheid en beheerbaarheid.

## Probleemstelling:

Het project vereist een robuuste en beveiligde infrastructuur op basis van Infrastructure as Code-principes om de AWS-resources te beheren en te configureren. De belangrijkste uitdagingen zijn het beveiligen van VM-disks, het implementeren van dagelijkse back-ups en het geautomatiseerd installeren van de webserver.

## Opties voor de eisen:

Van de 9 genoemde eisen worden ze in 6 categorieën geplaats namelijk:

1. Beveiliging
	1. Alle VM disks moeten encrypted zijn.
	2. Firewall voor subnets
	3. SSH of RDP verbindingen met de webserver mogen alleen tot stand komen vanuit de admin server.
2. Backups
	1. De webserver moet dagelijks gebackupt worden.
	2. De backups moeten 7 dagen behouden worden.
3. Automatiseren
	1. De webserver moet op een geautomatiseerde manier geïnstalleerd worden.
4. Bereikbaarheid
	1. De admin/management server moet bereikbaar zijn met een publiek IP.
	2. De admin/management server moet alleen bereikbaar zijn van vertrouwde locaties (office/admin’s thuis).
5. IP ranges
	1. De volgende IP ranges worden gebruikt: 10.10.10.0/24 & 10.20.20.0/24
6. Ontwerp
	1. Wees niet bang om verbeteringen in de architectuur voor te stellen of te implementeren, maar maak wel harde keuzes, zodat je de deadline kan halen.




## Evaluatiecriteria:

De volgende criteria worden gebruikt om de opties te evalueren:

- Beveiliging: Mate van encryptie en bescherming van gegevens.
- Schaalbaarheid: Mogelijkheid om de infrastructuur gemakkelijk op te schalen.
- Beheerbaarheid: Niveau van automatisering en gemak van configuratie.




------


1. Inleiding:
- Geef een overzicht van het doel van de beslissingsdocumentatie en de context van het project of de situatie.

2. Probleemstelling:
- Identificeer de specifieke problemen of uitdagingen die moeten worden aangepakt op basis van de voorgestelde eisen.
- Benadruk het belang van het nemen van beslissingen om aan deze eisen te voldoen.

3. Beschrijving van de opties:
- Geef een gedetailleerde beschrijving van de verschillende opties die zijn overwogen om aan de eisen te voldoen.
- Dit kunnen technologieën, services, tools of benaderingen zijn die geschikt zijn voor de vereisten.

4. Evaluatiecriteria:
- Definieer de criteria waarmee de opties worden geëvalueerd.
- Dit kunnen technische, operationele, financiële, beveiligings- of andere relevante criteria zijn.

5. Evaluatie van de opties:
- Evalueer elke optie aan de hand van de vastgestelde criteria.
- Gebruik objectieve gegevens en informatie om de prestaties van elke optie te beoordelen.
- Leg de voordelen, nadelen en implicaties van elke optie uit.

6. Genomen beslissing(en):
- Verklaar welke optie(s) zijn gekozen om aan de eisen te voldoen.
- Leg de redenen en motivering achter de genomen beslissing(en) uit.
- Verwijs naar de evaluatiecriteria en de resultaten van de evaluatie.

7. Implementatieplan:
- Beschrijf het plan om de gekozen oplossing(en) te implementeren.
- Identificeer de benodigde middelen, tijdlijnen en verantwoordelijkheden.
- Overweeg eventuele risico's en implementatiestrategieën.

8. Conclusie:
- Sluit de beslissingsdocumentatie af met een samenvatting en conclusie.
- Benadruk de gekozen oplossing(en) en de verwachte voordelen ervan.
- Moedig aanvullende vragen, opmerkingen of discussie aan.