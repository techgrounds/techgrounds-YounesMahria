# Files and directories  
Omgaan met files and directories in powershell met commandos.

## Key-terms

### nano
een text editor in de ternimal.

### ~  
Je root directory weergeven.  

### ls  
Weergeeft lijst van je files en directories op je huidige map. 

### mkdir  
Nieuwe directory aanmaken.  

### cat  
het maken of weergeven van een file.

### cd  
Nagiveren door je mappen.  

## Opdracht

### Find out your current working directory.  
```
~
```

### Make a listing of all   in your home directory.  
```
ls -all
```

### Within your home directory, create a new directory named ‘techgrounds’.  
```
mkdir techgrounds
```

### Within the techgrounds directory, create a file containing some text.  
```
cat text.txt
```

### Move around your directory tree using both absolute and relative paths.  
Absolute path (vanaf je root folder) 
```
cd /home/younes/techgrounds/  
```

Relative path (vanaf je huidige folder)
```
cd ../../younes/techgrounds/
```

### Gebruikte bronnen  
https://kinsta.com/blog/linux-commands/

### Ervaren problemen  
Geen

### Resultaat
Een nieuwe folder 'techgrounds' kunnen aanmaken en open gemaakt met **cd** command. Het kunnen lezen van een bestand met **cat**
![resultaat](/00_includes/LNX-02-resultaat.png "resultaat")
