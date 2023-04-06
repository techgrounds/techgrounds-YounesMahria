# LNX-03 Working with text (CLI)  
Het kunnen verwerken van teksten.

## Key-term

### bash  
Het staat voor Bourne Again Shell en het is veel gebruikte voor Linux en UNIX systemen dat laat gebruikers verschillende commandos en taken op de computer. 

### Shell  
De software waar je commandos invoert in de terminal waarbij Bash een ervan is. Er zijn ook andere shell softwares zoals:
* sh (bourne shell)
* csh (c shell)
* tcsh (turbo c shell)
* Windows PowerShell

### Terminal
De GUI van het Shell waarbij je kunt zien waar je commandos kan invoeren.

### Kernel
De belangerijke communicatiemiddel voor je operation system. Leest de ingevoerde commando om extra taken te kunnen verichten nadat de shell het heeft goed gekeurd denk hierbij aan een admin en sudo commando. 

### echo  
Het weergeven de output resultaat dat je op het einde had geschreven.

### >  
Verwijst de output om het te schrijven naar een bestand, als de bestand al bestaat wordt alles gewist als het niet bestaat wordt het als nieuw gemaakt.

###  >>  
Verwijst de output om het te schrijven naar een bestand als toevoeging vanaf de nieuwe regel, als de bestand niet bestaat wordt het als nieuw gemaakt.

### grep  
Het filtert en zoekt de opgeven worden in je tekst bestand.

### stdin  (Standard Input)   
De file handle dat de invoeringen van een commando leest zodat het weet wat het moet doen.

### stdout  (Standard Output)
Jouw process schrijft de output naar de file handle.

### stderr  (Standard Error)  
Jouw process schrijf de diagnostisch output naar de file handle

## Opdracht  

### Use the echo command and output redirection to write a new sentence into your text file using the command line. The new sentence should contain the word ‘techgrounds’.


### echo "new tech met linux" > test.txt  
Vervangt alle tekst met het word 'techgrounds'

### echo "techgrounds" >> test.txt  
Voegt een nieuwe lijn toe met het word 'techgrounds'

```
echo "new tech met linux" > test.txt
echo "techgrounds" >> test.txt
cat test.txt
```

![resultaat](/00_includes/LNX-03-resultaat.png "resultaat")

### Use a command to write the contents of your text file to the terminal. Make use of a command to filter the output so that only the sentence containing ‘techgrounds’ appears.

```
grep "techgrounds" test.txt
```
![resultaat](/00_includes/LNX-03-resultaat2.png "resultaat")

### Read your text file with the command used in the second step, once again filtering for the word ‘techgrounds’. This time, redirect the output to a new file called ‘techgrounds.txt’.

```
grep "techgrounds" test.txt > techgrounds.txt
```
![resultaat](/00_includes/LNX-03-resultaat3.png "resultaat")

### Gebruikte bronnen
https://linuxize.com/post/bash-write-to-file/
https://www.cyberciti.biz/faq/howto-use-grep-command-in-linux-unix/
https://blog.devops.dev/bash-commands-101-a-beginners-guide-to-the-linux-command-line-interface-d8a379f41bf
https://stackoverflow.com/questions/3385201/confused-about-stdin-stdout-and-stderr

### Ervaren problemen  
De juiste commands vinden en gebruiken.   

### Resultaat
Nieuwe bestanden maken en dan of alles wissen met een nieuwe tekst of het toevegen. Het kunnen filteren en vinden van het opgeven woord.