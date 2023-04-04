# LNX-03 Working with text (CLI)
[Geef een korte beschrijving van het onderwerp]

## Key-term
**bash** Het schrijven in een tekst bestand
**echo "new tech met linux" > test.txt** Vervangt alle tekst met het word 'techgrounds'
**echo "techgrounds" >> test.txt** Voegt een nieuwe lijn toe met het word 'techgrounds'
**grep** het filteren van worden in je tekst bestand.

## Opdracht
-Use the echo command and output redirection to write a new sentence into your text file using the command line. The new sentence should contain the word ‘techgrounds’.

echo "new tech met linux" > test.txt
echo "techgrounds" >> test.txt
cat test.txt

-Use a command to write the contents of your text file to the terminal. Make use of a command to filter the output so that only the sentence containing ‘techgrounds’ appears.

grep "techgrounds" test.txt

-Read your text file with the command used in the second step, once again filtering for the word ‘techgrounds’. This time, redirect the output to a new file called ‘techgrounds.txt’.

grep "techgrounds" test.txt > techgrounds.txt

### Gebruikte bronnen
https://linuxize.com/post/bash-write-to-file/

### Ervaren problemen
De juiste commands vinden en gebruiken.   

### Resultaat
![resultaat](/00_includes/LNX-03-resultaat.png "resultaat")