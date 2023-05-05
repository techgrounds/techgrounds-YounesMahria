# Well Architected Framework
Beschrijving wat een Well Architected Framework (WAF)

## Key-terms / Opdracht

### The Well Architected Framework (WAF)
---- 
----
### ENG
-----
#### AWS Well-Architected
>AWS Well-Architected helps cloud architects build secure, high-performing, resilient, and efficient infrastructure for a variety of applications and workloads. Built around six pillars—operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability—AWS Well-Architected provides a consistent approach for customers and partners to evaluate architectures and implement scalable designs.  

> The AWS Well-Architected Framework includes domain-specific lenses, [hands-on labs](https://www.wellarchitectedlabs.com/), and the AWS Well-Architected Tool. The [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no cost in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected/), provides a mechanism for regularly evaluating workloads, identifying high-risk issues, and recording improvements.

>The AWS Well-Architected Framework describes key concepts, design principles, and architectural best practices for designing and running workloads in the cloud. By answering a few foundational questions, learn how well your architecture aligns with cloud best practices and gain guidance for making improvements.

#### Framework Overview

The AWS Well-Architected Framework describes key concepts, design principles, and architectural best practices for designing and running workloads in the cloud. By answering a few foundational questions, learn how well your architecture aligns with cloud best practices and gain guidance for making improvements.

#### CROPSS  (Six Pillars) - Info (Kort)
1) ***C*ost optimization pillar**  
    The cost optimization pillar focuses on avoiding unnecessary costs. Key topics include understanding spending over time and controlling fund allocation, selecting resources of the right type and quantity, and scaling to meet business needs without overspending.
      
2) ***R*eliability pillar**  
    The reliability pillar focuses on workloads performing their intended functions and how to recover quickly from failure to meet demands. Key topics include distributed system design, recovery planning, and adapting to changing requirements.
   
3) ***O*perational Excellence pillar**  
    The operational excellence pillar focuses on running and monitoring systems, and continually improving processes and procedures. Key topics include automating changes, responding to events, and defining standards to manage daily operations.
   
4) ***P*erformance efficiency pillar**  
    The performance efficiency pillar focuses on structured and streamlined allocation of IT and computing resources. Key topics include selecting resource types and sizes optimized for workload requirements, monitoring performance, and maintaining efficiency as business needs evolve.
   
5) ***S*ecurity pillar**  
    The security pillar focuses on protecting information and systems. Key topics include confidentiality and integrity of data, managing user permissions, and establishing controls to detect security events.
   
6) ***S*ustainability pillar**  
    The sustainability pillar focuses on minimizing the environmental impacts of running cloud workloads. Key topics include a shared responsibility model for sustainability, understanding impact, and maximizing utilization to minimize required resources and reduce downstream impacts.


#### CROPSS  (Six Pillars) - Info (Deep)
The 'White Paper' information of Six Pillars.
1) ***C*ost optimization pillar**  
	1) ***Cost optimization***  
	    Cost optimization is a continual process of refinement and improvement over the span of a workload’s lifecycle. The practices in this paper help you build and operate cost-aware workloads that achieve business outcomes while minimizing costs and allowing your organization to maximize its return on investment.
	   
	2) ***Practice cloud financial management***  
	    Managing cloud finance requires evolving your existing finance processes to establish and operate with cost transparency, control, planning, and optimization for your AWS environments.
	    
	    Applying traditional, static waterfall planning, IT budgeting, and cost assessment models to dynamic cloud usage can create risks, lead to inaccurate planning, and result in less visibility. Ultimately, this results in a lost opportunity to eﬀectively optimize and control costs and realize long-term business value. To avoid these pitfalls, actively manage costs throughout the cloud journey, whether you are building applications natively in the cloud, migrating your workloads to the cloud, or expanding your adoption of cloud services.
	    
	    _Cloud Financial Management_ (CFM) allows finance, product, technology, and business organizations to manage, optimize, and plan costs as they grow their usage and scale on AWS. The primary goal of CFM is to allow customers to achieve their business outcomes in the most cost-efficient manner and accelerate economic and business value creation while finding the right balance between agility and control.
	  ![resultaat](/00_includes/AWS-12-resultaat.png "resultaat")
	   
	3) ***Expenditure and usage awareness***  
	    Understanding your organization’s costs and drivers is critical for managing your cost and usage effectively, and identifying cost-reduction opportunities. Organizations typically operate multiple workloads run by multiple teams. These teams can be in different organization units, each with its own revenue stream. The capability to attribute resource costs to the workloads, individual organization, or product owners drives efficient usage behavior and helps reduce waste. Accurate cost and usage monitoring allows you to understand how profitable organization units and products are, and allows you to make more informed decisions about where to allocate resources within your organization. Awareness of usage at all levels in the organization is key to driving change, as change in usage drives changes in cost.
	   
	4) ***Cost effective resourcess***  
	    Using the appropriate services, resources, and configurations for your workloads is key to cost savings.Consider the following when creating cost-effective resources.
	   
	5) ***Manage demand and supply resources***  
	    When you move to the cloud, you pay only for what you need. You can supply resources to match the workload demand at the time they’re needed — eliminating the need for costly and wasteful overprovisioning. You can also modify the demand using a throttle, buffer, or queue to smooth the demand and serve it with less resources.
	   
	6) ***Optimize over time***  
	    In AWS, you optimize over time by reviewing new services and implementing them in your workload. As AWS releases new services and features, it is a best practice to review your existing architectural decisions to ensure that they remain cost effective. As your requirements change, be aggressive in decommissioning resources, components, and workloads that you no longer require. Consider the following best practices to help you optimize over time.
	   
      
2) ***R*eliability pillar**  
	1) ***Reliability***  
	    The reliability pillar encompasses the ability of a workload to perform its intended function correctly and consistently when it’s expected to. This includes the ability to operate and test the workload through its total lifecycle. This paper provides in-depth, best practice guidance for implementing reliable workloads on AWS.
	   
	2) ***Foundations***  
	    Foundational requirements are those whose scope extends beyond a single workload or project. Before architecting any system, foundational requirements that influence reliability should be in place. For example, you must have sufficient network bandwidth to your data center.
	   
	3) ***Workload architecture***   
	    A reliable workload starts with upfront design decisions for both software and infrastructure. Your architecture choices will impact your workload behavior across all six Well-Architected pillars. For reliability, there are specific patterns you must follow.
	   
	4) ***Change management***   
	    A reliable workload starts with upfront design decisions for both software and infrastructure. Your architecture choices will impact your workload behavior across all six Well-Architected pillars. For reliability, there are specific patterns you must follow.
	   
	5) ***Failure management***   
	    Low-level hardware component failures are something to be dealt with every day in in an on-premises data center. In the cloud, however, you should be protected against most of these types of failures. For example, Amazon EBS volumes are placed in a specific Availability Zone where they are automatically replicated to protect you from the failure of a single component. All EBS volumes are designed for 99.999% availability. Amazon S3 objects are stored across a minimum of three Availability Zones providing 99.999999999% durability of objects over a given year. Regardless of your cloud provider, there is the potential for failures to impact your workload. Therefore, you must take steps to implement resiliency if you need your workload to be reliable.
	   
   
3) ***O*perational Excellence pillar**  
	1) ***Operational excellence***  
	    At Amazon, we define operational excellence as a commitment to build software correctly while consistently delivering a great customer experience. It contains best practices for organizing your team, designing your workload, operating it at scale, and evolving it over time. Operational excellence helps your team to focus more of their time on building new features that benefit customers, and less time on maintenance and firefighting. To build correctly, we look to best practices that result in well-running systems, a balanced workload for you and your team, and most importantly, a great customer experience.
	   
	2) ***Organization***  
	    You need to understand your organization’s priorities, your organizational structure, and how your organization supports your team members, so that they can support your business outcomes.
	   
	3) ***Prepare***  
	    To prepare for operational excellence, you have to understand your workloads and their expected behaviors. You will then be able to design them to provide insight to their status and build the procedures to support them.
	   
	4) ***Operate***  
	    Success is the achievement of business outcomes as measured by the metrics you define. By understanding the health of your workload and operations, you can identify when organizational and business outcomes may become at risk, or are at risk, and respond appropriately.
	   
	5) ***Evolve***
	    Evolution is the continuous cycle of improvement over time. Implement frequent small incremental changes based on the lessons learned from your operations activities and evaluate their success at bringing about improvement.
	   
   
4) ***P*erformance efficiency pillar**  
	1) ***Performance efficiency***  
	    The performance efficiency pillar focuses on the efficient use of computing resources to meet requirements, and how to maintain efficiency as demand changes and technologies evolve.
	   
	2) ***Selection***  
	    The optimal solution for a particular workload varies, and solutions often combine multiple approaches. Well-architected workloads use multiple solutions and allow different features to improve performance.
	    
	    AWS resources are available in many types and configurations, which makes it easier to find an approach that closely matches your needs. You can also find options that are not easily achievable with on-premises infrastructure. For example, a managed service such as Amazon DynamoDB provides a fully managed NoSQL database with single-digit millisecond latency at any scale.
	   
	3) ***Review***  
	    When architecting workloads, there are finite options that you can choose from. However, over time, new technologies and approaches become available that could improve the performance of your workload. In the cloud, it’s much easier to experiment with new features and services because your infrastructure is code.
	    1) **Infrastructure as code**
	    2) **Deployment pipeline**
	    3) **Well-defined metrics**
	    4) **Performance test automatically**
	    5) **Load generation**
	    6) **Performance visibility**
	    7) **Visualization**
	   
	4) ***Monitoring***  
	    After you implement your architecture you must monitor its performance so that you can remediate any issues before they impact your customers. Monitoring metrics should be used to raise alarms when thresholds are breached.
	    1) **Generation** – scope of monitoring, metrics, and thresholds.
	    2) **Aggregation** – creating a complete view from multiple sources.
	    3) Real-time processing and alarming – recognizing and responding.
	    4) **Storage** – data management and retention policies.
	    5) **Analytics** – dashboards, reporting, and insights
	   
	5) ***Trade-offs***
	    When you architect solutions, think about trade-offs to ensure an optimal approach. Depending on your situation, you could trade consistency, durability, and space for time or latency, to deliver higher performance.
	   
   
5) ***S*ecurity pillar**  
	1) ***Security foundations***  
	    The security pillar describes how to take advantage of cloud technologies to protect data, systems, and assets in a way that can improve your security posture. This paper provides in-depth, best-practice guidance for architecting secure workloads on AWS.
	   
	2) ***Identity and access management***  
	    To use AWS services, you must grant your users and applications access to resources in your AWS accounts. As you run more workloads on AWS, you need robust identity management and permissions in place to ensure that the right people have access to the right resources under the right conditions. AWS offers a large selection of capabilities to help you manage your human and machine identities and their permissions. The best practices for these capabilities fall into two main areas.
	   
	3) ***Detection***  
	    Detection consists of two parts: detection of unexpected or unwanted configuration changes, and the detection of unexpected behavior. The first can take place at multiple places in an application delivery lifecycle. Using infrastructure as code (for example, a CloudFormation template), you can check for unwanted configuration before a workload is deployed by implementing checks in the CI/CD pipelines or source control. Then, as you deploy a workload into non-production and production environments, you can check configuration using native AWS, open source, or AWS Partner tools. These checks can be for configuration that does not meet security principles or best practices, or for changes that were made between a tested and deployed configuration. For a running application, you can check whether the configuration has been changed in an unexpected fashion, including outside of a known deployment or automated scaling event.
	   
	4) ***Infrastructure protection***  
	    Infrastructure protection encompasses control methodologies, such as defense in depth, that are necessary to meet best practices and organizational or regulatory obligations. Use of these methodologies is critical for successful, ongoing operations in the cloud.
	    
	    Infrastructure protection is a key part of an information security program. It ensures that systems and services within your workload are protected against unintended and unauthorized access, and potential vulnerabilities. For example, you’ll define trust boundaries (for example, network and account boundaries), system security configuration and maintenance (for example, hardening, minimization and patching), operating system authentication and authorizations (for example, users, keys, and access levels), and other appropriate policy-enforcement points (for example, web application firewalls and/or API gateways).
	   
	5) ***Data protection***  
	    Before architecting any workload, foundational practices that influence security should be in place. For example, data classification provides a way to categorize data based on levels of sensitivity, and encryption protects data by way of rendering it unintelligible to unauthorized access. These methods are important because they support objectives such as preventing mishandling or complying with regulatory obligations.
	   
	6) ***Incident response***  
	    Even with mature preventive and detective controls, your organization should implement mechanisms to respond to and mitigate the potential impact of security incidents. Your preparation strongly affects the ability of your teams to operate effectively during an incident, to isolate, contain and perform forensics on issues, and to restore operations to a known good state. Putting in place the tools and access ahead of a security incident, then routinely practicing incident response through game days, helps ensure that you can recover while minimizing business disruption.
	   
	7) ***Application security***
	    Application security (AppSec) describes the overall process of how you design, build, and test the security properties of the workloads you develop. You should have appropriately trained people in your organization, understand the security properties of your build and release infrastructure, and use automation to identify security issues.
	   
   
6) ***S*ustainability pillar**  
	1) ***Cloud sustainability***  
	    The discipline of sustainability addresses the long-term environmental, economic, and societal impact of your business activities. The [United Nations World Commission on Environment and Development](https://www.un.org/en/academic-impact/sustainability) defines sustainable development as “development that meets the needs of the present without compromising the ability of future generations to meet their own needs.” Your business or organization can have negative environmental impacts like direct or indirect carbon emissions, unrecyclable waste, and damage to shared resources like clean water.
	   
	2) ***Improvement process***  
	    The architectural improvement process includes understanding what you have and what you can do to improve, selecting targets for improvement, testing improvements, adopting successful improvements, quantifying your success and sharing what you have learned so that it can be replicated elsewhere, and then repeating the cycle.
	   
	3) ***Sustainability as a non-functional requirement***  
	    Adding sustainability to your list of business requirements can result in more cost-effective solutions. Focusing on getting more value from the resources you use and using fewer of them directly translates to cost savings on AWS as you pay only for what you use.
	   
	4) ***Best practices for sustainability in the cloud***  
	    Optimize workload placement, and optimize your architecture for demand, software, data, hardware, and process to increase energy efficiency. Each of these areas represents opportunities to employ best practices to reduce the sustainability impact of your cloud workload by maximizing utilization, and minimizing waste and the total resources deployed and powered to support your workload.
	   
	   

----
### NL
-----
#### CROPSS  (Six Pillars) - Info (Kort)
1) ***C*ost optimization pillar**  
    De Cost optimization (kostenoptimalisatie) richt zich op het vermijden van onnodige kosten. Belangrijke onderwerpen zijn onder meer het begrijpen van uitgaven in de loop van de tijd en het beheersen van de toewijzing van middelen, het selecteren van middelen van het juiste type en de juiste hoeveelheid, en opschalen om aan de bedrijfsbehoeften te voldoen zonder te veel uit te geven.
      
2) ***R*eliability pillar**  
    De Reliability (betrouwbaarheids) richt zich op workloads die hun beoogde functies uitvoeren en hoe snel kan worden hersteld als niet aan de eisen wordt voldaan. Belangrijke onderwerpen zijn onder meer het ontwerp van gedistribueerde systemen, herstelplanning en aanpassing aan veranderende eisen.
   
3) ***O*perational Excellence pillar**  
    De Operational Excellence (Operational Excellence) richt zich op het draaien en monitoren van systemen en het continu verbeteren van processen en procedures. Belangrijke onderwerpen zijn onder meer het automatiseren van wijzigingen, het reageren op gebeurtenissen en het definiëren van standaarden voor het beheer van de dagelijkse activiteiten.
   
4) ***P*erformance efficiency pillar**  
    De Performance efficiency (prestatie-efficiëntie) richt zich op gestructureerde en gestroomlijnde toewijzing van IT- en computerresources. Belangrijke onderwerpen zijn onder meer het selecteren van resourcetypen en -groottes die zijn geoptimaliseerd voor werklastvereisten, het bewaken van de prestaties en het handhaven van de efficiëntie naarmate de bedrijfsbehoeften evolueren.
   
5) ***S*ecurity pillar**  
    De Security (beveiligings) richt zich op het beschermen van informatie en systemen. Belangrijke onderwerpen zijn vertrouwelijkheid en integriteit van gegevens, het beheer van gebruikersmachtigingen en het opzetten van controles om beveiligingsgebeurtenissen te detecteren.
   
6) ***S*ustainability pillar**  
    De Sustainability (duurzaamheids) richt zich op het minimaliseren van de milieueffecten van het uitvoeren van cloudworkloads. Belangrijke onderwerpen zijn onder meer een model voor gedeelde verantwoordelijkheid voor duurzaamheid, inzicht in de impact en het maximaliseren van het gebruik om de benodigde middelen te minimaliseren en de downstream-impact te verminderen.


#### CROPSS  (Six Pillars) - Info (Deep)
De 'White Paper' met meer informatie:
1) ***C*ost optimization pillar**  
	1) ***Cost optimization***  
	    Kostenoptimalisatie is een continu proces van verfijning en verbetering gedurende de levenscyclus van een werklast. De werkwijzen in dit document helpen u bij het bouwen en gebruiken van kostenbewuste workloads die bedrijfsresultaten behalen, terwijl de kosten worden geminimaliseerd en uw organisatie in staat wordt gesteld het rendement op de investering te maximaliseren.
	   
	2) ***Practice cloud financial management***  
	    Het beheren van cloudfinanciering vereist het ontwikkelen van uw bestaande financiële processen om kostentransparantie, controle, planning en optimalisatie voor uw AWS-omgevingen tot stand te brengen en te laten werken.
	  ![resultaat](/00_includes/AWS-12-resultaat.png "resultaat")
	   
	3) ***Practice Cloud Financial Management***  
	    Het beheren van cloudfinanciering vereist het ontwikkelen van uw bestaande financiële processen om kostentransparantie, controle, planning en optimalisatie voor uw AWS-omgevingen tot stand te brengen en te laten werken.
	   
	4) ***Expenditure and usage awareness***  
	    Inzicht in de kosten en drijfveren van uw organisatie is van cruciaal belang om uw kosten en gebruik effectief te beheren en mogelijkheden voor kostenbesparing te identificeren.
	   
	5) ***Cost effective resourcess***  
	    Het gebruik van de juiste services, resources en configuraties voor uw workloads is de sleutel tot kostenbesparingen. Houd rekening met het volgende bij het maken van kosteneffectieve resources:
		1) AWS Solutions Architects 
		2) AWS Solutions 
		3) AWS Reference Architectures 
		4) APN Partners
	   
	6) ***Manage demand and supply resources***  
	    Wanneer u naar de cloud overstapt, betaalt u alleen voor wat u nodig heeft. U kunt middelen leveren die passen bij de vraag naar werklast op het moment dat ze nodig zijn, waardoor kostbare en verspillende overprovisioning overbodig wordt. U kunt de vraag ook wijzigen met behulp van een beperking, buffer of wachtrij om de vraag af te vlakken en met minder middelen te bedienen.
	   
	7) ***Optimize over time***  
	    In AWS optimaliseert u in de loop van de tijd door nieuwe services te beoordelen en deze in uw werklast te implementeren.
	   
      
2) ***R*eliability pillar**  
	1) ***Reliability***  
	    De betrouwbaarheidspijler omvat het vermogen van een workload om de beoogde functie correct en consistent uit te voeren wanneer dat wordt verwacht. Dit omvat de mogelijkheid om de werkbelasting gedurende de gehele levenscyclus te bedienen en te testen. Deze paper biedt diepgaande best practice-richtlijnen voor het implementeren van betrouwbare workloads op AWS.
	   
	2) ***Foundations***  
	    Fundamentele vereisten zijn vereisten waarvan de reikwijdte verder reikt dan een enkele werklast of project. Voordat u een systeem ontwerpt, moeten er fundamentele vereisten zijn die van invloed zijn op de betrouwbaarheid. U moet bijvoorbeeld voldoende netwerkbandbreedte hebben naar uw datacenter.
	   
	3) ***Workload architecture***   
	    Een betrouwbare workload begint met ontwerpbeslissingen vooraf voor zowel software als infrastructuur. Uw architectuurkeuzes zijn van invloed op uw werklastgedrag in alle zes Well-Architected-pijlers. Voor betrouwbaarheid zijn er specifieke patronen die u moet volgen.
	   
	4) ***Change management***   
	    Veranderingen in uw werklast of de omgeving ervan moeten worden geanticipeerd en aangepast om een ​​betrouwbare werking van de werklast te bereiken. Veranderingen zijn onder meer wijzigingen die aan uw werklast worden opgelegd, zoals pieken in de vraag, maar ook wijzigingen van binnenuit, zoals functie-implementaties en beveiligingspatches.
	   
	5) ***Failure management***   
	    Storingen in hardwarecomponenten op laag niveau zijn iets dat elke dag moet worden opgelost in een on-premises datacenter. In de cloud moet u echter beschermd zijn tegen de meeste van dit soort storingen. Amazon EBS-volumes worden bijvoorbeeld in een specifieke beschikbaarheidszone geplaatst waar ze automatisch worden gerepliceerd om u te beschermen tegen het falen van een enkel onderdeel. Alle EBS-volumes zijn ontworpen voor 99,999% beschikbaarheid. Amazon S3-objecten worden opgeslagen in minimaal drie beschikbaarheidszones die 99,999999999% duurzaamheid van objecten gedurende een bepaald jaar bieden. Ongeacht uw cloudprovider bestaat de kans dat storingen uw werklast beïnvloeden. Daarom moet u stappen ondernemen om veerkracht te implementeren als uw werkbelasting betrouwbaar moet zijn.
	   
   
3) ***O*perational Excellence pillar**  
	1) ***Operational excellence***  
	    Bij Amazon definiëren we operationele uitmuntendheid als een toewijding om software correct te bouwen en tegelijkertijd een geweldige klantervaring te bieden. Het bevat best practices voor het organiseren van uw team, het ontwerpen van uw werkbelasting, het op grote schaal uitvoeren ervan en het in de loop van de tijd ontwikkelen. Operationele uitmuntendheid helpt uw ​​team om meer tijd te besteden aan het bouwen van nieuwe functies die klanten ten goede komen, en minder tijd aan onderhoud en brandbestrijding. Om correct te bouwen, kijken we naar best practices die resulteren in goed draaiende systemen, een evenwichtige werkdruk voor u en uw team, en vooral een geweldige klantervaring.
	   
	2) ***Organization***  
	    U moet de prioriteiten van uw organisatie, uw organisatiestructuur en hoe uw organisatie uw teamleden ondersteunt begrijpen, zodat zij uw bedrijfsresultaten kunnen ondersteunen.
	   
	3) ***Prepare***  
	    Om u voor te bereiden op operational excellence, moet u inzicht hebben in uw workloads en het verwachte gedrag. Vervolgens kunt u ze ontwerpen om inzicht te geven in hun status en de procedures bouwen om ze te ondersteunen.
	   
	4) ***Operate***  
	    Succes is het behalen van bedrijfsresultaten zoals gemeten aan de hand van de statistieken die u definieert. Door inzicht te krijgen in de gezondheid van uw werklast en activiteiten, kunt u vaststellen wanneer de resultaten van de organisatie en het bedrijf gevaar lopen of lopen, en kunt u hier op gepaste wijze op reageren.
	   
	5) ***Evolve***
	    Evolutie is de continue cyclus van verbetering in de tijd. Implementeer regelmatig kleine incrementele wijzigingen op basis van de lessen die zijn geleerd uit uw operationele activiteiten en evalueer hun succes bij het tot stand brengen van verbeteringen.
	   
   
4) ***P*erformance efficiency pillar**  
	1) ***Performance efficiency***  
	    The performance efficiency pillar focuses on the efficient use of computing resources to meet requirements, and how to maintain efficiency as demand changes and technologies evolve.
	   
	2) ***Selection***  
	    De optimale oplossing voor een bepaalde workload varieert en oplossingen combineren vaak meerdere benaderingen. Goed ontworpen workloads gebruiken meerdere oplossingen en maken verschillende functies mogelijk om de prestaties te verbeteren.
	   
	3) ***Review***  
	    Bij het ontwerpen van workloads zijn er eindige opties waaruit u kunt kiezen. Na verloop van tijd komen er echter nieuwe technologieën en benaderingen beschikbaar die de prestaties van uw workload kunnen verbeteren. In de cloud is het veel gemakkelijker om te experimenteren met nieuwe functies en services, omdat je infrastructuur code is.
	   
	4) ***Monitoring***  
	    Nadat u uw architectuur hebt geïmplementeerd, moet u de prestaties ervan bewaken, zodat u eventuele problemen kunt oplossen voordat ze gevolgen hebben voor uw klanten. Monitoringstatistieken moeten worden gebruikt om alarm te slaan wanneer drempels worden overschreden.
	   
	5) ***Trade-offs***
	    Denk bij het ontwerpen van oplossingen na over compromissen om een ​​optimale aanpak te garanderen. Afhankelijk van uw situatie kunt u consistentie, duurzaamheid en ruimte inruilen voor tijd of latentie om betere prestaties te leveren.
	   
   
5) ***S*ecurity pillar**  
	1) ***Security foundations***  
	    De beveiligingspijler beschrijft hoe u kunt profiteren van cloudtechnologieën om gegevens, systemen en activa te beschermen op een manier die uw beveiligingspostuur kan verbeteren. Deze paper biedt diepgaande richtlijnen voor best practices voor het ontwerpen van veilige workloads op AWS.
	   
	2) ***Identity and access management***  
	    To use AWS services, you must grant your users and applications access to resources in your AWS accounts. As you run more workloads on AWS, you need robust identity management and permissions in place to ensure that the right people have access to the right resources under the right conditions. AWS offers a large selection of capabilities to help you manage your human and machine identities and their permissions. The best practices for these capabilities fall into two main areas.
	   
	3) ***Detection***  
	    Detectie bestaat uit twee delen: detectie van onverwachte of ongewenste configuratiewijzigingen en de detectie van onverwacht gedrag. De eerste kan plaatsvinden op meerdere plaatsen in de levenscyclus van een applicatielevering. Door infrastructuur als code te gebruiken (bijvoorbeeld een CloudFormation-sjabloon), kunt u controleren op ongewenste configuratie voordat een werkbelasting wordt geïmplementeerd door controles in de CI/CD-pijplijnen of bronbeheer te implementeren. Vervolgens kunt u, terwijl u een workload implementeert in niet-productie- en productieomgevingen, de configuratie controleren met native AWS-, open source- of AWS Partner-tools. Deze controles kunnen betrekking hebben op configuraties die niet voldoen aan beveiligingsprincipes of best practices, of op wijzigingen die zijn aangebracht tussen een geteste en geïmplementeerde configuratie. Voor een actieve toepassing kunt u controleren of de configuratie op een onverwachte manier is gewijzigd, ook buiten een bekende implementatie of geautomatiseerde schaalgebeurtenis.
	   
	4) ***Infrastructure protection***  
	    Infrastructuurbescherming omvat controlemethodologieën, zoals diepgaande verdediging, die nodig zijn om te voldoen aan best practices en organisatorische of regelgevende verplichtingen. Het gebruik van deze methodologieën is van cruciaal belang voor succesvolle, doorlopende activiteiten in de cloud.
	   
	5) ***Data protection***  
	    Voordat u een workload ontwerpt, moeten er basispraktijken aanwezig zijn die van invloed zijn op de beveiliging. Gegevensclassificatie biedt bijvoorbeeld een manier om gegevens te categoriseren op basis van gevoeligheidsniveaus, en encryptie beschermt gegevens door ze onbegrijpelijk te maken voor ongeoorloofde toegang. Deze methoden zijn belangrijk omdat ze doelstellingen ondersteunen, zoals het voorkomen van verkeerd gebruik of het naleven van wettelijke verplichtingen.
	   
	6) ***Incident response***  
	    Zelfs met volwassen preventieve en detectiecontroles, moet uw organisatie mechanismen implementeren om te reageren op en de potentiële impact van beveiligingsincidenten te beperken. Uw voorbereiding heeft grote invloed op het vermogen van uw teams om effectief te opereren tijdens een incident, om problemen te isoleren, in te dammen en forensisch onderzoek uit te voeren, en om operaties te herstellen naar een bekende goede staat. Door de tools en toegang voorafgaand aan een beveiligingsincident in te voeren en vervolgens tijdens gamedagen routinematig incidentrespons te oefenen, kunt u ervoor zorgen dat u kunt herstellen en tegelijkertijd de bedrijfsonderbreking tot een minimum kunt beperken.
	   
	7) ***Application security***
	    Applicatiebeveiliging (AppSec) beschrijft het algemene proces van hoe u de beveiligingseigenschappen ontwerpt, bouwt en test van de workloads die u ontwikkelt. U moet goed opgeleide mensen in uw organisatie hebben, de beveiligingseigenschappen van uw build- en release-infrastructuur begrijpen en automatisering gebruiken om beveiligingsproblemen te identificeren.
	   
   
6) ***S*ustainability pillar**  
	1) ***Cloud sustainability***  
	    De discipline duurzaamheid richt zich op de ecologische, economische en maatschappelijke impact van uw bedrijfsactiviteiten op de lange termijn. De Wereldcommissie voor Milieu en Ontwikkeling van de Verenigde Naties definieert duurzame ontwikkeling als "ontwikkeling die voorziet in de behoeften van het heden zonder het vermogen van toekomstige generaties om in hun eigen behoeften te voorzien in gevaar te brengen". Uw bedrijf of organisatie kan negatieve gevolgen hebben voor het milieu, zoals directe of indirecte koolstofemissies, niet-recyclebaar afval en schade aan gedeelde hulpbronnen zoals schoon water.
	   
	2) ***Improvement process***  
	    Het architecturale verbeteringsproces omvat het begrijpen van wat u heeft en wat u kunt doen om te verbeteren, het selecteren van doelen voor verbetering, het testen van verbeteringen, het toepassen van succesvolle verbeteringen, het kwantificeren van uw succes en het delen van wat u hebt geleerd zodat het elders kan worden gerepliceerd, en vervolgens het herhalen van de fiets.
	   
	3) ***Sustainability as a non-functional requirement***  
	    Het toevoegen van duurzaamheid aan uw lijst met zakelijke vereisten kan resulteren in meer kosteneffectieve oplossingen. Als u zich richt op het halen van meer waarde uit de bronnen die u gebruikt en er minder van gebruikt, vertaalt dit zich direct in kostenbesparingen op AWS, aangezien u alleen betaalt voor wat u gebruikt.
	   
	4) ***Best practices for sustainability in the cloud***  
	    Optimaliseer de plaatsing van werklasten en optimaliseer uw architectuur voor vraag, software, gegevens, hardware en processen om de energie-efficiëntie te verhogen. Elk van deze gebieden vertegenwoordigt kansen om best practices toe te passen om de duurzaamheidsimpact van uw cloudworkload te verminderen door het gebruik te maximaliseren en verspilling en de totale middelen die worden ingezet en aangedreven om uw workload te ondersteunen, te minimaliseren.
	   1) ***Region selection***  
	   2) ***User behavior patterns***  
	   3) ***Software and architecture patterns***  
	   4) ***Measure results***  
	   5) ***Data patterns***  
	   
	   



### Gebruikte bronnen
https://aws.amazon.com/architecture/well-architected/
https://docs.aws.amazon.com/waf/
https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html
https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/pillars-of-the-well-architected-framework.html
https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc

https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html
https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html
https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html
https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html
https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html
https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html

### Ervaren problemen
Veel theory met rabbit-holes voor hoe deep je moet gaan, ik ging het erbij houden om korte algemene info erover te beschrijven en niet te deep om in gaan. De Engelse versie heb ik gewoon toevoegt aangezien de exames en termen breder zijn in het engels dan nederlands.

### Resultaat
Het kort kunnen uitleggen wat een Well Architected Framework is en bij elke pilliar beetje meer informatie kan geven.