print("Jarand5122")

import csv

# Get five string values from the user
values = []
for i in range(1, 6):
    value = input(f"Enter string value {i}: ")
    values.append(value)

# Write the values to myFile.csv
file_path = "myFile.csv"
with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write each value as a row
    for value in values:
        writer.writerow([value])

print(f"\nValues successfully saved to {file_path}")
