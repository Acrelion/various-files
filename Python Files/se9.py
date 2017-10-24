def stihotvorenie(purvi, vtori, treti, chetvurti):
    print "%s is fat." % purvi
    print "%s has a snort." % vtori
    print "%s is kind of girly." % treti
    print "And %s farts.\n" % chetvurti

	
print "Lets see."
p = raw_input("Write a male name: ")
print
v = raw_input("Now write a female name: ")
print
t = raw_input("Write a male name again: ")
print
c = raw_input("Write a female name again please: ")

print
print

stihotvorenie(p, v, t, c)


#If you dont want the user to input stuff, then use such code:
#stihotvorenie("Mia", "Ren", "Jane", "Murry")

