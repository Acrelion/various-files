# A game of mastermind. Player has 10 tries to guess a number.

import random

done = False
stop = 0
number_str = []


all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
random.shuffle(all_digits)


for i in range(4):
    number_str.append(all_digits.pop(0))


while not done:
    if stop == 10:
        print "You are out of guesses. You loose."
        break
    
    
    user_input = raw_input("Make a guess:")
    
    
    how_many = 0
    
    for i in range(len(number_str)):
        if number_str[i] == user_input[i]:
            how_many += 1
           
 
    if how_many == 4:
        done = True
        print "You win! Game is now over."
    else:
        print "*" * how_many
        stop += 1