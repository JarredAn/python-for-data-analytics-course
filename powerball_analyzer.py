import csv
import matplotlib.pyplot as plt

def read_powerball_numbers(file_path):
    # Count how many times specific numbers appear
    # Dictionary to track multiple numbers
    number_counts = {"11": 0, "20": 0}
    
    with open(file_path, 'r') as csvfile:
        for line in csvfile:
            # Split each line by spaces to get individual numbers
            numbers = line.split()
            for number in numbers:
                # Check if this number is one we're tracking
                if number in number_counts:
                    number_counts[number] += 1
    
    # Display results
    for num, count in number_counts.items():
        print(f"Number '{num}' appeared {count} time(s) in the file.")
    
    # Create bar graph
    numbers = list(number_counts.keys())
    counts = list(number_counts.values())
    
    plt.bar(numbers, counts, color=['blue', 'green'])
    plt.xlabel('Numbers')
    plt.ylabel('Frequency')
    plt.title('Powerball Number Frequency')
    plt.show()
    

def main():
    
    # Get file path from user
    file_path = "C:\\PythonFiles\\powerball.csv"
    
    print()
    read_powerball_numbers(file_path)

main()
