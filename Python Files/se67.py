from sys import exit
a = ["John", 'Lizz']
b = []
print "-" * 6, "List operations. 1.4 by I. Ivanov", "-" * 6

def start():
	print "\nWe have a list 'a':", a
	print "Choose what to do from the list below. \
	Type the number to select."
	print "\t1. Add to the list."
	print "\t2. Delete an item from the list."
	print "\t3. Check the length of the list."
	print "\t4. Copy the list."
	print "\t5. Show the list."
	print "\t6. Exit"
	inp1 = input("O.o/ n: ")
	if inp1 == 1:
		add_some()
	elif inp1 == 2:
		del_some()
	elif inp1 == 3:
		len_some()
	elif inp1 == 4:
		copy_some()
	elif inp1 == 5:
		show_some()
	elif inp1 == 6:
		exit()
	else:
		print "Sorry. Please try again."
		start()
		
def add_some():
	add_this = raw_input("Add what to the list: ")
	a.append(add_this)
	print "Done. Now what?"
	print "\t1. Show the list."
	print "\t2. Go back to the options."
	inp1 = input("O.o/ n: ")
	if inp1 == 1:
		show_some()
	elif inp1 == 2:
		start()
	else:
		print "Sorry. Please try again."
		inp1 = input("O.o/ n: ")

def del_some():
	print "This is your list:", a
	if len(b):
		print "\Copied list:", b
	print "\t1.Delete from list a."
	if len(b) > 0:
		print "\t2. Delete from list b."
	else:
		print
	inpp = input("O.o/ n: ")
	if inpp == 1:
		del_this = input("What item you want to delete from a?  ")
		del a[del_this]
	elif inpp == 2:
		del_this2 = input("What item you want to delete from b?  ")
		del b[del_this2]
	else:
		print "Sorry. Please try again."
		del_some()
	print "Done. Now what?"
	print "\t1. Show the list."
	print "\t2. Go back to the options."
	print "\t3. Delete another item."
	inp1 = input("O.o/ n: ")
	if inp1 == 1:
		show_some()
	elif inp1 == 2:
		start()
	elif inp1 == 3:
		del_some()
	else:
		print "Sorry. Please try again."
		inp1 = input("O.o/ n: ")
		
def len_some():
	print "The length of a is:", len(a)
	if len(b) > 0:
		print "\nThe length of b is:", b
	raw_input("Continue? ")
	print "Now what?"
	print "\t1. Go back to the options. "
	print "\t2. Exit the program."
	inp1 = input("O.o/ n: ")
	if inp1 == 1:
		start()
	elif inp1 == 2:
		exit()
	else:
		print "Sorry. Please try again."
		inp1 = input("O.o/ n: ")
		
def copy_some():
	global b
	b = a[:]
	print "Done. The new list is copied to a variable 'b'."
	print "b:", b
	print "\nNow what?"
	print "\t1. Go back to the options. "
	print "\t2. Exit the program."
	inp1 = input("O.o/ n: ")
	if inp1 == 1:
		start()
	elif inp1 == 2:
		exit()
	else:
		print "Sorry. Please try again."
		inp1 = input("O.o/ n: ")
	return b
		
def show_some():
	if len(b) > 0:
		print "You have 2 lists."
		inp3 = raw_input("Which list do you want to print out?O.o/ n:  ")
		if inp3 == 1:
			print a
		if inp3 == 2:
			print b
		else:
			print "Sorry. Please try again."
			inp3 = raw_input("Which list do you want to print out?O.o/ n:  ")
	else:
		print a
	print "\nNow what?"
	print "\t1. Go back to the options. "
	print "\t2. Exit the program."
	inp1 = input("O.o/ n: ")
	if inp1 == 1:
		start()
	elif inp1 == 2:
		exit()
	else:
		print "Sorry. Please try again."
		inp1 = input("O.o/ n: ")


start()
