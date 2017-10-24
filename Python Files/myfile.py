# This script creates a file and reads it.

# In case the file does not exist, use the first part.


# my_file = open("proba.txt", "w")
# my_file.write("Hi\nthere!")
# my_file.close()

for line in open("proba.txt").readlines():
	print line,
