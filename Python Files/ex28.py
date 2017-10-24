# Practice of boolean logic. Every line should be True or False
# First it is evaluated "not", then "and" and lastly "or". () are as usual.

a = True and True
print a, "I think it's True"
b = False and True
print b, "I think it's False"
c = 1 == 1 and 2 == 1
print c, "I think it's False"
d = "test" == "test"
print d, "I think it's True"
i = 1 == 1 or 2 != 1
print i, "I think it's True"
f = True and 1 == 1
print f, "I think it's True"
g = "test" == "testing"
print g, "I think it's False"
h = 1 != 0 and 2 == 1
print h, "I think it's False"
j = "test" != "testing"
print j, "I think it's True"
k = "test" == 1
print k, "I think it's False"
l = not (True and False)
print l, "I think it's True"
m = not (1 == 1 and 0 != 1)
print m, "I thinks it's False"
n = not (10 == 1 or 1000 == 1000)
print n, "I think it's False"
o = not (1 != 10 or 3 == 4)
print o, "I think it's False"
p = not ("testing" == "testing" and "Zed" == "Cool Guy")
print p, "I think it's True"
q = 1 == 1 and (not ("testing" == 1 or 1 == 0))
print q, "I think its True"
r = "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
print r, "I think it's False"
u = 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
print u, "I think it's False"
