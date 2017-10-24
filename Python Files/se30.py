a = 1
b = 0
c = 0
z = 1

"""first block"""
q = (not a)
print q
w = (not b)
print w

print
"""second block """
e = (a or b)
print e
r = (a or z)
print r
t = (b or a)
print r
y = (b or c)
print y

print
"""third block """
u = (a and b)
print u
i = (a and z)
print i
o = (b and a)
print o
p = (b and c)
print p

print
"""fourth block """
s = (not (a or b))
print s
d = (not (a or z))
print d
f = (not (b or a))
print f
g = (not (b or c))
print g

print
"""fifth block """
h = (not (a and b))
print h
j = (not (a and z))
print j
k = (not (b and a))
print k
l = (not (b and c))
print l
