# Onderwerpen Cloud Fundamentals
Vertellen hoe andere AWS services werken namelijke: ECS, Support Plan, Trusted Advisor, Config, Cloud Trial, IAM, Cloudwatch, DYnamoDB, Lambda, SNS, SQS en Event Bridges.

### [ECS](https://aws.amazon.com/ecs/) 
Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the Amazon Web Services (AWS) Cloud. Using Amazon EC2 eliminates your need to invest in hardware up front, so you can develop and deploy applications faster. You can use Amazon EC2 to launch as many or as few virtual servers as you need, configure security and networking, and manage storage. Amazon EC2 enables you to scale up or down to handle changes in requirements or spikes in popularity, reducing your need to forecast traffic.

![resultaat](/00_includes/AWS-13a-resultaat22.png "resultaat")

#### Vragen voor theoretisch onderzoek:
- ##### Waar is [EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) voor?  
  Amazon Elastic Compute Cloud (Amazon EC2) biedt schaalbare computerkracht in de Amazon Web Services (AWS) Cloud. Met Amazon EC2 wordt het investeringen in hardware weggehaald, zodat je sneller applicaties kunt ontwikkelen en implementeren. Je kan het gebruiken om zoveel of zo weinig mogelijke virtuele servers op te starten die je nodig hebt, configureren van je beveiliging en netwerken en opslagruimte beheren.
  
- ##### Hoe past / vervangt EC2 in een on-premises setting?  
  Het **vervangt** om vooraf in hardware te investeren en stelt het u in staat om snel op te schalen of af te schalen om veranderingen in vereisten of pieken in populariteit aan te kunnen. Bij
  
- ##### Hoe kan ik EC2 combineren met andere diensten?  
  Je kan de volgende diensten van AWS combineren:
  1) AWS Migration Tools
  2) AWS Managed Services
  3) Amazon Lightsail om uw applicaties gemakkelijk te migreren en te bouwen
  Deze volgenden diensten zijn buiten van AWS om maar wel mogelijke

- ##### Wat is het verschil tussen EC2 en andere gelijksoortige diensten?  
  


### [AWS Support Plans](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)
#### Vragen voor theoretisch onderzoek:
- ##### Waar is AWS Support Plans voor?  
  AWS Support Plans offers five support plans:

-   **Basic**
	1) One-on-one responses to account and billing question.
	2) Support forums.
	3) Service health checks.
	4) Documentation, technical papers, and best practice guides.

-   **Developer** 
	1) Best practice guidance.
	2) Client-side diagnostic tools.
	3) Building-block architecture support: guidance on how to use AWS products, features, and services together.
	4) Supports an unlimited number of support cases that can be opened by one primary contact, which is the [AWS account _root user_](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html).
	   
-   **Business**
	1) Use-case guidance – What AWS products, features, and services to use to best support your specific needs.
	2) [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) – A feature of AWS Support, which inspects customer environments and identifies opportunities to save money, close security gaps, and improve system reliability and performance. You can access all Trusted Advisor checks.
	3) The AWS Support API to interact with Support Center and Trusted Advisor. You can use the AWS Support API to automate support case management and Trusted Advisor operations.
	4) Third-party software support – Help with Amazon Elastic Compute Cloud (Amazon EC2) instance operating systems and configuration. Also, help with the performance of the most popular third-party software components on AWS. Third-party software support isn't available for customers on Basic or Developer Support plans.
	5) Supports an unlimited number of AWS Identity and Access Management (IAM) users who can open technical support cases.
    
-   **Enterprise On-Ramp** OR **Enterprise**
	1) Application architecture guidance – Consultative guidance on how services fit together to meet your specific use case, workload, or application.
	2) Infrastructure event management – Short-term engagement with AWS Support to get a deep understanding of your use case. After analysis, provide architectural and scaling guidance for an event.
	3) Technical account manager – Work with a technical account manager (TAM) for your specific use cases and applications.
	4) White-glove case routing.
	5) Management business reviews.
  
- ##### Hoe past / vervangt AWS Support Plans in een on-premises setting?  
  Het wordt vervangen om de technische ondersteuning die je normaal gesproken zou hebben in een on-premises omgeving.
  
- ##### Hoe kan ik AWS Support Plans combineren met andere diensten?  
  Dit is een helpdesk omgeving waardoor je de juiste plan moet selecteren om de juiste behoefte hulp te kunnen krijgen.
  
  
- ##### Wat is het verschil tussen AWS Support Plans en andere gelijksoortige diensten?  
  Direct hulp van de expterise op het field omdat ze alle diensten onder een omgeving hebben of die kunnen worden aangesloten. Omdat je hun diensten en producten gebruikt.

### [Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)
Trusted Advisor draws upon best practices learned from serving hundreds of thousands of AWS customers. Trusted Advisor inspects your AWS environment, and then makes recommendations when opportunities exist to save money, improve system availability and performance, or help close security gaps.
![resultaat](/00_includes/AWS-13a-resultaat23.png "resultaat")

1) If you have a Basic or Developer Support plan, you can use the Trusted Advisor console to access all checks in the Service Limits category and six checks in the Security category.
2) If you have a Business, Enterprise On-Ramp, or Enterprise Support plan, you can use the Trusted Advisor console and the [AWS Support API](https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html) to access all Trusted Advisor checks. You also can use Amazon CloudWatch Events to monitor the status of Trusted Advisor checks. For more information, see [Monitoring AWS Trusted Advisor check results with Amazon EventBridge](https://docs.aws.amazon.com/awssupport/latest/user/cloudwatch-events-ta.html).

You can access Trusted Advisor in the AWS Management Console. For more information about controlling access to the Trusted Advisor console, see [Manage access to AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html).

#### Vragen voor theoretisch onderzoek:
- ##### Waar is [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) voor?  
  Het is een dienst die aanbevelingen geeft om je te helpen voor het volgen van AWS-best practices, waarbij het je account evalueert met behulp van de controles. Deze controles identificeren de manieren om je AWS-infrastructuur:
  1) Optimaliseren
  2) Beveiliging en prestaties te verbeteren
  3) Kosten te verlagen
  4) Servicequota’s te bewaken
  
- ##### Hoe past / vervangt Trusted Advisor in een on-premises setting?  
  Het is specifiek bedoeld voor je AWS-omgeving te optimaliseren.  Dus je kan dit niet vervangen of toepassen op je on-premises settings.
  
- ##### Hoe kan ik Trusted Advisor combineren met andere diensten?  
  Het is meer een rapport die aangeeft welke diensten met de beste opties zijn ter vegelijken die je nu al hebt. 
  
- ##### Wat is het verschil tussen Trusted Advisor en andere gelijksoortige diensten?  
  Omdat dit speciaal is gemaakt voor AWS diensten zelf heb je geen gelijksoortige diensten ervan. Voor on-premises zou je eigen analyze moeten maken.

### [AWS Config](https://aws.amazon.com/config/) 
AWS Config continually assesses, audits, and evaluates the configurations and relationships of your resources on AWS, on premises, and on other clouds.
![resultaat](/00_includes/AWS-13a-resultaat24.png "resultaat")
#### Vragen voor theoretisch onderzoek:
- ##### Waar is [AWS Config](https://aws.amazon.com/config/) voor?  
  AWS Config is een tool die je helpt bij het beoordelen, controleren en evalueren van de configuraties van uw AWS-resources. Het kan worden gebruikt om veranderingen in de configuratie van uw resources te volgen en om compliance met je organisatiebeleid te controleren
  
- ##### Hoe past / vervangt AWS Config in een on-premises setting?  
  Het is specifiek bedoeld voor je AWS-omgeving
  
- ##### Hoe kan ik [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) combineren met andere diensten?  
  Je kan de volgende diensten van AWS combineren:
  1) **Amazon S3:** 
  2) **Amazon SNS:** om configuratiegegevens op te slaan en meldingen te verzenden.
  
- ##### Wat is het verschil tussen AWS Config en andere gelijksoortige diensten?  
  Omdat dit speciaal is gemaakt voor AWS diensten zelf heb je geen gelijksoortige diensten ervan. Voor on-premises zou je eigen configuraties moeten maken.

### [AWS Cloud Trail](https://aws.amazon.com/cloudtrail/)
AWS Cloud Trail monitors and records account activity across your AWS infrastructure, giving you control over storage, analysis, and remediation actions.
![resultaat](/00_includes/AWS-13a-resultaat25.png "resultaat")
#### Vragen voor theoretisch onderzoek:
- ##### Waar is [AWS Cloud Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)voor?  
  Het is een AWS-service die je helpt bij het inschakelen:
  1) Operationele en risico-audits, 
  2) Governance en naleving van uw AWS-account. 
  Acties die worden ondernomen door:
  1) Gebruiker 
  2) Rol 
  3) AWS-service 
  Worden geregistreerd als gebeurtenissen in CloudTrail. Gebeurtenissen omvatten acties die worden ondernomen in de AWS Management Console, AWS Command Line Interface en AWS SDK’s en API’s
  
- ##### Hoe past / vervangt AWS Cloud Trail in een on-premises setting?  
  Het is een monitoren systeem binnen je AWS account. Bij on-premise zou je eigen log systeem hebben of van andere party voor het bijhouden voor wijziging op het system.
  
- ##### Hoe kan ik AWS Cloud Trail combineren met andere diensten?    
  Je kan de volgende diensten van AWS combineren: 
  1) AWS Management Console
  2) AWS Command Line Interface
  3) AWS SDK’s en API’s
  
- ##### Wat is het [verschil](https://blog.awsfundamentals.com/cloudwatch-vs-cloudtrail-understanding-the-differences) tussen AWS Cloud Trail en andere gelijksoortige diensten?  
  Zowel bij AWS CloudWatch als CloudTrail is het een monitoring- en loggingservices, maar de verschillen zijn: 
  1) **CloudWatch:** Wordt gebruikt om de interne werking van een applicatie te monitoren en te loggen. 
  2) **CloudTrail:** Wordt gebruikt om alle API-activiteiten bij te houden die plaatsvinden binnen een AWS-account.

### [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)
With AWS Identity and Access Management (IAM), you can specify who or what can access services and resources in AWS, centrally manage fine-grained permissions, and analyze access to refine permissions across AWS.
![resultaat](/00_includes/AWS-13a-resultaat26.png "resultaat")
#### Vragen voor theoretisch onderzoek:
- ##### Waar is [Identity and Access Management (IAM)](https://aws.amazon.com/iam/) voor?  
  Het is een AWS-service die je helpt met het beheren van toegang tot AWS-services op een veilige manier zonder extra kosten.   
  
  Je kan gebruikers en groepen:  
  1) Maken
  2) Beheren
  3) Machtigingen gebruiken om hun toegang tot AWS-bronnen toe te staan of te weigeren.
  
- ##### Hoe past / vervangt Identity and Access Management (IAM) in een on-premises setting?    
  Het is specifiek bedoeld voor je AWS-omgeving die toegang behoort te krijgen ervan. Het kan niet je eigen on-premses settings vervangen omdat niet mogelijke is, die blijft los staan ervan. Hiervoor is het bedoeld om AWS diensten te gebruiken voor andere gebruikers.
  
- ##### Hoe kan ik Identity and Access Management (IAM) combineren met andere diensten?  
  Je kan niet combineren omdat het meer toegang kan geven voor het gebruiken voor het aantal diensten zoals het lezen van S3 objecten of het gebruiken van een AWS-dienst.
  
- ##### Wat is het verschil tussen Identity and Access Management (IAM) en andere gelijksoortige diensten?  
  Je kan het vergelijken met andere applicaties die de gebruikers beheren voor andere toestemmingen die buiten om AWS zijn. 
  1) **Windows:** Bij scholen waarbij je een 'Admin' en 'Student' account hebt.
  2) **Azure:** Vergelijkebaar structuur met zelfde opzet dan voor Azure omgeving.
  
#### Vragen voor praktisch onderzoek:
- ##### Waar kan ik deze dienst vinden in de console?  
- ##### Hoe zet ik deze dienst aan?  
- ##### Hoe kan ik deze dienst koppelen aan andere resources?  
  Zie de opdrachten onderaan:

### [AWS Cloudwatch](https://aws.amazon.com/cloudwatch/)
Amazon CloudWatch collects and visualizes real-time logs, metrics, and event data in automated dashboards to streamline your infrastructure and application maintenance.
![resultaat](/00_includes/AWS-13a-resultaat27.png "resultaat")
#### Vragen voor theoretisch onderzoek:
- ##### Waar [is](https://intellipaat.com/blog/what-is-cloudwatch-in-aws/) [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) voor?  
  Het is een realtime monitoring- en beheerservice van AWS  diensten die is ontworpen om de services en bronnen die worden gebruikt te onderhouden. Het is speciaal ontworpen om  leven gemakkelijker te maken voor:   
  1) Ontwikkelaars
  2) Site reliability engineers
  3) IT-managers en systeemoperators
 
- ##### Hoe past / vervangt CloudWatch in een on-premises setting?  
  Het is een monitoren systeem binnen je AWS diensten. Bij on-premise kan je CloudWatch zelf eraan toevoegen en het hangt echt af of je eigen applicatie een ingebouwde log systeem heeft tot beschikking.  
  
- ##### Hoe kan ik CloudWatch combineren met andere diensten?   
  Je kan de volgende diensten van AWS combineren: 
  1) EC2 instances
  2) DynamoDB tables
  3) Amazon RDS DB instances
  
- ##### Wat is het verschil tussen CloudWatch en andere gelijksoortige diensten?  
  Zowel bij AWS CloudWatch als CloudTrail is het een monitoring- en loggingservices, maar de verschillen zijn: 
  1) **CloudWatch:** Wordt gebruikt om de interne werking van een applicatie te monitoren en te loggen. 
  2) **CloudTrail:** Wordt gebruikt om alle API-activiteiten bij te houden die plaatsvinden binnen een AWS-account.
  

#### Vragen voor praktisch onderzoek:
- ##### Waar kan ik deze dienst vinden in de console?  
- ##### Hoe zet ik deze dienst aan?  
- ##### Hoe kan ik deze dienst koppelen aan andere resources?   
  Zie de opdrachten onderaan:

### [DynamoDB](https://aws.amazon.com/dynamodb/)
Amazon DynamoDB is a fully managed, serverless, key-value NoSQL database designed to run high-performance applications at any scale. DynamoDB offers built-in security, continuous backups, automated multi-Region replication, in-memory caching, and data import and export tools.
![resultaat](/00_includes/AWS-13a-resultaat28.png "resultaat")
#### Vragen voor theoretisch onderzoek:
- ##### Waar [is](https://aws.amazon.com/dynamodb/) DynamoDB voor?  
  Het is een volledig beheerde, serverloze, key-value NoSQL-database die is ontworpen om high-performance applicaties op elke schaal uit te voeren: 
  1) Ingebouwde beveiliging, 
  2) Continue back-ups, 
  3) Geautomatiseerde multi-Region-replicatie, 
  4) In-memory caching en 
  5) Tools voor het importeren en exporteren van gegevens.
  
- ##### Hoe past / vervangt DynamoDB in een on-premises setting?  
  Het vervangt je bestaande database met Amazon DynamoDB  omdat die draait in een AWS omgeving. 
  
- ##### Hoe kan ik DynamoDB combineren met [andere](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/OtherServices.html) diensten?  
  Je kan de volgende diensten van AWS combineren:  
  1) Configureren van AWS-referenties in uw bestanden met behulp van Amazon Cognito.
  2) Laden van gegevens van DynamoDB naar Amazon Redshift.
  3) Verwerken van DynamoDB-gegevens met Apache Hive op Amazon EMR
  
- ##### Wat is het verschil tussen DynamoDB en andere gelijksoortige diensten?  
  Het is een NoSQL database waardoor het geen SQL gebruikt.

#### Vragen voor praktisch onderzoek:
- ##### Waar kan ik deze dienst vinden in de console?  
- ##### Hoe zet ik deze dienst aan?  
- ##### Hoe kan ik deze dienst koppelen aan andere resources?   
  Zie de opdrachten onderaan:

### [AWS Lambda](https://aws.amazon.com/lambda/)
AWS Lambda is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers. You can trigger Lambda from over 200 AWS services and software as a service (SaaS) applications, and only pay for what you use.

#### Vragen voor theoretisch onderzoek:
- ##### Waar is [Lambda](https://aws.amazon.com/lambda/) voor?  
  Het is een serverloze, event-gedreven compute-service waarmee je code kunt uitvoeren voor vrijwel elk type applicatie of backend-service zonder servers te hoeven beheren. Je kan het activeren vanuit meer dan 200 AWS diensten en software als een service (SaaS) -applicaties en alleen betalen voor wat je gebruikt.  
  
- **File processing:** Use Amazon Simple Storage Service (Amazon S3) to trigger Lambda data processing in real time after an upload.      ![resultaat](/00_includes/AWS-13a-resultaat53.png "resultaat")

- **Stream processing:** Use Lambda and Amazon Kinesis to process real-time streaming data for application activity tracking, transaction order processing, clickstream analysis, data cleansing, log filtering, indexing, social media analysis, Internet of Things (IoT) device data telemetry, and metering.    ![resultaat](/00_includes/AWS-13a-resultaat54.png "resultaat")
  
- **Web applications:** Combine Lambda with other AWS services to build powerful web applications that automatically scale up and down and run in a highly available configuration across multiple data centers.    ![resultaat](/00_includes/AWS-13a-resultaat55.png "resultaat")
  
- **IoT backends:** Build serverless backends using Lambda to handle web, mobile, IoT, and third-party API requests.   ![resultaat](/00_includes/AWS-13a-resultaat56.png "resultaat")
  
- **Mobile backends:** Build backends using Lambda and Amazon API Gateway to authenticate and process API requests. Use AWS Amplify to easily integrate with your iOS, Android, Web, and React Native frontends.    ![resultaat](/00_includes/AWS-13a-resultaat57.png "resultaat")
  

- ##### Hoe past / vervangt Lambda in een [on-premises](https://help.mypurecloud.com/articles/example-aws-lambda-data-action-with-on-premises-solution/) setting?  
  Lambda is een soort tussenpersoon die luister naar de **Triggeres** van uit eigen AWS diensten of andere partijen met hulp van AWS EventBridge en dat wordt vestuurd naar de **Destination** eigen AWS diensten of Eventbus.
  
- ##### Hoe kan ik Lambda combineren met andere diensten?  
  Zoals eerder gezegd kan je het combineren met wel 200 AWS diensten en services and software as a service (SaaS) applicaties. 
  
- ##### Wat is het [verschil]([Compare AWS Lambda to Azure, GCP serverless platforms | TechTarget](https://www.techtarget.com/searchaws/tip/Compare-AWS-Lambda-to-Azure-GCP-serverless-platforms)) tussen Lambda en andere gelijksoortige diensten?  
  Ja, er zijn andere gelijksoortige diensten die een andere programmeurtalen ondersteunen.  
|  	| [**AWS Lambda**](https://aws.amazon.com/lambda/faqs/) 	| [**Microsoft Azure Functions**](https://learn.microsoft.com/en-us/azure/azure-functions/) 	| [**Google Cloud Functions**](https://cloud.google.com/functions/docs/) 	|
|---	|---	|---	|---	|
| **Runtime API** 	| ✔ 	| ✔ 	| ✔ 	|
| **Python** 	| ✔ 	| ✔ 	| ✔ 	|
| **Java** 	| ✔ 	| ✔ 	| ✔ 	|
| **C#** 	| ✔ 	| ✔ 	| ✔ 	|
| **Go** 	| ✔ 	| ✔ 	| ✔ 	|
| **Node.js** 	| ✔ 	| ✔ 	| ✔ 	|
| **Ruby** 	| ✔ 	| ✔ 	| ✔ 	|
| **PowerShell** 	| ✔ 	| ✔ 	|  	|
| **TypeScript** 	| ✔ 	| ✔ 	|  	|
| **_Kubernets_** 	| ✔ 	| ✔ 	|  	|

#### Vragen voor praktisch onderzoek:
- ##### Waar kan ik deze dienst vinden in de console?  
- ##### Hoe zet ik deze dienst aan?  
- ##### Hoe kan ik deze dienst koppelen aan andere resources?   
  Zie de opdrachten onderaan:

### [SNS](https://aws.amazon.com/sns/)  
Amazon Simple Notification Service (SNS) sends notifications two ways, A2A and A2P. A2A provides high-throughput, push-based, many-to-many messaging between distributed systems, microservices, and event-driven serverless applications. These applications include Amazon Simple Queue Service (SQS), Amazon Kinesis Data Firehose, AWS Lambda, and other HTTPS endpoints. A2P functionality lets you send messages to your customers with SMS texts, push notifications, and email.
![resultaat](/00_includes/AWS-13a-resultaat30.png "resultaat")
#### Vragen voor theoretisch onderzoek:
- ##### Waar is [SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) voor?  
  Het is een volledig beheerde service die bericht verstuurt van uitgevers naar abonnees (ook wel producenten en consumenten genoemd). Uitgevers communiceren asynchroon met abonnees door berichten naar een onderwerp te sturen, wat een logisch toegangspunt en communicatiekanaal is. Klanten kunnen zich abonneren op het SNS-onderwerp en gepubliceerde berichten ontvangen met behulp van een ondersteund eindpunttype, zoals Amazon Kinesis Data Firehose, Amazon SQS, AWS Lambda, HTTP, e-mail, mobiele pushmeldingen en mobiele tekstberichten (SMS).
  
- ##### Hoe past / vervangt SNS in een on-premises setting?  
  Het vervangt en past de manier om notifcaties te kunnen krijgen die vanuit andere applicaties/protocols komen. Waardoor je meer ondersteuen kan krijgen dan on-premises instellingen.
  
- ##### Hoe kan ik SNS combineren met andere diensten?  
  Je kan de volgende diensten van AWS combineren of andere:  
  1) Amazon SQS
  2) AWS Lambda
  3) Amazon Kinesis Data FileHouse
  4) SMS
  5) Mobile Push
  6) Email
  ![resultaat](/00_includes/AWS-13a-resultaat58.png "resultaat")
- ##### Wat is het verschil tussen SNS en andere gelijksoortige diensten?  
  Ja, er zijn wat verschillen zoals wat ze ondersteunen.
  1) Azure Service Bus
  2) Google Cloud Pub/Sub
  

#### Vragen voor praktisch onderzoek:
- ##### Waar kan ik deze dienst vinden in de console?  
- ##### Hoe zet ik deze dienst aan?  
- ##### Hoe kan ik deze dienst koppelen aan andere resources?   
  Zie de opdrachten onderaan:

#### [SQS](https://aws.amazon.com/sqs/)  
Amazon Simple Queue Service (SQS) lets you send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.
![resultaat](/00_includes/AWS-13a-resultaat32.png "resultaat")
#### Vragen voor theoretisch onderzoek:
- ##### Waar is [Simple Queue Service (SQS)](https://aws.amazon.com/sqs/)[1](https://aws.amazon.com/sqs/) voor?  
  Het is een volledig beheerde wachtrijservice voor berichten die het mogelijk maakt om gedistribueerde softwarecomponenten te ontkoppelen en te verbinden met behulp van wachtrijen. Het biedt een veilige, duurzame en beschikbare gehoste wachtrij.
  
- ##### Hoe past / vervangt Simple Queue Service (SQS) in een on-premises setting?  
  Geen, er zijn geen on-premises setting die al bestond ervoor.
  
- ##### Hoe kan ik Simple Queue Service (SQS) combineren met andere diensten?  
   Je kan de volgende diensten van AWS combineren of andere:  
  1) Amazon Redshift,
  2) Amazon DynamoDB 
  3) Amazon Relational Database Service (RDS) 
  4) Amazon Elastic Compute Cloud (EC2)
  5) Amazon Elastic Container Service (ECS)
  6) AWS Lambda 
  7) Amazon S3
  8) Frontend-applicatie naar een backend-service te sturen
  
- ##### Wat is het verschil tussen Simple Queue Service (SQS) en andere gelijksoortige diensten?  
  Ja, er zijn wat verschillen zoals wat ze ondersteunen.
  1) Azure Service Bus
  2) Google Cloud Pub/Sub
  

#### Vragen voor praktisch onderzoek:
- ##### Waar kan ik deze dienst vinden in de console?  
- ##### Hoe zet ik deze dienst aan?  
- ##### Hoe kan ik deze dienst koppelen aan andere resources?   
  Zie de opdrachten onderaan:


### [Event Bridge](https://aws.amazon.com/eventbridge/)  
Amazon Event Bridge Event Bus is a serverless event bus that helps you receive, filter, transform, route, and deliver events.
![resultaat](/00_includes/AWS-13a-resultaat33.png "resultaat")
### Use Case  
#### 1) Increase developer agility  
Remove the need to coordinate across service teams with decoupled microservices using AWS, SaaS apps, or your own custom apps.  

#### 2) Monitor and audit applications  
Monitor and audit your AWS environments, and respond to operational changes in your applications in real time to prevent infrastructure vulnerabilities.

#### 3) Extend functionality with SaaS integrations  
Connect your applications to other SaaS applications by sending a custom event to EventBridge, and then send it through API Destinations to Zendesk CRM.  

#### 4) Scheduling in your Applications  
Use EventBridge Scheduler in your applications and platforms to provide scheduling services to your customers with reminders, delayed actions, or prompts to continue where they left off.

#### Vragen voor theoretisch onderzoek:
- ##### Waar is [Event Bridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) voor?  
  Het is een serverloze service die gebeurtenissen gebruikt om applicatiecomponenten met elkaar te verbinden, waardoor het gemakkelijker wordt om schaalbare op gebeurtenissen gebaseerde applicaties te bouwen. Je kunt het gebruiken om gebeurtenissen te routeren van bronnen zoals zelfgemaakte applicaties, AWS-services en software van derden naar consumentenapplicaties binnen je organisatie.
  
  Een event bus is een pijplijn die gebeurtenissen ontvangt. Regels die aan de event bus zijn gekoppeld, evalueren gebeurtenissen naarmate ze binnenkomen. Elke regel controleert of een gebeurtenis overeenkomt met de criteria van de regel. Je koppelt een regel aan een specifieke event bus, zodat de regel alleen van toepassing is op gebeurtenissen die door die event bus worden ontvangen.
  
- ##### Hoe past / vervangt Event Bridge in een [on-premises](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-saas.html) [setting](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-saas.html#eb-supported-integrations)?  
  Het wordt toegepast op de SaaS partners zoals:
  1) Auth0
  2) Karte
  3) Zendesk
  
- ##### Hoe kan ik Event Bridge combineren met andere diensten?  
  Je kan de volgende diensten van AWS combineren of andere:  
  1) Amazon SQS
  2) AWS CloudWatch
  3) SaaS Partners
  
- ##### Wat is het [verschil](https://vunvulearadu.blogspot.com/2019/08/the-value-proposition-of-aws.html) tussen Event Bridge en andere gelijksoortige diensten?  
  Ja, Microsoft heeft ook een soortgelijke versie ervan die heet Azure Event Grid. Een van de grootste verschil is dat bij Azure Event Grid wel mogelike is voor externe partners om het te gebruiken maar Azure focus zich er niet op terwijl AWS het wel doet.

#### Vragen voor praktisch onderzoek:
- ##### Waar kan ik deze dienst vinden in de console?  
- ##### Hoe zet ik deze dienst aan?  
- ##### Hoe kan ik deze dienst koppelen aan andere resources?   
  Zie de opdrachten onderaan:



## Opdracht

### Look around IAM 

https://us-east-1.console.aws.amazon.com/iamv2/home?region=eu-central-1#/home

Normaal gesproken wanneer je volledige nieuwe account aan maakt ben je de Root user van je eigen omgeving, maar je kan worden toegevoegt aan iemand anders. Hierbij krijg je toegang tot bepaalde toestemmingen die je zelf kan verrichten.

We gaan een nieuwe gebruiker maken:
https://us-east-1.console.aws.amazon.com/iamv2/home?region=eu-central-1#/users

Vul in 'new-techground-student-cloud11-one' en druk op 'Next'
![resultaat](/00_includes/AWS-13a-resultaat34.png "resultaat")

Je kan kiezen welke 'toestemmingen' ze kunnen krijgen.
- **Add user to group:** moeten we nog een aanmaken, let op dat het gaat om group waar je toegang tot hebt anders konden we zomaar mensen toevoegen op 'Cloud 10' die door Casper wordt beheerd.
- **Copy permissions:** Je kopieert de instellingen van een andere gebruiker over naar deze.
- **Attach Policies Directly:** Je gaat ze zelf af en geeft aan welke toestemmingen ze kunnen krijgen. (Ik zal het zelf niet echt aanraden omdat je anders te maken krijgt met micromanagement van elke gebruiker. Daarom is group als eerste optie!) 
![resultaat](/00_includes/AWS-13a-resultaat35.png "resultaat")

Druk op 'Çreate group' dan
Bij 'User group name' = 'IAM-Group-Test'
Voor nu laten we de 'Permissions policies' leeg staan en drukken we op 'Create user group'
![resultaat](/00_includes/AWS-13a-resultaat36.png "resultaat")
Selecteer de 'IAM-Group-Test' en druk vervolgens op 'Next'

Controleer de gegevens en dan op 'Create user'
![resultaat](/00_includes/AWS-13a-resultaat37.png "resultaat")

Bij elke AWS services wordt gegeken naar de 'Permissions policies' 
voor de toestemmingen. Op zicht moet je nog wel inloggen op de gegeven account via SLI of Cloudshell (automatisch de huidige account waarme je de nieuwe account hebt aangemaakt). 

### We have used AWS Cloudwatch for our Auto Scalling earlier assigements. 
We hadden het al gebruit bij het vorige opdracht van 'AWS-11' voor het 'Auto Scalling'
![resultaat](/00_includes/AWS-13a-resultaat.png "resultaat")

We kunnen een dashboard maken op:
https://eu-central-1.console.aws.amazon.com/cloudwatch/home?region=eu-central-1#dashboards:;expand=false

Druk op 'Create dashboard'
Bij 'Dashboard-name' = 'Lab_Dashboard'
Druk op 'Create dashboard'
![resultaat](/00_includes/AWS-13a-resultaat2.png "resultaat")

Nu kan je een widget toevoegen, dus selecteer een ervan en druk op 'Next' daarna.
![resultaat](/00_includes/AWS-13a-resultaat3.png "resultaat")


### Make a notification for your email by using the SNS. You need first to create a Topic and make a Subscriptions for your email.
https://eu-central-1.console.aws.amazon.com/sns/v3/home?region=eu-central-1#/dashboard

Om te beginnen moeten we eerste een topic maken dus:
https://eu-central-1.console.aws.amazon.com/sns/v3/home?region=eu-central-1#/topics

Druk op 'Create topic' 
![resultaat](/00_includes/AWS-13a-resultaat38.png "resultaat")

Bij 'Type' = 'Standard', aangezien we het later ook nodig hebben voor 'Lambda' en niet alleen voor 'SQS'
Bij 'Name' = 'My-SNS-Message'
Bij 'Display name' = 'READ THIS!'
Druk up 'Create topic' vervolgens gelijk op 'Create subscription'
![resultaat](/00_includes/AWS-13a-resultaat39.png "resultaat")

We gaan 3 subscriptions maken (Email, SQS en Lambda!)
Bij 'Topic ARN' wordt je topic automatische geselecteerd als je bij de topic zelf zat en toen op 'Create subscription' had gedrukt.

##### Email
Bij 'Protocol' = 'Email'  
Bij 'Endpoint' = 'je eigen email'  
Druk op 'Create subscription'  
![resultaat](/00_includes/AWS-13a-resultaat40.png "resultaat")

Je krijgt email voor 'Confirm subscription' te bevestingen, nadat je dat hebt gedaan.
![resultaat](/00_includes/AWS-13a-resultaat41.png "resultaat")

##### SQS (Volg de 'SQS' opdracht eerste)
Bij 'Protocol' = 'Amazon SQS'  
Bij 'Endpoint' = 'My-SQS-Queue  
Druk op 'Create subscription'  
![resultaat](/00_includes/AWS-13a-resultaat46.png "resultaat")
*Dit is alleen voorbeeld ervan als je via SNS het zou toevoegen*

##### Lambda (Volg de 'Lambda' opdracht eerste)
Bij 'Protocol' = 'Amazon Lambda'  
Bij 'Endpoint' = 'je eigen email'  
Druk op 'Create subscription'
![resultaat](/00_includes/AWS-13a-resultaat40.png "resultaat")
*Dit is alleen voorbeeld ervan als je via SNS het zou toevoegen*

Nu heb je het aangemaakt en aangesloten bij je Email (later ook voor SQS en Lambda)!


### SQS 
https://eu-central-1.console.aws.amazon.com/sqs/v2/home?region=eu-central-1#/
Druk op 'Create queue'
![resultaat](/00_includes/AWS-13a-resultaat42.png "resultaat")

Bij 'Type' = 'Standard'  
Bij 'Name' = 'My-SQS-Queue'  
![resultaat](/00_includes/AWS-13a-resultaat43.png "resultaat")
Je kan zelf nog wat veranderen bij 'Configuration' maar we laten alles op 'Default' voor nu. Druk op 'Create queue'

We kunnen gelijk terug naar 'SNS' door 'Subscribe to Amazon SNS topic' te drukken. 
![resultaat](/00_includes/AWS-13a-resultaat44.png "resultaat")

Selecteer ons eerder aangemaakt 'SNS topic' dus 'My-SNS-Message' en druk op vervolgens 'Save'
![resultaat](/00_includes/AWS-13a-resultaat45.png "resultaat")
Nu is het aangesloten bij 'SNS'!

### Event Bridge
https://eu-central-1.console.aws.amazon.com/events/home?region=eu-central-1#/rules?redirect_from_cwe=true

We gaan een nieuwe 'Rule' maken dus druk op 'Create rule'
![resultaat](/00_includes/AWS-13a-resultaat47.png "resultaat")

Bij 'Name' = 'My-EventBridge-Rule'
Druk op 'Next'
![resultaat](/00_includes/AWS-13a-resultaat48.png "resultaat")

Bij 'Event source' = 'AWS events or EventBridge partner events'
![resultaat](/00_includes/AWS-13a-resultaat49.png "resultaat")

Bij 'Sample event type' = 'AWS events'
Bij 'Sample events' = 'AWS API Call via CloudTrail' (SQS)
![resultaat](/00_includes/AWS-13a-resultaat50.png "resultaat")
Bij 'Method' = 'Use patter form'  
Bij 'Event source' = 'AWS services'  
Bij 'AWS service' = 'Simple Notifcation SNS'  
Bij 'Event type' = 'All Events'  
Druk op 'Next'  
![resultaat](/00_includes/AWS-13a-resultaat51.png "resultaat")

Bij 'Target types' = 'AWS service'  
Bij 'Select a target' = 'SNS topic'  
Bij 'Topic' = 'My-SNS-Message'  
Druk op 'Next' 2 keer. (Tags wordt overgeslagen).
![resultaat](/00_includes/AWS-13a-resultaat52.png "resultaat")
Druk op 'Create Rule' bij de laaste stap.

Success! Je nieuwe regel is aangemaakt en aangesloten bij AWS SNS service!


![resultaat](/00_includes/AWS-13a-resultaat4.png "resultaat")
*Bij Cloudwatch*

### Create a table using DynamoDB

Ga naar de link:
https://eu-central-1.console.aws.amazon.com/dynamodbv2/home?region=eu-central-1#service

Druk op 'Create table'
![resultaat](/00_includes/AWS-13a-resultaat7.png "resultaat")

Bij 'Table name' = 'Techgrounds'
Bij 'Partition key' = 'userID'
![resultaat](/00_includes/AWS-13a-resultaat5.png "resultaat")

A) Als 'Default settings' wordt het rest ingevuld voor je, waarbij je ziet wat die zijn daarna op 'Create Table' drukken.
![resultaat](/00_includes/AWS-13a-resultaat6.png "resultaat")

B) Als 'Customize settings' ga je zelf verder invullen of wijziging waar het nodig is.

Bij 'Table class' = 'DynamoDB Standard'
![resultaat](/00_includes/AWS-13a-resultaat8.png "resultaat")

Bij 'Capacity calculator' is het gewoon om te kijken wat je verwacht kosten zou zijn.

Bij 'Read/write capacity settings' = 'Provisioned'
Bij 'Read capacity' = 'Auto-scaling: on, min:1, max: 10, targe:70'
Bij 'Write capacity' = 'Auto-scaling: on, min:1, max: 10, targe:70'
![resultaat](/00_includes/AWS-13a-resultaat9.png "resultaat")

Bij 'Secondary indexes' kan je het leeg laten.
Bij '## Estimated read/write capacity cost' staat **verwachte** kosten.

Bij 'Encryption at rest' = 'Owned by Amazon DynamoDB' 
![resultaat](/00_includes/AWS-13a-resultaat10.png "resultaat")
Als laaste druk je op 'Create table'

De table is aangemaakt:
![resultaat](/00_includes/AWS-13a-resultaat11.png "resultaat")


### Create a hello world function in AWS Lambda
https://eu-central-1.console.aws.amazon.com/lambda/home?region=eu-central-1#/begin

Begin met 'Create a function'
![resultaat](/00_includes/AWS-13a-resultaat12.png "resultaat")

Selecteer 'Author from scratch'
Bij 'Function name' = 'HelloWorldFunction'
Bij 'Architecture' = 'x86_64'
![resultaat](/00_includes/AWS-13a-resultaat13.png "resultaat")
Dan druk je op 'Create function'

Na het maken kom je direct op de dashboard van je functie.
Er zitten nog opties er tussen waarmee je 'trigger' en 'destination' kan toevoegen. 
Trigger = Soure, waar het moet vandaan komen om deze functie te kunnen activeren
Destination = Bestemming, na het activeren van deze functie en informatie versturen ervan.
![resultaat](/00_includes/AWS-13a-resultaat14.png "resultaat")

Voor 'Add trigger' heb je opties die je kan kiezen tussen AWS of 'Partner event sources' 
![resultaat](/00_includes/AWS-13a-resultaat15.png "resultaat")

Als je een 'Partner event sources' zou kiezen dan wordt er ook een Amazon Eventbridge aangemaakt voor je.
![resultaat](/00_includes/AWS-13a-resultaat16.png "resultaat")

Voor 'Add destination' heb je weer andere opties.
Bij 'Source' = 'Asynchronous invocation'
Bij 'Condition' = 'On success'
Bij 'Destination type' = 'SNS topic'
Bij 'Destination' = '(je aangemaakt SNS)'
![resultaat](/00_includes/AWS-13a-resultaat17.png "resultaat")
Dan druk je op 'Save'

*Je hebt deze andere opties voor 'Destination type'*
![resultaat](/00_includes/AWS-13a-resultaat18.png "resultaat")

Nu staat 'Amazon SNS' op de lijst.
![resultaat](/00_includes/AWS-13a-resultaat19.png "resultaat")

We kunnen onze code testen door:
Seleecteer 'Test'
Bij 'Test event action' = 'Create new event'
Bij 'Event name' = 'HalloWorld'
Bij 'Event sharing settings' = 'Private'
Bij 'Template - _optional_' en 'Event JSON' laat je default staan voor nu
Nu druk je op 'Test'
![resultaat](/00_includes/AWS-13a-resultaat20.png "resultaat")

Je ziet dat de code  'Execution result: succeeded' en geslaagd is.
![resultaat](/00_includes/AWS-13a-resultaat20.png "resultaat")



### Gebruikte bronnen

https://docs.aws.amazon.com/aws-support/index.html
https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html
https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html

https://aws.amazon.com/ecs/
https://aws.amazon.com/config/
https://aws.amazon.com/cloudtrail/
https://aws.amazon.com/iam/
https://aws.amazon.com/cloudwatch/
https://aws.amazon.com/dynamodb/
https://aws.amazon.com/lambda/
https://aws.amazon.com/sns/
https://aws.amazon.com/sqs/
https://aws.amazon.com/eventbridge/

### Ervaren problemen
Veel theory ervan vinden en deeper erin duiken hoe het inelkaar zit.

### Resultaat
Weten hoe de AWS services werken en hoe sommige met elkaar vervonden zijn voor het verwerken van de juiste gegevens. Weten hoe andere AWS services werken namelijke: ECS, Support Plan, Trusted Advisor, Config, Cloud Trial, IAM, Cloudwatch, DYnamoDB, Lambda, SNS, SQS en Event Bridges.