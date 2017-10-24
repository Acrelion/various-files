a = 4
b = 3
c = 2

q = (a and b)
w = ( not a and b)
e = (not (a and b))
r = (a or b)
t = (a or not b)
y = (not (a or b))
u = (a and (a or b))
i = (a and b and c)
o = (a and b or c)
p = (a and (b or c))
s = ((a and b) or c)

print
print a, b, c

if (a and b):
    print "(%d and %d) True" % (a, b), q
else:
    print "(%d and %d) False" % (a, b), q

if ( not a and b):
    print "(not %d and %d) True" % (a, b), w
else:
    print "(not %d and %d) False" % (a, b), w

if (not (a and b)):
    print "(not (%d and %d)) True" % (a, b), e
else:
    print "(not (%d and %d)) False" % (a, b), e

if (a or b):
    print "(%d or %d) True" % (a, b), r
else:
    print "(%d or %d) False" % (a, b), r

if (a or not b):
    print "(%d or not %d) True" % (a, b), t
else:
    print "(%d or not %d) False" % (a, b), t

if (not (a or b)):
    print "(not (%d or %d)) True" % (a, b), y
else:
    print "(not (%d or %d)) False" % (a, b), y

if (a and (a or b)):
    print "(%d and (%d or %d)) True" % (a, a, b), u
else:
    print "(%d and (%d or %d)) True" % (a, a, b), u

if (a and b and c):
    print "(%d and %d and %d) True" % (a, b, c), i
else:
    print "(%d and %d and %d) False" % (a, b, c), i

if (a and b or c):
    print "(%d and %d or %d) True" % (a, b, c), o
else:
    print "(%d and %d or %d) False" % (a, b, c), o

if (a and (b or c)):
    print "(%d and (%d or %d)): True" % (a, b, c), p
else:
    print "(%d and (%d or %d)): False" % (a, b, c), p

if ((a and b) or c):
    print "((%d and %d) or %d) True" % (a, b, c), s
else:
    print "((%d and %d) or %d) False" % (a, b, c), s
