# Ex in which I am trying to clear the screen with os.system("cls")
#State: Finished.

import os
print "Hello!"
a = raw_input("Write something short: ")

print "You wrote:\n %s\n" % a
print "Press Enter to see the last message.",
raw_input()
os.system('cls')

print "Thank you."

