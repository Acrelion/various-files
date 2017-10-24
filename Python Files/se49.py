a = ['I', 'v', 'a', 'n']

b = ''.join(a)

print a
print b
print # blank row
print a[0:len(a)]

c = {"name": 'Ivan', 'age': 25}
print c['name'],
print c['age']

d = c['age'] = 'Secret'

print d
print c
del c['age']

print
k = {'heigh': 166, 'weight': 54}
c.update(k)

print c