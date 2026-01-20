print("Jarand5122")

import csv

# Read data from myFile.csv
file_path = "myFile.csv"

with open(file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    print("Values from myFile.csv:")
    for row in reader:
        print(row[0])
