# AWS-02 AWS Pricing
Hoe de prijzen structure van AWS werkt.

## Key-terms

### The four advantages of the AWS pricing model  
- Pay-as-you-go
  Het makkelijke aanpassen aan veranderende (bedrijfs)behoeften zonder te grote budgetten vaste te leggen zodat het niet een prognoses is. Het verkleind de risco op overprovisioning of ontbrekende capacaiteit.
  
- Save when you commit
  Een flexibel prijsmodel dat aanzienlijke besparingen op uw AWS-gebruik oplevert. Het zijn spaarplannen die besparingen bieden ten opzichte van On-Demand. Die wordt bereken per uur voor een AWS-service. Door te aanmelden voor een service met een termijn van 1 of 3 jaar. De plannen worden eenvoudig beheerd door AWS Cost Explorer met de volgende functies: 
  1) Aanbevelingen
  2) Prestatierapportage 
  3) Budgetwaarschuwingen
  
- Pay less by using more
  Kortingen krijgen per opslagen data GB op basis hoeveel volume je in total hebt gebruikt.
![resultaat](/00_includes/AWS-02-resultaat.png "resultaat")

- Benefit from massive economies of scale
  Een lagere variabele kosten krijgen omdat het AWS grotere schaalvoordelen behaalt des meer gebruikers worden gebruikt.
  
### AWS free tier for
- **S3:**  
  **S**imple **S**torage **S**ervice is een oplslagservice voor objecten in de cloud. Het biedt oneperkte opslagruimte en is ontworpen om te integreren met andere AWS-services zoals EC2.
  
- **EC2:**  
  **E**lastic **C**ompute **C**loud is een web service die een schaalbare cloud computing-capaciteit biedt. Het geeft de gebruikers de mogelijkeheid om virtuele machines te huren ook bekend als 'instances' om hun applicaties en diensten te draain. Het is een flexibele oplossing voor het lanceren van een nieuwe instances waarbij ze de grootte en capaciteit af kunnen stemmen op hun behoeftes.
  
- **Always free services:**  
  Dat zijn de extra services die AWS biedt die altijd gratis zullen zijn zolang ze niet over de limit gaan. 
  

### Total Cost of Ownership (TCO)  
Het wordt gebruikt voor het meten hoeveel een infrastructuur zou kosten als de tradionele manier wordt gehost. Hiervoor wordt de CapEx gebruikt.

### CapEx (CAPital EXpenses / Investeringen)  
Een investeringsuitgaven in een vaste activa als gevolg van vervanging en/of uitbreiding. Het zijn eenmalige uitgaven.

### OpEx (OPerational EXpenses / Bedrijfskosten)  
Een uitgaven die het gevolg zijn van het exploiteren van eerder aangeschafte kapitaalgoederen. Het zijn terugkerende uitgaven.


## Opdracht  

### Create an alert that you can use to monitor your own cloud costs.  

Je gaat naar 'My Account' > 'Billing & Cost Management'
![resultaat](/00_includes/AWS-02-resultaat2.png "resultaat")

Op de dashboard ga naar je 'Budgets' > 'Create a budget'
![resultaat](/00_includes/AWS-02-resultaat3.png "resultaat")

In onze geval kunnen we zeggen dat we op 'Zero spend budget' moeten blijven. Verder vullen we de naam voor onze budget in en email adress(max 10) wie allemaal de alert krijgt. Nadat alles is goed ingevuld druk je op 'Create Budget'.
![resultaat](/00_includes/AWS-02-resultaat4.png "resultaat")

Nu als je op begin naar 'Budgets' gaat zie je nu een andere scherm. Dit keer gaat het direct naar de 'Overview' met jouw aangemaakt budget.   
![resultaat](/00_includes/AWS-02-resultaat5.png "resultaat")

We kunnen nu meer informatie zien wanneer op onze budget naam drukken. Onderaan kan je op 'Alerts' drukken en daar zie je een kort info erover. Je kan meer info krijgen voor elke alert wanneer je de naam klikt in onze geval is het 'Actual cost > $0.01' 
![resultaat](/00_includes/AWS-02-resultaat5a.png "resultaat")

Hier zie je de volledige informatie over onze alert die je dan uit kan lezen. Verder is geen 'Action' of terwijl 'Actie Ondernemen' wanneer wij boven de limit zijn, alleen een 'Alert' of terwijl 'Waarschuwing' door een email te versturen naar mij.
![resultaat](/00_includes/AWS-02-resultaat5b.png "resultaat")

Dus onthoud dit is een alleen nog 'Waarschuwing' en je dient snel eigen actie te ondernemen. Lastiger als je de enige bent en het tijdens je slaap uren zou gebeuren en pas volgende morgen er achter komt dat iemand iets duur heeft aangezet. Je zou het ook automatische kunnen instellen dat het niet boven de budget gaat tenzij met jouw toestemming.

### Understand the options that AWS offers to get insights in your cloud costs.  

Voor de bovenstaand genoemde 'Budgets' kunnen we meerdere opties selecteren en dit zijn ze als volgt:

- Use a template (simplified) 
	- Zero spend budget
	- Monthly cost budget
	- Daily Saving Plans coverage budget
	- Daily Reservation Utilzation budget

- Customize (advanced)
	- Cost budget - Recommended
	- Usage budget
	- Savigns Plans budget
	- Reservation budget

Zoals je merkt heb je bij elke dan 4 (vergelijkebare) verschillende opties. Dit hangt af hoe simple je budget in te plannen is. De keuzes zou zijn dat bij vasten kosten je 'Template' kiest en bij variable kosten of 'Usage budget' voor AWS services zoals S3 of EC2 je 'Customize' kiest. 

### Gebruikte bronnen
https://aws.amazon.com/pricing/?aws-products-pricing.sort-by=item.additionalFields.productNameLowercase&aws-products-pricing.sort-order=asc&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all
https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html
https://www.marcelmartens.nl/post/zijn-clouddiensten-opex-of-capex
https://cmweb.nl/2022/11/wat-zijn-capex-en-opex/
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html
https://aws.amazon.com/free/free-tier-faqs/

### Ervaren problemen
Goed door zoeken waar die opties staan maar in dit geval is het gewoon in 'My Account' opties doorlezen om het te kunnen vinden inplaats afgeleid te zijn met de documantie lezen afgelopen middag. 

### Resultaat
De nieuwe termen kennen van AWS prijzen system en wat de voordelen zijn. Daarbij hoe je een alerm zet voor je 'Budget' met daarbij de verschillende opties. 