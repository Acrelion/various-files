# Introducing me to lists and loops. For every item in the list, do something.
# Lists can be sorted and can contain everything - numbers, strings, other lists, etc.
# .append adds a new item at the end of the list.
# Empty list is created by a = []

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
	print "This is count %d" % number

for i in change:
	print "I got %r" % i

elements = []
for i in range(0, 6):
	print "Adding %d to the list" % i
	elements.append(i)
	
for i in elements:
	print "Element was: %d" % i
