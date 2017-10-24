def func(inp):
    if int_input <= 10:
        return True

user_input = raw_input("Enter a number between 0 and 10.\n")
int_input = int(user_input)
funkciq = func(int_input)
    
if funkciq == True:
    print "Great. This is:",funkciq
    print
else:
    print "%s is more than 10. This is False" % int_input
