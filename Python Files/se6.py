# Example of how you can use a string and raw_input or just type the string
#inside the () of a raw_input function.

age = raw_input("Your age is? ")
real_age = raw_input("And your real age? ")

print "And what's your name? ",
name = raw_input()


print
print "Ex:1", "So your age is %s." % age

print
print "Ex2:", "So your real age is %s, that's better." % real_age

print
print "Ex3:", "So your real age is %r,\nthats better." % real_age

print
print "Ex4:", "So your age is", age

print
print "Ex5:", "You said that your name is %s." % name
