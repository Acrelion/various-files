# Let's try out the os.walk function.

import os

path = "D:\Ivan\Multimedia\My music\Personal created"

for path, dirs, files in os.walk(path):

	print path
	print dirs
	print files
	print "********"
	print len(files)
	

	
