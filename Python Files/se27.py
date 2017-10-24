def f1(a1):
    tv1 = a1 * 10
    tv2 = tv1 * 10
    return tv1, tv2
	
var1 = 2
v1, v2 = f1(var1)
v3 = v1 + v2
print v1, v2
print "%d %d" % f1(var1)
print "v1 + v2 = %d" % v3