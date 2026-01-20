# Temperature average calculator: Celsius to Fahrenheit

celsius1 = float(input("Enter first temperature in Celsius: "))
celsius2 = float(input("Enter second temperature in Celsius: "))

average_celsius = (celsius1 + celsius2) / 2
average_fahrenheit = (average_celsius * 9/5) + 32

print(f"The average temperature is {average_celsius:.2f}°C")
print(f"The average temperature in Fahrenheit is {average_fahrenheit:.2f}°F")
