# LNX-08 Cron jobs  
Het toevoegen van taken die je crontab zet.

## Key-terms

### **Cron Jobs**  
Een Linux taken schema die script moet gaan uitvoeren op specifieke tijden en dagen.

### **Crontab**    
Het beheren van de takenschemas waarbij je aangeeft de tijden en dagen, opties en verwijzen naar de script path.  

### tail
Het volgt en laat live updates zien op de geselecteerde file die je aangeeft. Zo kun je beter zien wanneer de output veranderd.

## Opdracht

### Create a Bash script that writes the current date and time to a file in your home directory.  

De script om de huidige tijd te kunnen krijgen
```
cat <<"EOF"> CurrentDaT.sh  
#!/bin/bash  
echo $(date +"%D %T") >> /home/younes/scripts/CurrentDaTOutput.txt  
EOF
```

### Register the script in your crontab so that it runs every minute.    

De paths krijgen voor de bestanden.
```
readlink -f CurrentDaT.sh  
readlink -f CurrentDaTOutput.txt  
```

De outputs zijn:  
/home/younes/scripts/CurrentDaT.sh  
/home/younes/scripts/CurrentDaTOutput.txt  

Excuatble toestemming geven
```
chmod +x CurrentDaT.sh    
```

Crontab opstarten
```
crontab -e  
```

Deze code boven aan zetten zodat het weet waar de path is.
```
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/younes/scripts
```

![resultaat](/00_includes/LNX-08-resultaat3.png "resultaat")

Elke minute de huidige tijd automatisch schrijven naar de CurrentDaTOutput.txt
```
* * * * * /home/younes/scripts/CurrentDaT.sh  
```

Deze heb ik bij 2de ternimal ingevoert om het live te kunnen volgen.
```
tail -f /home/younes/scripts/CurrentDaTOutput.txt  
```

![resultaat](/00_includes/LNX-08-resultaat.png "resultaat")
-------------------------------  


### Create a script that writes available disk space to a log file in ‘/var/log’. Use a cron job so that it runs weekly.  

In ternimal gedaan om te kijken dat er geen synta errors waren.
```
df -h --total|grep ^total  
df -h /  
echo "Avaible Space Left  $(df -h / --output=used,avail,size,pcent) as of $(date)" >> /var/log/DiskSpace.log  
```

De script voor **DiskSpaceLog.sh**
```
cat <<"EOF"> DiskSpaceLog.sh  
#!/bin/bash  
echo "Avaible Space Left:$(df -h / --output=avail | tail -1) as of $(date)" >> /var/log/DiskSpace.log  
EOF
```

Vanwege de locatie voor de output file is het belangrijk om sudo erbij te zetten.
```
sudo bash DiskSpaceLog.sh  
```

Deze heb ik bij 2de ternimal ingevoert om het live te kunnen volgen.
```
tail -f /var/log/DiskSpaceLog.log  
```

Terug naar crontab
```
crontab -e
```

Testing voor elke minute om te kijken of het werkt eerst.
```
* * * * * sudo /home/younes/scripts/DiskSpaceLog.sh 
```

![resultaat](/00_includes/LNX-08-resultaat2.png "resultaat")

De script werkt voor elke minute en daarna weer aangepast om elke Maandag om 12:00.
```
0 12 * * 1 sudo /home/younes/scripts/DiskSpaceLog.sh  
```


### Gebruikte bronnen  
https://www.cyberciti.biz/faq/linux-display-date-and-time/  
https://opensource.com/article/17/11/how-use-cron-linux  
https://crontab.guru/  
https://www.baeldung.com/linux/cron-jobs-path  
https://www.redhat.com/sysadmin/linux-df-command  
https://www.hostinger.com/tutorials/vps/how-to-check-and-manage-disk-space-via-terminal  
https://phoenixnap.com/kb/linux-tail

### Ervaren problemen  
Voor de crontab dacht ik eerste dat het elke minute was 1 * * * * door dat in te vullen. Tijdens deze mindset ging ik het hard op lezen toen heb ik gemerkt dat ik het verkeerd had gelezen. Ook moest ik de path correct zetten omdat het niet last vanaf de script voor de crontab.  

### Resultaat  
Het kunnen invoeren van taken op schema. Eerst controleren dat ze werken met Bash command en  daarna Path aangepast zodat het ook in crontab kon vinden.
- Elke minuut de dag en tijd noteren naar een bestand.
- Elke week opslag ruimte noteren naar een bestand.
	- Had het eerste op elke minute getested.
  
