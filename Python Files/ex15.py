# Handling files. You must create an object and then put the file into it.
# Then you can manupulate the object.

from sys import argv

script, filename = argv
txt = open(filename)

print "Here is your file %r:" % filename
print
print txt.read()

print
print "Type the filename again:"
file_again = raw_input()

txt_again = open(file_again)

print
print txt_again.read()

txt.close()
txt_again.close()
