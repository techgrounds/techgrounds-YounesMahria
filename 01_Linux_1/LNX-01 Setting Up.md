	# LNX-01 Setting Up  
Het kunnen inloggen op een SSH connection.  

## Key-terms

### SSH  
Secure Shell is een network protocol bedoeld om gebruikers een beveiligd connection maken naar en toegang te kunnen krijgen bij een computer met onbeveiligd network.

## Opdracht

### Make an SSH-connection to your virtual machine. SSH requires the key file to have specific permissions, so you might need to change those.
*When the connection is successful, type whoami in the terminal. This command should show your username.
![resultaat](/00_includes/LNX-01-resultaat.png "resultaat")

### Gebruikte bronnen
Techgrounds Pathways van de cloud opdracht.

### Ervaren problemen
Permission Denied tijdens het inloggen. De command op terminal was niet volledige ingevuld en geen verwijzen naar de file. De volgende stappen heb ik genomen om het op te lossen.
```
cd C:\Users\TechGrounds\.ssh
ssh -i .\Nest-Yo-Mahria.pem younes@18.157.179.30 -p 52211
```

### Resultaat
Het kunnen inloggen op een SSH connection. De opstart scherm van Ubuntu is gekomen en whoiam heeft een output laten zien.