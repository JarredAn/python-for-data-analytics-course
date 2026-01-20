print("Jarand5122")

import csv

# Read data from myFile.csv and check for numeric data
file_path = "myFile.csv"

try:
    has_numeric = False
    
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        # Check each cell for numeric data
        for row in reader:
            for cell in row:
                # Try to convert to a number
                try:
                    float(cell)
                    has_numeric = True
                    break
                except ValueError:
                    continue
            if has_numeric:
                break
    
    # Output result
    if has_numeric:
        print("The file contains numeric data.")
    else:
        print("The file contains no numeric data.")
        
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
