# Functions! First lesson. We have a function with 2 arguments.
# You call the function multiple times by using numbers, variables
# and variables + numbers.

def cheese_and_crackers(cheese, crackers):
 print "You have %d cheeses!" % cheese
 print "You have %d boxes of crackers!\n" % (
 crackers)
 
print ("We can just give the function numbers "
"directly:")
cheese_and_crackers(20, 30)


print "Or, we can use variables from our script:"
cheese = 10
crackers = 50

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(cheese + 100, crackers + 1000)

