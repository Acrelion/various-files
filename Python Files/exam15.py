#Some code in this programs is repeated. If you can, fix this. 8.5.2015
# prints a diamond shape by given number

def printNumberLine(diaCenter):
    #main function hub

    #sub functions for the two parts of the picture
    upper(diaCenter)
    lower(diaCenter)

def howMany(diaCenter):
    # helper function
    # getting how many digits we will have
    spaces = 0
        
    for i in range(diaCenter + 1):
        spaces += 1
    for j in range(diaCenter, -1, -1):
        spaces += 1

    return spaces

def upper(diaCenter):
    # printing the upper part of the picture
    for xPrime in range (0, diaCenter):
        numbers = []

        # how many character we will have at most on one line
        characters = howMany(diaCenter)

        for i in range(0, xPrime):         
            numbers.append(str(i))

        for i in range(xPrime, -1, -1):
            numbers.append(str(i))

        # how many empty spaces in total we will have left to fill the bill
        difference = characters - len(numbers)
        onEachSide = 0
        
        if (difference != 0):
            onEachSide = difference / 2
             
        print (" " * onEachSide) + "".join(numbers) + (" " * onEachSide)

def lower(diaCenter):
    #printing the lower part of the picture
    for xSecond in range(diaCenter, -1, -1):
        numbers = []

        # how many character we will have at most on one line
        characters = howMany(diaCenter)

        for i in range(0, xSecond):
            numbers.append(str(i))

        for i in range(xSecond, -1, -1):
            numbers.append(str(i))

        # how many empty spaces in total we will have left to fill the bill
        difference = characters - len(numbers)
        onEachSide = 0
        
        if (difference != 0):
            onEachSide = difference / 2
             
        print (" " * onEachSide) + "".join(numbers) + (" " * onEachSide)



        
#calling the main function
printNumberLine(input("Enter a number 0-9: "))
