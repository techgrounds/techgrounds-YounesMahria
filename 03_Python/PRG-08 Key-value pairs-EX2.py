import csv
import os

busy_add_date = True;

# Make the dictionary array list
dictionary = {
  "First name": [],
  "Last name": [],
  "Job title": [],
  "Company": []
}

# I know this is a rabbit hole I did but it was fun to make it this way to challenge myself!
while busy_add_date != False:
  # Checks the length of dictionary
  dictionary_arraylength = (len(dictionary["First name"]));

  # Inserting all 4 information
  print("Please insert your information!");
  firstname = input("Type your first name: ");
  lastname = input("Type your last name: ");
  jobtitle = input("Type your current job title: ");
  company = input("Type your company you work at: ");

  # Storage information of the value above
  newData = [firstname, lastname, jobtitle, company]

  # Loop through every entery to add with the i - index
  # This will add multi-values to 1 key.
  for i, x in enumerate(dictionary.keys()):
    # Add all new entry to dictionary. 
    dictionary.setdefault(x, [dictionary_arraylength]).append(newData[i]);

  answer_time = input("\nDo you wish to enter another data? (type 'no' to stop anything else to resume) ");
  if (answer_time.lower()  == "no"):
    busy_add_date = False;
  else:
    print(f"Okay! Put a new data!");  
  

# Check my current storage list
for x,y in dictionary.items():
  # Prints out the every dictionary list with a for loop.
  print(f"{x}: {y}");

print(dictionary);


file_csv = "dictionaryData.csv";
# columns_csv = ["First name","Last name","Job title","Company"];

# Checks if csv file existe otherwise make a new csv file
if not os.path.exists(file_csv):
  with open(file_csv, "w+", newline="") as file:
    print(f"A new file has been created!");
    writer = csv.writer(file);
    # Adds every row to header!
    writer.writerow(dictionary.keys());
    # OLD way with writer = csv.DictWriter(file_csv, fieldnames=columns_csv);
    
    # If I entered 1 or multi entries that I want to add each time to a new row.
    max_len = max(len(arr) for arr in dictionary.values())
    
    for i in range(max_len):
      row = [dictionary[key][i] if i < len(dictionary[key]) else "" for key in dictionary.keys()];
      writer.writerow(row);
    
else:
  with open(file_csv, "a", newline="") as file:
    print(f"File already exists!");
    writer = csv.writer(file);
    max_len = max(len(arr) for arr in dictionary.values())
    
    for i in range(max_len):
      row = [dictionary[key][i] if i < len(dictionary[key]) else "" for key in dictionary.keys()];
      writer.writerow(row);
      
    #for row in multivalues():
     # writer.writerow(row);
    
    
