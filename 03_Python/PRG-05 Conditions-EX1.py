name = input("Please in put your name: ")

# Gets the input from the name and checks if it is my name(Younes) or not (CASESENTIVE)
if (name  == "Younes"):
  print(f"Hello! Welcome, {name}!");  
else:
  print(f"You're {name}, not Younes. Please leave!");  

print("\nNot sentive to your cases! I mean not casesentive");

# Gets the input from the name and converts to lowercases and checks if it is my name(younes) or not (NOT CASESENTIVE)
if (name.lower()  == "younes"):
  print(f"Hello! Welcome, {name}!");  
else:
  print(f"You're {name}, not Younes. Please leave!");  