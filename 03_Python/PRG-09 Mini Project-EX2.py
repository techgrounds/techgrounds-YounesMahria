# Rock Paper Scissors:
# 
# The player plays against a computer opponent typing either a letter (rps) or an entire word (rock paper scissors) to play their move.
# Create a function that checks whether the move is valid or not.
# Create another function to create a computer move.
# Create another function to check who wins the round.
# Finally, create a function that keeps track of the score.
# The game should be played in a predetermined number of rounds.

import random

player_name = "";
player_score = 0;
player_guess = "";

cpu_score = 0;
cpu_name = "Not AlphaZero";
cpu_guess = "";
cpu_random = ["rock","paper","scissors"]
cpu_cheats = False;

# If you want to change the scoring system!
game_win = 3; # The winner gets awared 3 points by defaults
game_tie = 1; # Both gets awared with 1 point by default
game_lose = 0; # The loser scores 0 points by default

total_round = 7;
current_round = 0;

valid_guess = ["rock", "r", "paper","p", "scissors","s"];

#print(f"Please enter your next move Rock(r), Paper(p) or Scissors(s)");


def cpu_move():
  cpu_guess = random.choice(cpu_random);
  return cpu_guess;

def end_result():
  if(player_score > cpu_score):
    print(f"{player_name} WON! With a score of {player_score} against {cpu_name} score of {cpu_score}");
  elif(player_score < cpu_score):
    print(f"{player_name} lost against the {cpu_name}! Your score was {player_score} against {cpu_name} score of {cpu_score}");
  else:
    print(f"{player_name} and {cpu_name} tied! You're both scored {player_score}");
  
def guess_convert(a):
  if(player_guess == "r"):
    return "rock";
  elif(player_guess == "p"):
    return "paper"; 
  elif(player_guess == "s"):
    return "scissors";
  else:
    return a

player_name = input(f"Please enter your name: ").lower();

  
# while the number is not equal to 100 repeat the process till it is.
while current_round != total_round:
  #attempts to see if input is an integer, if it is then follow the conditions otherwise go to except
  #try:
    # Accepts only Rock(r), Paper(p) or Scissors(s) 
    
    player_guess = input(f"Please enter your next move rock(r), paper(p) or scissors(s): ").lower();
    
    # Checks if the input was valid otherwise tell them to do it
    while player_guess not in valid_guess:
      player_guess = input(f"You typed an invalid choose, please try again and actually type rock(r), paper(p) or scissors(s): ").lower();
       
    cpu_guess = cpu_move();
    player_guess = guess_convert(player_guess);
        
    # checks if both chosen the same!
    current_round+=1;
    if(player_guess == cpu_guess):
      print(f"This is a tie! You both selected {cpu_guess}!")
      player_score+=game_tie;
      cpu_score+=game_tie;
    # If player choose Rock
    elif(player_guess == "rock"):
      if(cpu_guess == "paper"):
        print(f"You lost! Paper wins against Rock");
        player_score+=game_lose;
        cpu_score+=game_win;
      else:
        print(f"You Win! Rock wins against Scissors");
        player_score+=game_win;
        cpu_score+=game_lose;        

    # If player choose Paper
    elif(player_guess == "paper"):
      if(cpu_guess == "scissors"):
        print(f"You lost! Scissors wins against Paper");
        player_score+=game_lose;
        cpu_score+=game_win;
      else:
        print(f"You Win! Paper wins against Rock");
        player_score+=game_win;
        cpu_score+=game_lose;           

    # If player choose Scissors
    elif(player_guess == "scissors"):
      if(cpu_guess == "rock"):
        print(f"You lost! Rock wins against Scissors");
        player_score+=game_lose;
        cpu_score+=game_win;
      else:
        print(f"You Win! Scissors wins against paper");
        player_score+=game_win;
        cpu_score+=game_lose;        
  
  # if the input was not a integer then we throw this error message.      
  #except:
  #  print(f"Please input only integer  number (that means a number without decimal!)");  
    
end_result()