# Looping through a list, printing every item + string.
# In the last line we print index of the elements and then the element itself.
# The element is being selected/called by using its index:
# Give me the element from list animals with index i.

animals = ['bear', 'python', 'peacock', 'kangaroo',
           'whale', 'platypus']

"""
print animals[1], "python"
print animals[2], "peacock"
print animals[0], 'bear'
print animals[3], 'kangaroo'
print animals[4], 'whale'
print animals[2], "peacock"
print animals[5], 'platypus'
print animals[4], 'whale'
"""

for i in range(len(animals)):
    print "Index %d in the list is %s" % (i, animals[i])
