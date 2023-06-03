# Number Guessing
# This is very close to PRG-05 Conditions-EX2 with PRG-06 Functions-EX1 code but modified.
#
# Generate a random number between 1 and 100 (or any other range). (Lets have the player choose range!).
# The player guesses a number. For every wrong answer the player receives a clue.
# When the player guesses the right number, display a score.

import random
minimal_number = 0; # The lowest number for the range
maximal_number = 0; # The highest number for the range
guessing_number = 0; # The number you input for guessing
correct_number = 0; # The correct number that gets generated randomly
attempts_number = 0; # The amount attempts it toke you before guessing
score_number = 0; # Your score after finally guessing the correct number.

# Making sure that they did in face put in the lowest and highest number.
while maximal_number <= minimal_number:
  try:
    minimal_number = int(input("Please input the lowest number for the range: "));
    maximal_number = int(input("Please input the higest number for the range: "));
    # Fail safe so that player will not try any funny business.
    if (maximal_number <= minimal_number):
      print(f"Nice try! This is not allowed redo it!");
    # if the input was not a integer then we throw this error message.      
  except:
    print(f"Please input only integer  number (that means a number without decimal!)");  

# Randomly generate a number
correct_number = random.randint(minimal_number, maximal_number);

# Debug information to see if all coding worked as intended.
# print(f"L{minimal_number},H:{maximal_number},C:{correct_number}");

# function to call the final score calculations!
def finale_score():
    # Score system, if it really toke you over 100 guesses then your score is getting even lower!
    score_number = 1000 / attempts_number + 50 * (100-attempts_number) + 50;
    return int(score_number);

# while the number is not guessed repeat the process till it is.
while guessing_number != correct_number:
  #attempts to see if input is an integer, if it is then follow the conditions otherwise go to except
  try:
    # Accepts only int numbers
    guessing_number = int(input("Please guess the number: "));
    ## I added while to make sure you put 1 and 100
    while(guessing_number > maximal_number):
      guessing_number = int(input(f"Please input a number BETWEEN {minimal_number} and {maximal_number} and not higher than {maximal_number}: "))
    while(guessing_number < minimal_number):
      guessing_number = int(input(f"Please input a number BETWEEN {minimal_number} and {maximal_number} and not lower than {minimal_number}: "))

    
    
    if (guessing_number == correct_number):
      attempts_number+=1;
      score_number = finale_score();
      # Easter egg for people who somehow managed do it on their first try
      if(attempts_number == 1):
        print(f"WOW! First try you were very lucky!"); 
      
        print(f"""{guessing_number} is the correct number!
You're total score is {score_number} in {attempts_number} attempt(s)""");  
      
    elif (guessing_number < correct_number):
      attempts_number+=1;
      print(f"{guessing_number}? Not high enough!");
          
    elif (guessing_number > correct_number):
      attempts_number+=1;
      print(f"{guessing_number}? You need to go back!"); 
  
  # if the input was not a integer then we throw this error message.      
  except:
    print(f"Please input only integer  number (that means a number without decimal!)");  