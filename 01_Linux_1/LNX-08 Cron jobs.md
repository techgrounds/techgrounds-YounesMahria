# LNX-08 Cron jobs  


## Key-terms

### **Cron Jobs**  

### **Crontab**    
Lijst met schemas voor de taken die automatische worden uitgevoerd.  

## Opdracht

### Create a Bash script that writes the current date and time to a file in your home directory.  

```
cat <<"EOF"> CurrentDaT.sh  
#!/bin/bash  
echo $(date) >> /home/younes/scripts/CurrentDaTOutput.txt  
EOF  
```
*echo $(date +"%D %T") > $HOME/datetime.txt*
-------------------------------  

### Register the script in your crontab so that it runs every minute.    

```
readlink -f CurrentDaT.sh  
/home/younes/scripts/CurrentDaT.sh  
readlink -f CurrentDaT.sh  
/home/younes/scripts/CurrentDaTOutput.txt  

chmod +x CurrentDaT.sh    

tail -f /home/younes/scripts/CurrentDaTOutput.txt  

crontab -e  


```
Crontab opstarten
```
crontab -e  
```

```
* * * * * /home/younes/scripts/CurrentDaT.sh  
```

-------------------------------  


### Create a script that writes available disk space to a log file in ‘/var/log’. Use a cron job so that it runs weekly.  

```
df -h --total|grep ^total  
df -h /  
echo "Avaible Space Left  $(df -h / --output=used,avail,size,pcent) as of $(date)" >> /var/log/DiskSpace.log  
```

```
cat <<"EOF"> DiskSpaceLog.sh  
#!/bin/bash  
echo "Avaible Space Left:$(df -h / --output=avail | tail -1) as of $(date)" >> /var/log/DiskSpace.log  
EOF  
```

```
sudo bash DiskSpaceLog.sh  
tail -f /var/log/DiskSpaceLog.log  
```


Testing voor elke minute om te kijken of het werkt eerst.
```
* * * * * sudo /home/younes/scripts/DiskSpaceLog.sh 
```

De script werkt en daarna weer aangepast om elke Maandag om 12:00
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





### Ervaren problemen  
Voor de crontab dacht ik eerste dat het elke minute was 1 * * * * door dat in te vullen. Tijdens deze mindset ging ik het hard op lezen toen heb ik gemerkt dat ik het verkeerd had gelezen. Ook moest ik de path correct zetten omdat het niet last vanaf de script voor de crontab.  

### Resultaat  
![resultaat](/00_includes/LNX-08-resultaat.png "resultaat")  
![resultaat](/00_includes/LNX-08-resultaat2.png "resultaat")  
