# LNX-04 Users and groups
Nieuwe gebruiker aanmaken in admin group, password en sudo.

## Key-terms
**sudo** Een admin taak te kunnen uitvoeren hierbij moet je wachtwoord ook geven ter controlere.
**adduser** Een nieuwe gebruiker toevoegen.
**usermod** Het wijzing van een gebruiker toestemmingen.

## Opdracht
-Create a new user in your VM. 
>The new user should be part of an admin group.
>The new user should have a password.
>The new user should be able to use ‘sudo’

sudo adduser techgrounds
sudo usermod -aG sudo techgrounds
id techgrounds

-Locate the files that store users, passwords, and groups. See if you can find your newly created user’s data in there.
cat /etc/passwd

### Gebruikte bronnen
https://www.cyberciti.biz/faq/add-new-user-account-with-admin-access-on-linux/

### Ervaren problemen
Vergeet soms sudo op begin te zetten nadat ik lees hoe ik de commandos moet uitvoeren.

### Resultaat
![resultaat](/00_includes/LNX-04-resultaat.png "resultaat")
![resultaat2](/00_includes/LNX-04-resultaat2.png "resultaat2")
