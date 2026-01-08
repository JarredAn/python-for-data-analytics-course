print ("My student ID is Jarand5122")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def compare():
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 < num2:
        print(f"{num1} is less than {num2}")
    else:
        print(f"{num1} is equal to {num2}")

def math():
    add = num1 + num2
    print(f"The sum of {num1} and {num2} is {add}")

    if num1 > num2:
        print (f" {num1} is greater than {num2}")
    elif num1 < num2:
        print (f" {num1} is less than {num2}")
    else:
        print (f" {num1} is equal to {num2}")

def lastFunction():
    print("FunctionThree returned the value of 1234")

compare()
math()
lastFunction()