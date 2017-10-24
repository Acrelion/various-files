import re

a = [1, 2, 3]

print "We have a list:", a
print
print 'The first item in a is', a[0]
print
print "We will change it to a different number. Enter a new one.\n"
inf = 1
while inf > 0:
    
    h = (raw_input("> "))
    if re.match("^[0-9]*$", h):
        h = int(h)
        a.append(h)
        break
    elif not re.match("^[0-9]*$", h):
        print "Not allowed."
        
    

print '\nNow the list looks like this: %s' % a
print '\nLets reverse the list. Press Enter to continue.',
raw_input()
a.reverse()
print "\nThe reversed list is like this: %s\n" % a
print "The first item in the list now is %s" % a[0]

