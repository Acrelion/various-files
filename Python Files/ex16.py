# Multiple arguments (file name) to unpack. The script is already mentioned.
# Using \n to make a new row. \ is character used for escaping characters.
# \\ is escape for \

from sys import argv

script, filename = argv

print "We are going to open %s." %filename
print "If you dont want that, hit CTRL+C."
print "If you want that, hit Enter."

raw_input("What is going to be? ")

print
print "Opening the file..."
ex16 = open(filename, "a")

print ("Now I am going to ask you for three lines.")

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I am going to write these to the file."

ex16.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally, we close it."
ex16.close()
