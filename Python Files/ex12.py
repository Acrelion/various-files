# Using the raw_input to get a string like data from the user.
#Input gives us objects.

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print
print ("So you are %r old, %r tall "
"and %r heavy.") % (
age, height, weight)
