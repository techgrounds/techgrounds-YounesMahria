# LNX-07 Bash scripting
[Geef een korte beschrijving van het onderwerp]

## Key-terms
**export** Het aanpassing van variables

## Opdracht
-Exercise 1:
Create a directory called ‘scripts’. Place all the scripts you make in this directory.
Add the scripts directory to the PATH variable.
Create a script that appends a line of text to a text file whenever it is executed.
Create a script that installs the httpd package, activates httpd, and enables httpd. Finally, your script should print the status of httpd in the terminal.

Variables:
You can assign a value to a string of characters so that the value can be read somewhere else in the script.
Assigning a variable is done using ‘=’.
Reading the value of a variable is done using ‘$<insert variable name here>’.

echo $PATH
export PATH=$PATH:/home/younes/scripts

cat << EOF > AppendsNewLine.sh
echo "newline >> AppendsOutput.txt"
EOF

cat << EOF >> AppendsNewLine.sh
#!/bin/bash
#Define text variable
text='placeholder';
#Typ welke text je wilt hebben.
read -p 'Typ in welke tekst je wilt gebruiken: ' text
echo "$text >> AppendsOutput.txt"
EOF

cat << EOF >> AppendsNewLine.sh
#Define text variable
text='placeholder';#Typ welke text je wilt hebben.
read -p 'Typ in welke tekst je wilt gebruiken: ' text
echo "$text" >> AppendsOutput.txt
EOF


echo "#!/bin/bash" > AppendsNewLine.sh
echo "#Define text variable" > AppendsNewLine.sh
echo "text='placeholder';" >> AppendsNewLine.sh
echo "#Typ welke text je wilt hebben." >> AppendsNewLine.sh
echo -e "read -p 'Typ in welke tekst je wilt gebruiken: ' text" >> AppendsNewLine.sh
echo -e "printf `$text` >> AppendsOutput.txt" >> AppendsNewLine.sh

echo -e "#Define text variable /n text='placeholder'; /n #Typ welke text je wilt hebben. /n read -p 'Typ in welke tekst je wilt gebruiken: ' text /n `$text` >> AppendsOutput.txt" >> AppendsNewLine.sh

printf "Appended text is: %s\n" "$newtext" >>

echo "test" >> AppendsOutput.txt'

echo "techgrounds" >> AppendsOutput.txt
echo ‘$text’ >> test.txt

#Typ welke text je wilt hebben.
read -p "Typ in welke tekst je wilt gebruiken"
echo ‘$<text>’ >> test.txt


echo "Installing httpd-apache2 package..."
sudo apt-get install -y apache2  
echo "Activing httpd-apache2..."
sudo /etc/init.d/apache2 start
sudo ufw allow 'Apache'
echo "Enabling httpd-apache2..."
sudo

sudo
echo "Your httpd-apache2 status below:"
sudo ufw status
sudo systemctl status apache2  



-Exercise 2:
Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file.

Conditions:
You can choose to only run parts of your script if a certain condition is met. For example, only read a file if the file exists, or only write to a log if the health check returns an error. This can be done using conditions.

A check for a condition can be done using ‘if’, ‘elif’, and/or ‘else’.




-Exercise 3:
Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file only if the number is bigger than 5. If the number is 5 or smaller, it should append a line of text to that same text file instead.

### Gebruikte bronnen
https://www.baeldung.com/linux/path-variable
https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04
https://www.howtogeek.com/442332/how-to-work-with-variables-in-bash/




### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
[Omschrijf hoe je weet dat je opdracht gelukt is (gebruik screenshots waar nodig).]
