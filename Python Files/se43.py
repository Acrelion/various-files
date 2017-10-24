def li():
	a = raw_input("Numbers? ")
	b = list(a)
	
	for c in b:
		print c
	li()
	
li()