# AWS-04 Core Services
Een gids en samenvatting welke kennissen je nodig hebt voor het behalen van de AWS Cloud Practitioner certification.

## Key-terms / (Zelf) Opdracht

Er zullen veel termen voorbij komen wat ik moet nog gaan leren aankomende weken. Bij elke term zou ik het verwijzen naar het opdracht zelf indien nodig is.

Op 25 April 2023 stond dit als een samenvatting voor de exam. Je moet 70% scoren om te kunnen slagen.
![resultaat](/00_includes/AWS-04-resultaat.png "resultaat")

In het kort geven ze dit aan:
**Recommended AWS knowledge**  
The target candidate should have the following knowledge:  
1) AWS Cloud concepts  
2) Security and compliance within the AWS Cloud  
3) Understanding of the core AWS services  
4) Understanding of the economics of the AWS Cloud  

**These items are considered out of scope for the exam:**  
1) Coding  
2) Designing cloud architecture  
3) Troubleshooting  
4) Implementation  
5) Migration  
6) Load and performance testing  
7) Business applications (for example, Amazon Alexa, Amazon Chime, Amazon WorkMail


Op de pdf bestand staat er dit:
> The following is a non-exhaustive list of the tools and technologies that **could appear** on the exam. 
> 
> This list is **subject to change** and is **provided to help you understand the general scope of services, features, or technologies on the exam**. 
> 
> The general tools and technologies in this list appear in no particular order. AWS services are grouped according to their primary functions. While some of these technologies will likely be covered more than others on the exam, the order and placement of them in this list are no indication of....  

### Relative weight or importance:  
1) [APIs](../00_Examen/EXA-XX%20API.md) 
2) [Cost Explorer](../00_Examen/EXA-XX%20Blank.md) 
3) [AWS Cost and Usage Report](../00_Examen/EXA-XX%20Blank.md) 
4) [AWS Command Line Interface (CLI)](../00_Examen/EXA-XX%20CLI.md) +
5) [Elastic Load Balancers](../00_Examen/EXA-XX%20ELB.md) +
6) [Amazon EC2 instance types (for example, Reserved, On-Demand, Spot)](../00_Examen/EXA-XX%20Blank.md) 
7) [AWS global infrastructure (for example, AWS Regions, Availability Zones)](../00_Examen/EXA-XX%20AWS%20Global%20Infrastructure.md) 
8) [Infrastructure as Code (IaC)](../00_Examen/EXA-XX%20Blank.md) 
9) [Amazon Machine Images (AMIs)](../00_Examen/EXA-XX%20Blank.md) 
10) [AWS Management Console](../00_Examen/EXA-XX%20Blank.md) 
11) [AWS Marketplace](../00_Examen/EXA-XX%20Blank.md) 
12) [AWS Professional Services](../00_Examen/EXA-XX%20Blank.md) 
13) [AWS Personal Health Dashboard](../00_Examen/EXA-XX%20Blank.md) 
14) [Security groups](../00_Examen/EXA-XX%20Blank.md) 
15) [AWS Service Catalog](../00_Examen/EXA-XX%20Blank.md) 
16) [AWS Service Health Dashboard](../00_Examen/EXA-XX%20Blank.md) 
17) [Service quotas](../00_Examen/EXA-XX%20Blank.md) 
18) [AWS software development kits (SDKs)](../00_Examen/EXA-XX%20Blank.md) 
19) [AWS Support Center](../00_Examen/EXA-XX%20Support%20Plan.md) +
20) [AWS Support tiers](../00_Examen/EXA-XX%20Support%20Plan.md) +
21) [Virtual private networks (VPNs)](../00_Examen/EXA-XX%20Blank.md) 

### AWS services and features 
1) **Analytics:**  
	1) [Amazon Athena](../00_Examen/EXA-XX%20Blank.md) 
	2) [Amazon Kinesis](../00_Examen/EXA-XX%20Blank.md) 
	3) [Amazon QuickSight](../00_Examen/EXA-XX%20Blank.md) 
2) **Application Integration:**  
	1) [Amazon Simple Notification Service (Amazon SNS)](../00_Examen/EXA-XX%20SNS.md) +
	2) [Amazon Simple Queue Service (Amazon SQS)](../00_Examen/EXA-XX%20SQS.md) +
3) **Compute and Serverless:**  
	1) [AWS Batch](../00_Examen/EXA-XX%20Blank.md) 
	2) [Amazon EC2](../00_Examen/EXA-XX%20Blank.md) 
	3) [AWS Elastic Beanstalk](../00_Examen/EXA-XX%20Elastic%20Beanstalk.md) +
	4) [AWS Lambda](../00_Examen/EXA-XX%20Lambda.md) +
	5) [Amazon Lightsail](../00_Examen/EXA-XX%20Blank.md) 
	6) [Amazon WorkSpaces](../00_Examen/EXA-XX%20Blank.md) 
4) **Containers:**  
	1) [Amazon Elastic Container Service (Amazon ECS)](../00_Examen/EXA-XX%20Blank.md) 
	2) [Amazon Elastic Kubernetes Service (Amazon EKS)](../00_Examen/EXA-XX%20Blank.md) 
	3) [AWS Fargate](../00_Examen/EXA-XX%20Blank.md) 
5) **Database:**  
	1) [Amazon Aurora](../00_Examen/EXA-XX%20Aurora.md) +
	2) [Amazon DynamoDB](../00_Examen/EXA-XX%20DynamoDB.md) +
	3) [Amazon ElastiCache](../00_Examen/EXA-XX%20Blank.md) 
	4) [Amazon RDS](../00_Examen/EXA-XX%20RDS.md) +
	5) [Amazon Redshift](../00_Examen/EXA-XX%20Blank.md) 
6) **Developer Tools:**  
	1) [AWS CodeBuild](../00_Examen/EXA-XX%20Blank.md) 
	2) [AWS CodeCommit](../00_Examen/EXA-XX%20Blank.md) 
	3) [AWS CodeDeploy](../00_Examen/EXA-XX%20Blank.md) 
	4) [AWS CodePipeline](../00_Examen/EXA-XX%20Blank.md) 
	5) [AWS CodeStar](../00_Examen/EXA-XX%20Blank.md) 
7) **Customer Engagement:**  
	1) [Amazon Connect](../00_Examen/EXA-XX%20Blank.md) 
8) **Management, Monitoring, and Governance:**  
	1) [AWS Auto Scaling](../00_Examen/EXA-XX%20Blank.md) 
	2) [AWS Budgets](../00_Examen/EXA-XX%20Blank.md) 
	3) [AWS CloudFormation](../00_Examen/EXA-XX%20Blank.md) 
	4) [AWS CloudTrail](../00_Examen/EXA-XX%20CloudTrail.md) +
	5) [Amazon CloudWatch](../00_Examen/EXA-XX%20CloudWatch.md) +
	6) [AWS Config](../00_Examen/EXA-XX%20Config.md) +
	7) [AWS Cost and Usage Report](../00_Examen/EXA-XX%20Blank.md) 
	8) [Amazon EventBridge (Amazon CloudWatch Events)](../00_Examen/EXA-XX%20EventBridge.md) +
	9) [AWS License Manager](../00_Examen/EXA-XX%20Blank.md) 
9) AWS Managed Services 
	11) [AWS Organizations](../00_Examen/EXA-XX%20Blank.md) 
	12) [AWS Secrets Manager](../00_Examen/EXA-XX%20Blank.md) 
	13) [AWS Systems Manager](../00_Examen/EXA-XX%20Blank.md) 
	14) [AWS Systems Manager Parameter Store](../00_Examen/EXA-XX%20Blank.md) 
	15) [AWS Trusted Advisor](../00_Examen/EXA-XX%20Trusted%20Advisor.md) +
10) **Networking and Content Delivery:**  
	1) [Amazon API Gateway](../00_Examen/EXA-XX%20Blank.md) 
	2) [Amazon CloudFront](../00_Examen/EXA-XX%20Blank.md) 
	3) [AWS Direct Connect](../00_Examen/EXA-XX%20Blank.md) 
	4) [Amazon Route 53](../00_Examen/EXA-XX%20Blank.md) 
	5) [Amazon VPC](../00_Examen/EXA-XX%20Blank.md) 
11) **Security, Identity, and Compliance:**  
	1) [AWS Artifact](../00_Examen/EXA-XX%20Blank.md) 
	2) [AWS Certificate Manager (ACM)](../00_Examen/EXA-XX%20Blank.md) 
	3) [AWS CloudHSM](../00_Examen/EXA-XX%20Blank.md) 
	4) [Amazon Cognito](../00_Examen/EXA-XX%20Blank.md) 
	5) [Amazon Detective](../00_Examen/EXA-XX%20Blank.md) 
	6) [Amazon GuardDuty](../00_Examen/EXA-XX%20Blank.md) 
	7) [AWS Identity and Access Management (IAM)](../00_Examen/EXA-XX%20IAM.md) +
	8) [Amazon Inspector](../00_Examen/EXA-XX%20Blank.md) 
	9) [AWS License Manager](../00_Examen/EXA-XX%20Blank.md) 
	10) [Amazon Macie](../00_Examen/EXA-XX%20Blank.md) 
	11) [AWS Shield](../00_Examen/EXA-XX%20Blank.md) 
	12) [AWS WAF](../00_Examen/EXA-XX%20Blank.md) 
12) **Storage:**  
	1) [AWS Backup](../00_Examen/EXA-XX%20Blank.md) 
	2) [Amazon Elastic Block Store (Amazon EBS)](../00_Examen/EXA-XX%20EBS.md) 
	3) [Amazon Elastic File System (Amazon EFS)](../00_Examen/EXA-XX%20EFS.md) +
	4) [Amazon S3](../00_Examen/EXA-XX%20Blank.md) 
	5) [Amazon S3 Glacier](../00_Examen/EXA-XX%20Blank.md) 
	6) [AWS Snowball Edge](../00_Examen/EXA-XX%20Blank.md) 
	7) [AWS Storage Gateway](../00Examen/EXA-XX%20Blank.md) 

### Gebruikte bronnen
https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf

### Ervaren problemen
Geen

### Resultaat
Een samenvatting gids gemaakt voor de exam als referenties voor het voorbreiden van de exam. Deze zal aankomende week aangepast worden. De algemene informaties zet ik bij 'EXA-00 Examen voorbereidingen' die andere informatie zullen bevatten.