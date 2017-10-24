a = [2, 6, 8, 11, 52, 5]

print len(a)
print "Max is", max(a)
print "Min is", min(a)
print

for b in a:
    if b < 10:
        print b
else:
    print "Done.\n"

for b in a:
	if 5 in a:
		print "5 is item number %d in a.\n" % (a.index(5))
		break
	else:
		print "No 5 in a.\n"
		break