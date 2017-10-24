a = []

for i in range(0, 5, 2):
	a.append(i)
	

b = a[1]

if b == 2:
	print b
else:
	print "Error. b is %d" % b