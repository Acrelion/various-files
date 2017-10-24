# Conditions. I am using if for the first time.
# dogs += 5 is the same as dogs = dogs + 1
# This is because Python is dynamic typed language. You can change the value
# of a variable after you have called it already.

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved."

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."
	
if people <= dogs:
    print "People are less than or equal to dogs."
	
if people == dogs:
    print "People are dogs."
