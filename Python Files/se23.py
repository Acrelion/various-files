inp1 = raw_input("What is your favorite color? ")
a = (inp1 + " ") * 10
b = ("%s " % inp1 + ((" " * len(inp1)) + " ") * 8) + inp1

print
print a
print b
print b
print a

"""
#This is the solution that is in the website.

inp1 = raw_input("What is your favorite color? ")
inp2 = str(inp1)

a = (inp2 + " ") * 10
b = " " * len(inp2)
c = (inp2 + " ") + ((b + " ") * 8) + inp2

print a
print c
print c
print a
"""
