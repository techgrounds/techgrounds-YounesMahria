arr = ["Coen", "Casper", "Joshua", "Abdessamad", "Saskia"]

for x in arr:
  # prints every array value in arr, it starts from 0 end auto breaks till the last array 4.
  print(x)
  
print("")

for x in arr:
  # prints every array value i arr but stops at Joshua without print it's name because print is after the break and not before.
  if x == "Joshua":
    break
  print(x) 
