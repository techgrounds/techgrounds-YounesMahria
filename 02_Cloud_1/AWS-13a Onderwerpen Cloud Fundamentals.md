# Onderwerpen Cloud Fundamentals
Vertellen hoe andere AWS services werken namelijke: ECS, Support Plan, Trusted Advisor, Config, Cloud Trial, IAM, Cloudwatch, DYnamoDB, Lambda, SNS, SQS en Event Bridges.

----
Het detail wat je moet weten voor het examen is alleen niet zo hoog als je hiervoor met de behandelende diensten heb gedaan.

Vragen die je kan stellen over nieuwe diensten die je tegen komt:
- Waar is X voor?
- Waar wordt X voor gebruikt?

Zoals je kan zien is dit lijstje stukken korter dan wat wij hiervoor hebben behandeld.

Hier zijn nogmaals de lijstjes vragen voor je onderzoek:
Vragen voor theoretisch onderzoek:
- Waar is X voor?
- Hoe past X / vervangt X in een on-premises setting?
- Hoe kan ik X combineren met andere diensten?
- Wat is het verschil tussen X en andere gelijksoortige diensten?

Vragen voor praktisch onderzoek:
- Waar kan ik deze dienst vinden in de console?
- Hoe zet ik deze dienst aan?
- Hoe kan ik deze dienst koppelen aan andere resources?
----

## Key-terms


### [ECS](https://aws.amazon.com/ecs/) 
Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the Amazon Web Services (AWS) Cloud. Using Amazon EC2 eliminates your need to invest in hardware up front, so you can develop and deploy applications faster. You can use Amazon EC2 to launch as many or as few virtual servers as you need, configure security and networking, and manage storage. Amazon EC2 enables you to scale up or down to handle changes in requirements or spikes in popularity, reducing your need to forecast traffic.


### [AWS Support Plans](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)
AWS Support offers five support plans:

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


### [Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)
Trusted Advisor draws upon best practices learned from serving hundreds of thousands of AWS customers. Trusted Advisor inspects your AWS environment, and then makes recommendations when opportunities exist to save money, improve system availability and performance, or help close security gaps.

1) If you have a Basic or Developer Support plan, you can use the Trusted Advisor console to access all checks in the Service Limits category and six checks in the Security category.
2) If you have a Business, Enterprise On-Ramp, or Enterprise Support plan, you can use the Trusted Advisor console and the [AWS Support API](https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html) to access all Trusted Advisor checks. You also can use Amazon CloudWatch Events to monitor the status of Trusted Advisor checks. For more information, see [Monitoring AWS Trusted Advisor check results with Amazon EventBridge](https://docs.aws.amazon.com/awssupport/latest/user/cloudwatch-events-ta.html).

You can access Trusted Advisor in the AWS Management Console. For more information about controlling access to the Trusted Advisor console, see [Manage access to AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html).


### [AWS Config](https://aws.amazon.com/config/) 
AWS Config continually assesses, audits, and evaluates the configurations and relationships of your resources on AWS, on premises, and on other clouds.


### [AWS Cloud Trail](https://aws.amazon.com/cloudtrail/)
AWS CloudTrail monitors and records account activity across your AWS infrastructure, giving you control over storage, analysis, and remediation actions.


### [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)
With AWS Identity and Access Management (IAM), you can specify who or what can access services and resources in AWS, centrally manage fine-grained permissions, and analyze access to refine permissions across AWS.


### [AWS Cloudwatch](https://aws.amazon.com/cloudwatch/)
Amazon CloudWatch collects and visualizes real-time logs, metrics, and event data in automated dashboards to streamline your infrastructure and application maintenance.


### [DynamoDB](https://aws.amazon.com/dynamodb/)
Amazon DynamoDB is a fully managed, serverless, key-value NoSQL database designed to run high-performance applications at any scale. DynamoDB offers built-in security, continuous backups, automated multi-Region replication, in-memory caching, and data import and export tools.


### [AWS Lambda](https://aws.amazon.com/lambda/)
AWS Lambda is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers. You can trigger Lambda from over 200 AWS services and software as a service (SaaS) applications, and only pay for what you use.


### [SNS](https://aws.amazon.com/sns/)  
Amazon Simple Notification Service (SNS) sends notifications two ways, A2A and A2P. A2A provides high-throughput, push-based, many-to-many messaging between distributed systems, microservices, and event-driven serverless applications. These applications include Amazon Simple Queue Service (SQS), Amazon Kinesis Data Firehose, AWS Lambda, and other HTTPS endpoints. A2P functionality lets you send messages to your customers with SMS texts, push notifications, and email.


#### [SQS](https://aws.amazon.com/sqs/)  
Amazon Simple Queue Service (SQS) lets you send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.


### [Event Bridge (Use cases)](https://aws.amazon.com/eventbridge/)  
Amazon EventBridge Event Bus is a serverless event bus that helps you receive, filter, transform, route, and deliver events.

#### 1) Increase developer agility

Remove the need to coordinate across service teams with decoupled microservices using AWS, SaaS apps, or your own custom apps.  

#### 2) Monitor and audit applications

Monitor and audit your AWS environments, and respond to operational changes in your applications in real time to prevent infrastructure vulnerabilities.

#### 3) Extend functionality with SaaS integrations

Connect your applications to other SaaS applications by sending a custom event to EventBridge, and then send it through API Destinations to Zendesk CRM.  

#### 4) Scheduling in your Applications

Use EventBridge Scheduler in your applications and platforms to provide scheduling services to your customers with reminders, delayed actions, or prompts to continue where they left off.

## Opdracht

### Gebruik IAM


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


### SNS
https://eu-central-1.console.aws.amazon.com/sns/v3/home?region=eu-central-1#/dashboard
Hier krijg je een 


### SQS 
https://eu-central-1.console.aws.amazon.com/sqs/v2/home?region=eu-central-1#/



### Event Bridge
https://eu-central-1.console.aws.amazon.com/events/home?region=eu-central-1#/rules?redirect_from_cwe=true
![resultaat](/00_includes/AWS-13a-resultaat4.png "resultaat")
*Bij Cloudwatch*


### Gebruik DynamoDB
https://eu-central-1.console.aws.amazon.com/dynamodbv2/home?region=eu-central-1#service


### Gebruik AWS Lambda
https://eu-central-1.console.aws.amazon.com/lambda/home?region=eu-central-1#/begin





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