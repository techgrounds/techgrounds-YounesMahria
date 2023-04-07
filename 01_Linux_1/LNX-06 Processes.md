# Processes  
telnet gebruiken inplaats van ssh.

## Key-terms

### telnet  
Het is een terminal emulation programma voor TCP/IP netwerken om toegang te kunnen krijgen naar een andere computer op het internet of lokale netwerk door aan te melden bij externe system. Het is een oude clientserverprotocol dat verbinding maakt met poort 23 maar dat is net beveiligd en alles kan gelezen worden door een derde in plain tekst.

### PID  
Een Process IDentification wordt gebruikt om elke process in je system te kunnen identificeren met een unikie nummer.

### inetd  
internet service daemon die telnet gebruikt voor Linux Ubuntu omgeving. Het is een communicatie middel tussen de verbonden apparateren.

## Opdracht

### Start the telnet daemon.  
```
sudo apt install telnetd -y 
sudo systemctl start inetd
```

![resultaat](/00_includes/LNX-06-resultaat.png "resultaat")

### Find out the PID of the telnet daemon.
```
sudo systemctl status inetd
systemctl show --property MainPID inetd
pidof inetd
```

![resultaat](/00_includes/LNX-06-resultaat2.png "resultaat")

### Find out how much memory telnetd is using.
```
sudo systemctl status inetd
sudo pmap process_ID | tail -n 1
```

![resultaat](/00_includes/LNX-06-resultaat3.png "resultaat")

### Stop or kill the telnetd process.  
```
sudo kill -9 process_ID
```

![resultaat](/00_includes/LNX-06-resultaat4.png "resultaat")


### Gebruikte bronnen  
https://www.howtoforge.com/how-to-install-and-use-telnet-on-ubuntu/
https://sleeplessbeastie.eu/2021/05/05/how-to-get-service-pid-using-systemctl/
https://itsfoss.com/how-to-find-the-process-id-of-a-program-and-kill-it-quick-tip
https://www.tutorialspoint.com/what-is-a-pid-file-in-linux

### Ervaren problemen  
telnet 18.157.179.30 52211  
Trying 18.157.179.30...  
Connected to 18.157.179.30.  
Escape character is '^]'.  
SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5  

Invalid SSH identification string.  
Connection closed by foreign host.

Kan geen verbinden maken met telnet.

Op Dinsdag zeer late op middag was had ik het verkeerd gedaan door het uitloggen van mij ssh en verbinding wou maken met telnet. Op Woensdag had ik get gewoon op mijn linux ternimal geinstalleerd en dat was alles nodig om de opdracht goed te kunnen makken.

### Resultaat  
Er achter komen dat de ze niet de zelfde namen bevant tussen package en process naam. Hierbij is telnet de package naam terwijl het inteld als process name gebruikt. Er kunnen achter wat de PID is voor de programma.