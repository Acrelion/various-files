"""
def uname():
    inp1 = raw_input("Your name? ")
    if inp1:
        return inp1
    else:
        print "You must enter your name."
        uname()

def usurname():
    inp2 = raw_input("Your surname? ")
    if inp2:
       return inp2
    else:
        print "You must enter your surname. "
        usurname()

def number():
    inp3 = raw_input("Your number?(optional) ")
    if inp3:
        return inp3
        print "Thank you"
    elif not inp3:
        return "None"


def alldata():
    print "Your name is %s, your surname is %s and your number is %s." % (
        uname(), usurname(), number())

alldata()
"""

a = raw_input("Name? ")
b = raw_input("Surname? ")
c = raw_input("Number? ")

if a and b:
    if c:
        print "Your name is %s, your surname is %s and your number is %s." % (
        a, b, c)
    else:
        print "Your name is %s, your surname is %s. \
You did not entered a number." % (a, b)
else:
    print "Sorry."
    

    
