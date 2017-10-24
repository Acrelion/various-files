text = "Python!"

box = []
norm = str(text)
x = 0
for n in norm:
    print n, len(n) + x
    x = x + 1
    box.insert(0, n)
print "".join(box)

print "-" * 10



