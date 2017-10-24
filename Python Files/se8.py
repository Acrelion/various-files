from sys import argv
from os.path import exists

script, sample_file = argv

print "File do exist: %s" % exists(sample_file)

print "I am opening the %s" % sample_file

print
#inputf = open(sample_file, "a")
new_text = raw_input("Write here the new text you want to be in the file. \n")
#inputd = inputf.write(new_text)
input1 = open(sample_file, "a").write("\n" + new_text)

print "File's lenght: %d." % len(str(input1))
print

#input1.close()


print "Do you want to see the new text? Press Enter, otherwise - CTRL+C."
raw_input()
#new_open = open(sample_file)
#again = new_open.read()
input2 = open(sample_file).read()
print input2

print
print "That's it. I will close the file."

#input2.close()



