print ("Jarand5122")
total = 0
salesTax = 0.07
#adds tax to items purchased and adds them to total and repeats 5 times
for counter in range(5):
    itemPrice = float(input("Enter the price of the item purchased: "))
    itemTax = itemPrice * salesTax
    itemTotal = itemPrice + itemTax
    total = total + itemTotal
print (f'The total cost of the 5 items purchased including tax is: {total}')