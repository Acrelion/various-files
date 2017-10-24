"""
# script 1 My version for guessing a lucky number.
from random import randint

a = randint(1, 7)

while True:
    b = int(raw_input("> "))
    if a == b:
        print "You guessed the number"
        break
    elif b >= 8:
        print "You want to give me a number between 1 and 7."
    else:
        print "Nope."

# script 2 Guessing a lucky number.

answer = raw_input("Do you like Python? ")
while answer != "1":
    print "That is not the right answer! Try again."
    answer = raw_input("Do you like Python? ")
else:
    print "That is great!"

# script 3 Guessing with prompt every time.

answer = raw_input("Guess the number: ")
while answer != "1":
    print "That is not the right answer! Do you want to try again or to stop?"
    a2 = (raw_input("Y for again/N for stop?").lower())
    if "y" in a2:
        answer = raw_input("Guess the number: ")
    elif "n" in a2:
        break
    else:
        "Sorry. Please be more specific."
else:
    print "That is great!"

# script 4 Guessing with an option to stop \1 var\.

answer = raw_input("Guess the number: ").lower()
while (answer != "1") and (answer != "no"):
    print "That is not the right answer! Type 'no' if you want to stop."
    answer = raw_input("Guess the number: ").lower()
else:
    if answer == "1":
        print "That is great!"
    elif answer == "no":
        print "Bye!"

"""
# Guessing with 2 variables which can break the loop. + Prompt

again = "yes"
number = 1
while (number != 5) and (again != "no"):
    number = input("Guess the number: ")
    if number != 5:
        print "Nope. Try again."
        again = raw_input("Do you want to try again? ")
        if again != "no":
            number = input("Guessthe number: ")
else:
    if number == 5:
        print "That is great!"
    elif number == "no":
        print "Bye!"
            
