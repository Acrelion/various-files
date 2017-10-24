import re
a = True
c = 0

while a:
	if c == 0:
		print "I love you. Do you love me?\n"
	elif c > 0:
		print "\nTell me that you love me again! ^^"

	b = raw_input("Yes or no? ").lower()
	if re.match("^[A-Za-z-_-]*$", b):
		if 'yes' in b and c == 0:
			print "OMG, you love me! I want to repeat that."
			c = c + 1
		elif ('yes' in b) and c != 0:
				print "OMG, you love me! I want to repeat that again!"
				c = c + 1
		elif 'no' in b:
			print "I am so sad. I am out of here."
			a = False
		else:
			print "I did not understand.\n"
			c = 0
	else:
		print "I did not understand.\n"
		c = 0
		