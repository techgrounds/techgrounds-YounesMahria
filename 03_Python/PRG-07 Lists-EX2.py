numbers = [9, 80, 16, 67, 35]


# We going through the range, len returns the amount of items in the list in this case it is 5.
for i in range(len(numbers)):
  # We do a simple math of i+1 % 5 (which is the length value), the % means modulo calcation the remaing number after division.
  # How many times can you dived it by? 13 / 2,  6 times 2 so that would be 12 and then 13-12 = 1 is the outcome.
  # In this same logic 4 % 5 would be 0 en remains 4 but 5 % 5 means 1 but 0 remains that's why I used this method.
  nextIndex= (i+1) % len(numbers);
  
  # Better make variables to make it easier to read. I pass the outcome of nextIndex to nextValue to keep it clean.
  # Which is much better than 'numbers[(i+1) % len(numbers)]'
  nextValue = numbers[nextIndex];
  
  # Now we print out the Numbers[i] + nextValue to get our correct calculation.
  print(f"number is {numbers[i]+nextValue}");
