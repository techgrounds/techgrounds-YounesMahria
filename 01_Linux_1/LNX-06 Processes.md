# LNX-06 Processes  
telnet gebruiken inplaats van ssh.

## Key-terms
**telnet** zelfde als ssh maar dan niet beveiligd waarbij alles in plain text te lezen valt.  
**PID**
**inetd** 

## Opdracht
**-Start the telnet daemon.**   
sudo apt install telnetd -y  

-Find out the PID of the telnet daemon.
sudo systemctl status inetd
systemctl show --property MainPID inetd
pidof inetd

-Find out how much memory telnetd is using.
sudo systemctl status inetd
sudo pmap process_ID | tail -n 1

-Stop or kill the telnetd process.  
sudo kill -9 process_ID



### Gebruikte bronnen
https://www.howtoforge.com/how-to-install-and-use-telnet-on-ubuntu/
https://sleeplessbeastie.eu/2021/05/05/how-to-get-service-pid-using-systemctl/
https://itsfoss.com/how-to-find-the-process-id-of-a-program-and-kill-it-quick-tip

### Ervaren problemen
telnet 18.157.179.30 52211  
Trying 18.157.179.30...  
Connected to 18.157.179.30.  
Escape character is '^]'.  
SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5  

Invalid SSH identification string.  
Connection closed by foreign host.

Kan geen verbinden maken met telnet.

Op Dinsdag had ik het verkeerd gedaan omdat ik uitlogd van mij ssh en verbinding wou maken met telnet. Op Woensdag had ik get gewoon op mijn linux ternimal geinstalleerd en dat was alles.

### Resultaat
![resultaat](/00_includes/LNX-06-resultaat.png "resultaat")


////Soft Skills///
Waar ik tegenaanliep?

Wat was de oplossing?
