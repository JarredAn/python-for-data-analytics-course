print ("Jarand5122")
# This program calculates th ending principal in a bank

#account after compunding the interest
p = float(input('Enter the starting prinipal" '))
r = float(input('Enter the annual interest rate: '))
n = int(input('How many times per year is the interst compounded? '))
t = int(input('For how many years will the account earn interest? '))

#Adjust the interest rate.
r = r / 100

#Calculate the ending balance.
a = p * (1 + float(r) / n ) ** (n * t)

# Display the ending balance
print (f'At the end of {t} years you will have ${a:,.2f}')