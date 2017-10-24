print """To your number will be added 10.
You can do this as many times as u want.
If your number is over 100 the program will stop.
If you need to exit the program, press CTRL + C.
"""

var = 1
while var == 1:
	num0 = raw_input("Your number: ")
	num = int(num0)
	if num + 10 <= 100:
		print "%d + 10 =" % num, (num + 10)
	else:
		var = var + 1
		print "Game over."