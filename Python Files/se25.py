name = raw_input("Your first name is? ")
family = raw_input("Your last name is? ")
phone = raw_input("Your phone is? ")

if name and family and phone:
    print "Thank you."
else:
    print "Do not leave any fields empty."