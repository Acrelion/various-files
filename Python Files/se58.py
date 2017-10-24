# Both functions are correct. The first is mine.
"""
def median(x):
    if len(x) % 2 == 0:
        a = len(x) / 2
        b = a - 1
        c = (x[a] + x[b]) / 2.0
        return c
    elif len(x) == 1:
        return x[0]
    else:
        d = len(x) / 2
        return x[d]
"""



def median(numbers):
    x = sorted(numbers)
    y = len(x)
    if y == 1:
        return x[0]
    elif y % 2 == 0:
        return (x[y / 2] + x[((y / 2) - 1)]) / 2.0
    else:
        return x[y / 2]


g = median([4, 5, 5, 4])
y = median([1, 2, 4, 3])
k = median([1])
l = median([1, 4, 7, 8, 9, 10, 20])
p = median([3, 5, 2, 8])

print g
print y
print k
print l
print p
