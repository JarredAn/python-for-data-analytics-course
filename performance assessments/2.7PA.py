#get name and student ID
name = input("Please enter your name: ")
student_id = input("Please enter your student ID: ")

#initialize guesses and guess
guesses = 0
guess = 0

#while loop to run until user guesses correctly
while guess != 7:
    guesses += 1
    guess = int(input("Guess a number between 1 and 10... "))
    if guess < 7:
        print("Too low!")
    elif guess > 7:
        print("Too high!")
print(f"Congratulations {name}! You've guessed the correct number in {guesses} attempts.")

#blank line for readability
print()

#while loop to count incrementally from 7 to 12
increment = 1
guess = 7
while guess != 12:
    guess = guess + 1
    print(f' 7 incremented by {increment} is {guess}')
    increment += 1

print()

#for loop to count incrementally from 7 to 12
guess = 7
increment = 1
for counter in range(5):
    guess = guess + 1
    print(f" 7 incremented by {increment} is {guess}")
    increment +=1