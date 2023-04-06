# LNX-05 File permissions
Permissions op files aanpassen.

## Key-terms
**ls -l [filename]** Weergeeft permissions voor de file.
**chmod** Het aanpassen van permissions op de file.
**chown [user_name] [file_name]** verander de owner voor de file
**chgrp [group_name] [file_name]** verander de group voor de file

## Opdracht

### Create a text file.
```
touch lnx05.txt
```

### Make a long listing to view the file’s permissions. 
```
ls -l lnx05.txt
```

![resultaat](/00_includes/LNX-05-resultaat.png "resultaat")

### Who is the file’s owner and group? 
younes younes

![resultaat2](/00_includes/LNX-05-resultaat2.png "resultaat2")

### What kind of permissions does the file have?
```
-rw-rw-r--
```
[-owner-group-others]



### Make the file executable by adding the execute permission (x).
```
chmod +x lnx05.txt
-rwxrwxrwx 1 younes younes 11 Apr  4 09:58 lnx05.txt
```

### Remove the read and write permissions (rw) from the file for the group and everyone else, but not for the owner. Can you still read it?
```
chmod -rw lnx05.txt
cat lnx05.txt 
(cat: lnx05.txt: Permission denied)
```

Nee, kan de file niet meer lezen omdat ik niet aangaf dat het alleen voor de group/everyone else was.

![resultaat3](/00_includes/LNX-05-resultaat3.png "resultaat3")

```
chmod +rw lnx05.txt
chmod go-rw lnx05.txt
```

![resultaat4](/00_includes/LNX-05-resultaat4.png "resultaat4")

### Change the owner of the file to a different user. If everything went well, you shouldn’t be able to read the file unless you assume 
```
sudo chown techgrounds lnx05.txt
cat lnx05.txt
```

### root privileges with ‘sudo’.
```
sudo cat lnx05.txt
```

### Change the group ownership of the file to a different group.
```
sudo chgrp techgrounds lnx05.txt
```

![resultaat5](/00_includes/LNX-05-resultaat5.png "resultaat5")

### Gebruikte bronnen
https://phoenixnap.com/kb/linux-file-permissions
https://www.pluralsight.com/blog/it-ops/linux-file-permissions
https://www.freecodecamp.org/news/linux-chmod-chown-change-file-permissions/

### Ervaren problemen
Tussenstap vergeten bij chmod om te vertellen voor welke groepen het geldt.

### Resultaat




