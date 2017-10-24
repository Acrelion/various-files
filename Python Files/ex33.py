# Ex for while loops. While the condition is met or not met, do this.
# There are infinite loops which must be avoided.

a = 0
chisla = []
b = 1

while a < 6:
	print "At the top a is %d" % a
	chisla.append(a)
	
	a += b
	print 'Chislata now: ', chisla
	print "At the bottom a is %d\n" % a
	
print "The numbers: "
for c in chisla:
	print c
