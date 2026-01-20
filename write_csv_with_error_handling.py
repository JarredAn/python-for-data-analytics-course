print("Jarand5122")

import csv
import os

# Write data to myFile.csv with error handling
file_path = "myFile.csv"

# Check if file exists
try:
    if os.path.exists(file_path):
        print(f"Warning: '{file_path}' already exists and will be overwritten.")
    
    # Write data to the CSV file
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Sample data to write
        data = [
            ["Name", "Age", "City"],
            ["Alice", "25", "New York"],
            ["Bob", "30", "Los Angeles"],
            ["Charlie", "35", "Chicago"]
        ]
        
        # Write each row
        for row in data:
            writer.writerow(row)
    
    print(f"Data successfully written to '{file_path}'")
    
except PermissionError:
    print(f"Error: Permission denied. Cannot write to '{file_path}'")
except Exception as e:
    print(f"An error occurred: {e}")
