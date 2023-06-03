number = 0;

# while the number is not equal to 100 repeat the process till it is.
while number != 100:
  #attempts to see if input is an integer, if it is then follow the conditions otherwise go to except
  try:
    # Accepts only int numbers
    number = int(input("Please input a number: "));
    
    if (number == 100):
      print(f"{number} is a nice number indeed");  
    elif (number < 100):
        print(f"{number} is pretty low, isn't it!");  
    elif (number > 100):
        print(f"Wow, {number} is a big number!"); 
  
  # if the input was not a integer then we throw this error message.      
  except:
    print(f"Please input only integer  number (that means a number without decimal!)");  