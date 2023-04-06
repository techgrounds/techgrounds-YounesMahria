# LNX-07 Bash scripting
Werken met verschilden Bash scripts

## Key-terms
**export** Het aanpassing van variables
**bash** 

## Opdracht

### Exercise 1:
### Create a directory called ‘scripts’. Place all the scripts you make in this directory.
```
mkdir scripts
```

### Add the scripts directory to the PATH variable.
```
echo $PATH
export PATH=$PATH:/home/younes/scripts/
```

### Create a script that appends a line of text to a text file whenever it is executed.

! Ik had 'cat <<"EOF"> EOF' gebruikt voordat ik nano deed.  

Deze script geschreven zodat je steeds een nieuwe tekst kan schrijven.

```
cat <<"EOF"> AppendsNewLine.sh
#!/bin/bash
#Define text variable
text="";
echo "Typ in welke tekst je wilt gebruiken: "
read text
echo "$text" > AppendsOutput.txt
EOF
```

Had later door dat ik voor mijzelf te moeijlijke maakte en gewoon dit kon doen.

```
cat <<"EOF"> AppendsNewLine.sh
#!/bin/bash
echo "Only this text" > AppendsOutput.txt
EOF
```

De excutable toestemming geven voor de file en daarna de script starten met bash daarna de output lezen.

```
chmod +x AppendsNewLine.sh
bash AppendsNewLine.sh
cat AppendsOutput.txt
```
 ![resultaat](/00_includes/LNX-07-resultaat.png "resultaat")

### Create a script that installs the httpd package, activates httpd, and enables httpd. Finally, your script should print the status of httpd in the terminal.

Mijn script toevegen met cat 

```
cat <<"EOF"> InstallHttpd.sh
#!/bin/bash

# Installing httpd-apache2 package
sudo apt-get install -y apache2

# Actives and Enable the httpd-apache2 service
sudo systemctl start apache2

# Enable the httpd-apache2 service
sudo systemctl enable apache2

# Print the status of httpd-apache2
sudo systemctl status apache2  

EOF
```

![resultaat](/00_includes/LNX-07-resultaat2.png "resultaat")
-----------------------------------

### Variables:
You can assign a value to a string of characters so that the value can be read somewhere else in the script.
Assigning a variable is done using ‘=’.
Reading the value of a variable is done using ‘$<insert variable name here>’.

### Exercise 2:
Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file.


```
cat <<"EOF"> rngStore.sh
#!/bin/bash
numberOutcome=0
#Generate random number between 1-10
numberOutcome=$((1 + $RANDOM % 10))
echo $numberOutcome
echo $numberOutcome > rngStoreOutput.txt
EOF
```

De excutable toestemming geven voor de file en daarna de script starten met bash daarna de output lezen.
```
chmod +x rngStore.sh
bash rngStore.sh
cat rngStoreOutput.txt
```
![resultaat](/00_includes/LNX-07-resultaat3.png "resultaat")

-----------------------------------

Conditions:
You can choose to only run parts of your script if a certain condition is met. For example, only read a file if the file exists, or only write to a log if the health check returns an error. This can be done using conditions.

A check for a condition can be done using ‘if’, ‘elif’, and/or ‘else’.


-Exercise 3:
Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file only if the number is bigger than 5. If the number is 5 or smaller, it should append a line of text to that same text file instead.



```
cat <<"EOF"> rngStoreIfStatement.sh
#!/bin/bash
numberOutcome=0
#Generate random number between 1-10
numberOutcome=$((1 + $RANDOM % 10))

#Check if the outcome is 5 or smaller
if [[  $numberOutcome -le 5  ]]; then
    echo "The outcome($numberOutcome) was 5 or smaller"
    echo $numberOutcome > rngStoreIfStatementOutput.txt
    exit 1
fi

#Check if the outcome is bigger than 5
if [[  $numberOutcome > 5  ]]; then
    echo "The outcome($numberOutcome) was bigger than 5"
    echo "Sorry number was too big!" > rngStoreIfStatementOutput.txt
    exit 1
fi
EOF
```

De excutable toestemming geven voor de file en daarna de script starten met bash daarna de output lezen.
```
chmod +x rngStoreIfStatement.sh
bash rngStoreIfStatement.sh
cat rngStoreIfStatementOutput.txt
```

![resultaat](/00_includes/LNX-07-resultaat4.png "resultaat")
-----------------------------------



### Gebruikte bronnen
https://www.baeldung.com/linux/path-variable
https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04
https://www.howtogeek.com/442332/how-to-work-with-variables-in-bash/
https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php
https://linuxhint.com/generate-random-number-bash/
https://linuxhint.com/compare-numbers-bash/







### Ervaren problemen
Een script kunnen scrhijven in de terminal was nieuwe voor mij. 
De eerste was vim maar die deed het niet goed,
De andere was nano wat veel beter is en juist editor voor doeleindine.
Wel heb ik kunnen vinden dat ik ook met de command 'cat <<"EOF"> 'regels tekst' EOF' het ook mogelijke is met copy pasting.

### Resultaat


