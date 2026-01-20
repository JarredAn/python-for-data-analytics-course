print("Jarand5122")

import csv

# Read data from myFile.csv with error handling
file_path = "myFile.csv"

try:
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        print("Values from myFile.csv:")
        for row in reader:
            print(row[0])
            
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
