a1 = raw_input("Number? ")
b2 = raw_input("Number? ")

a = int(a1)
b = int(b2)

if a != b:
    a += 1
    print "a is now %d" % a
else: 
    if (a and b) == 2:
        print "They are now two."
    else:
        print "I dont care. a and b are = %d and %d now " % (a, b)
