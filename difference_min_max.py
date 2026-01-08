# Program to find the difference between the lowest and highest of five user-input numbers
numbers = []
for i in range(5):
    while True:
        try:
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

lowest = min(numbers)
highest = max(numbers)
difference = highest - lowest

print(f"The difference between the highest and lowest number is: {difference}")