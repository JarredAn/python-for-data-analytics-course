from fractions import Fraction

print ("Jarand5122")

num1 = (int(input("Enter a whole number for the numerator: ")))
num2 = (int(input("Enter a whole number for the denominator: ")))

print (f'the simplified number is {format(Fraction(num1, num2), ".4f")}')
