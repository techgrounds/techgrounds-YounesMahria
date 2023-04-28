# AWS-07 Elastic Block Store (EBS)
Weten hoe EBS/Elastic Block Store werkt.

## Key-terms

### EBS / Elastic Block Store  
Zijn​​ virtuele harde schijven in de cloud. 
1) Root volumes (zoals interne harde schrijven) die kunnen alleen bij een EC2 instantie worden aangesloten.
2) Aparte volumes (zoals externe harde schrijven) die kunnen los gemaakt of aangesloten worden bij verschillende EC2 instantie. Je kan alleen met 'Provisioned IOPS SSD (io1 and io2)' volume op meerdere EC2 instantie (EBS Multi-Attach) aansluiten.

Ze zijn ook opgesplits in twee verschillende categorieën.
1) SDD-backed storage: Voor transactionele workloads zoals database, virtuele desktops en boot volumes.
2) HDD-backed storage: Voor verwerken van intensieve workloads, zoals MapReduce en logboekverwerking.
![resultaat](/00_includes/AWS-07-resultaat.png "resultaat")

## Opdracht  

We beginnen op https://aws.amazon.com/ebs/
![resultaat](/00_includes/AWS-07-resultaat2.png "resultaat")


### Exercise 1:  
#### Navigate to the EC2 menu.
We beginnen op https://aws.amazon.com/ec2/ en vervolgens op 'Get started with Amazon EC2'
![resultaat](/00_includes/AWS-06-resultaat2.png "resultaat")


#### Create a t2.micro Amazon Linux 2 machine with all the default settings.  
Zelfde instellingen als bij EC2 maar je kan ook een nieuwe EBS maken tijdens het maken van EC2 maar als gewoon gelijke een nieuwe EBS wilt aanmaken verloopt het anders.

![resultaat](/00_includes/AWS-07-resultaat3.png "resultaat")

#### Create a new EBS volume with the following requirements:  
- Volume type: General Purpose SSD (gp3)  
- Size: 1 GiB
- Availability Zone: same as your EC2

Om alleen nieuwe EBS maken. 
Aan de linkerkant van je menu scroll je naar beneden totdat je bij 'Elastic Block Store' komt en vervolgens op 'Volumes' drukken.
![resultaat](/00_includes/AWS-07-resultaat4.png "resultaat")

Nu druk je op 'Create volume' om een nieuwe EBS te maken.
![resultaat](/00_includes/AWS-07-resultaat5.png "resultaat")

Vul de gegevens in bij elke veld en druk op 'Create volume'
![resultaat](/00_includes/AWS-07-resultaat6.png "resultaat")

#### Wait for its state to be available.  
Verder naar rechts scrollen totdat je het ziet.
![resultaat](/00_includes/AWS-07-resultaat7.png "resultaat")
*In dit geval heb ik 3 gemaakt in plaats van 1.*

### Exercise 2:  
#### Attach your new EBS volume to your EC2 instance.  
Selecteer de volume in dit geval is het 'vol-01786c2e9aaa3aa2b' dan naar 'Actions > Attach volume' gaan.
![resultaat](/00_includes/AWS-07-resultaat8.png "resultaat")

We gaan de 'Instance' selecteren en dan op 'Attach Volume'
![resultaat](/00_includes/AWS-07-resultaat9.png "resultaat")

#### Connect to your EC2 instance using SSH.  
**Powershell**
Nu de powershell open maken van windows, naar onze map nagiveren en vervolgens de ssh verbinding maken.

```
cd C:\Users\TechGrounds\Desktop\Cloud\AWS
```

```
ssh -i "younestgaws.pem" ec2-user@ec2-18-194-208-72.eu-central-1.compute.amazonaws.com
```

Als alles goed werkt krijgt ik nu de welcome scherm van 'Amazon Linux 2 AMI'
![resultaat](/00_includes/AWS-07-resultaat10.png "resultaat")

#### Mount the EBS volume on your instance.  
We gaan kijken welke volume we al hebben met de volgende code:
```
sudo lsblk -f
```

Checked of er een file systeem er in zit:
```
sudo file -s /dev/xvdf
```

Dit keer is er geen filesystem:
![resultaat](/00_includes/AWS-07-resultaat21.png "resultaat")

We kunnen het formateren met:
```
sudo mkfs -t ext4 /dev/xvdf
sudo mkfs -t xfs /dev/xvdf
```

Een nieuwe folder maken:
```
sudo mkdir /data
```

Het mounten op de volume:
```
sudo mount /dev/xvdf /data
```

In de volume komen:
```
cd /data
```

Bevestigen dat we ook erin zitten:
```
df -h .
```

![resultaat](/00_includes/AWS-07-resultaat11.png "resultaat")

#### Create a text file and write it to the mounted EBS volume.  

We gaan nu een text maken in de mounted EBS volume:
```
echo "techgrounds" >> test.txt
```

![resultaat](/00_includes/AWS-07-resultaat12.png "resultaat")

Geen toestemming? Dat kan je snel oplossen door dit doen.
```
cd ..
sudo chown `whoami` /data/
cd data/
echo "techgrounds" >> test.txt
ls -l
```

![resultaat](/00_includes/AWS-07-resultaat13.png "resultaat")
De file is aangemaakt!

----
**Voor het auto-mounten:**

Ga uit 'newvolume'
```
cd ..
```

Maak een backup eerste:
```
sudo cp /etc/fstab /etc/fstab.bak
```

Open maken met nano:
```
sudo nano /etc/fstab
```

Deze codelijn toevoegen en daarna "ctrl+s" en "ctrl+x":
```
/dev/xvdf /data ext4 defaults,nofail 0 0
```

Als laaste deze code doen:
```
sudo mount -a
```


----

### Exercise 3:  
#### Create a snapshot of your EBS volume.  
Terug bij EBS dashboard.  
Selecteer de juiste 'Volume' daarna 'Actions > Snapshot'
![resultaat](/00_includes/AWS-07-resultaat14.png "resultaat")

Bij 'Description' gaan je een eigen omschrijving invullen en op 'create snapshot' drukken.
![resultaat](/00_includes/AWS-07-resultaat15.png "resultaat")

#### Remove the text file from your original EBS volume.  
Terug op onze Powershell.  
De 'test.txt' bestand verwijderen:
```
rm test.txt
```

#### Create a new volume using your snapshot.  
Terug bij EBS dashboard.  
Bij de linkerkant van het menu ga je dit keer 'Snapshots' selecteren.
![resultaat](/00_includes/AWS-07-resultaat16.png "resultaat")

Selecteer de 'Snapshot ID' en in dit geval is het 'snap-0def853ec10999cf7' en daarna 'Actions > Create volume from snapshot'.
![resultaat](/00_includes/AWS-07-resultaat17.png "resultaat")

Je ziet dit keer de 'Snapshot ID' bovenaan staan. Zelfde stappen als vorige keer:
![resultaat](/00_includes/AWS-07-resultaat18.png "resultaat")

#### Detach your original EBS volume.   
Terug bij Powershell.  
Voor het umount:
```
sudo umount /dev/xvdf
```
![resultaat](/00_includes/AWS-07-resultaat23.png "resultaat")

Terug bij EBS dashboard.  
Als op je volume bent dan 'Actions > Detach volume'
![resultaat](/00_includes/AWS-07-resultaat19.png "resultaat")

#### Attach the new volume to your EC2 and mount it.   
Bij 'Actions > Attach volume'
![resultaat](/00_includes/AWS-07-resultaat20.png "resultaat")

We gaan kijken welke volume we al hebben met de volgende code:
```
sudo lsblk -f
```

Checked of er een file systeem er in zit:
```
sudo file -s /dev/xvdg
```

Dit keer is er wel een filesystem:
![resultaat](/00_includes/AWS-07-resultaat22.png "resultaat")

Het mounten op de volume:
```
sudo mount /dev/xvdg /data
```

In de volume komen:
```
cd /data
```

Bevestigen dat we ook erin zitten:
```
df -h .
```

#### Find your text file on the new EBS volume.  

```
ls -l
```
![resultaat](/00_includes/AWS-07-resultaat23.png "resultaat")

### Gebruikte bronnen
https://aws.amazon.com/ebs/
https://aws.amazon.com/ebs/volume-types/
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes-multi.html
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html
https://devopscube.com/mount-ebs-volume-ec2-instance/
https://tldp.org/LDP/intro-linux/html/sect_03_04.html

### Ervaren problemen
Onverwachtse resultaten of errors met  bijkomende extra stappen die ik nodig had om het te kunnen oplossen maar die vond ik wel snel genoeg of ik deed er niet te moelijke over als ik alternative oplossing vond.

### Resultaat
Weten hoe een EBS werkt samen met EC2. Namelijke door volumes attach en detach op instances. Bij ternimal/powershell de volumes  mount en unmount ervan. Snapsnots(backups) maken van volumes en die weer herstellen als nieuwe volumes.
