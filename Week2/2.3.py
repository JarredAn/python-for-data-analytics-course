print ("Jarand5122")

# Local variables
pocketNum = 0
outputStr = ''

# Get the pocket number from the user
pocketNum = int(input('Enter a pocket number (0-36): '))

# Determine if the pocket number is valid.
if pocketNum < 0 or pocketNum > 36:
    outputStr = 'Error: Invalid input'
    print (outputStr)
    #determine the color of the pocket number.
else:
         # For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered pockets are black.
        if pocketNum>=1 and pocketNum<=10:
            if pocketNum% 2:
                outputStr = 'Black' # even
            else:
                outputStr = 'Red' # odd

        #for pockets 11 through 18, the odd-numbered pockets are black and the even-numbered pockets are red.
        elif pocketNum >= 11 and pocketNum<=18:  
            if pocketNum % 2:
                outputStr = 'Red' # even
            else:
                outputStr = 'Black' # odd

        #for pockets 19 through 28, the odd-numbered pockets are red and the even-numbered 
        # pockets are black. 
        elif pocketNum >= 19 and pocketNum <= 28:
            if pocketNum % 2:
                outputStr = 'Black' # even
            else:
                outputStr = 'Red' # odd

        #for pockets 29 through 36, the odd-numbered pockets are black and the even-numbered 
        # pockets are red.
        elif pocketNum >= 29 and pocketNum <= 36:
            if pocketNum % 2:
                outputStr = 'Red' # even
            else:
                outputStr = 'Black' # odd
        # pocket number 0 is green
        else:
            outputStr = 'Green'

        # display the output
        print(outputStr)
