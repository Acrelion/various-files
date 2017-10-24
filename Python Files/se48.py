from sys import exit

inventory = []

def show_inv():
	print "\nInventory:"
	for i in inventory:
		print i, 
	
	print '\n'
		

def start():
	print "Lets make some great cookies."
	print "You need flour, butter, sugar or eggs. What are you going to get first? Or leave?"
	
	choise1 = raw_input("Flour, butter, suggar, eggs, leave: ")
	choise = choise1.lower()
	
	if choise == "flour":
		def_flour()
	elif choise == "butter":
		def_butter()
	elif choise == "sugar":
		def_sugar()
	elif choise == "eggs":
		def_eggs()
	elif choise == "leave":
			print "Bye."
			here = 0
			exit(0)
	else:
		print "This is a nice recipe. Follow it exactly please."
		exit(0)
		
def def_flour():
	here = 1
	print "\nYou are in front of a large cabinet."
	print "What will you do? Open it or get back to the table where you are cooking?"
	print "You can also leave everything behind if you don't feel cooking at the moment.\n"
	while here == 1:
		input1 = (str(raw_input("Open, back, inv, drop, leave? ").lower()))
		if "open" in input1:
			here = 0
			cabinet()
		elif "back" in input1:
			here = 0
			table()
		elif "inv" in input1:
			show_inv()
		elif "leave" in input1:
			print "\nYou stop looking for ingredients and leave. Bye."
			here = 0
			exit(0)
		else:
			print "I am not sure. I know only 'open' and 'back'.",
			print "Don't stare at the poor cabinet all day!\n"
		
def cabinet():
	print "\nYou are now looking in the cabinet. Inside there are bags of flour and salt."
	print "Will you take the flour, the salt, both or get back to the table? You can drop them later."
	print "Type in inventory to see what you already have.\n"
	here = 1
	flour_taken = 0
	salt_taken = 0
	while here == 1:
		input1 = (str(raw_input(">Get flour, get salt, inv, drop, back, leave? ").lower()))
		if "flour" in input1 and flour_taken != 1:
			print "\nFlour taken."
			flour_taken = 1
			inventory.append('flour')
			input1 = ""
		elif "inv" in input1:
			show_inv()
		elif "flour" in input1 and flour_taken == 1:
			print "\nFlour already taken."
		elif "salt" in input1 and salt_taken != 1:
			print "\nSalt taken."
			salt_taken = 1
			inventory.append('salt')
			input1 = ""
		elif "both" in input1 and ((flour_taken != 1) and (salt_taken != 1)):
			print "\nYou take them both."
			flour_taken = 1
			inventory.append("flour")
			salt_taken = 1
			inventory.append("salt")
			input1 = ""
		elif "salt" in input1 and salt_taken == 1:
			print "\nSalt already taken."
		elif "both" in input1 and ((flour_taken ==1) and (salt_taken == 1)):
			print "You already got both."
		elif "both" in input1 == ((flour_taken != 1) or (salt_taken != 1)):
			print "\nYou already got one. You can't get both like that. Type flour or salt."
		elif "back" in input1:
			here = 0
			table()
		elif "drop" in input1:
			drop_what = (str(raw_input("Which one? ").lower()))
			if drop_what == 'flour':
				inventory.remove('flour')
				flour_taken = 0
			elif drop_what == 'salt':
				inventory.remove('salt')
				salt_taken = 0
		else:
			print "\nNot sure about that. I know only flour, salt, both and back.\n"
			
def table():
	here = 1
	print "\nYou are back to the table now. You now have:", show_inv()
	if ('flour' and 'sugar' and 'eggs' and 'butter') in inventory:
		print "\nYou have all the ingredients. You can start cooking. Let's go."
		here = 0
		inventory.append('mixture')
		cooking()
	print "\nWhat do you want to do now?"
	print "Will you get flour, sugar, eggs, butter or you will start cooking?"
	print "Or drop something? You can also leave everything behind. It's not too late for pizza!\n"
	while here == 1:
		input1 = (str(raw_input("Flour, sugar, eggs, butter, cook, drop, leave? ").lower()))
		if "flour" in input1:
			here = 0
			def_flour()
		elif "sugar" in input1:
			here = 0
			def_sugar()
		elif "butter" in input1:
			here = 0
			def_butter()
		elif "eggs" in input1:
			here = 0
			def_eggs()
		elif "cook" in input1:
			here = 0
			cooking()
		elif "inv" in input1:
			show_inv()
		elif "drop" in input1:
			drop_what = (str(raw_input("Which one? ").lower()))
			if drop_what in inventory:
				inventory.remove(drop_what)
		elif "leave" in input1:
			print "\nYou suspend the cookie making. Maybe later? Bye!"
			here = 0
			exit(0)
		else:
			"\nNot sure. Flour, sugar, eggs, butter, cook, drop, leave is what I understand.\n"
	
def def_butter():
	print "\nYou find a big pot with butter in it. Will you take some, get back or leave everything?"
	print "You can also check what you have in your inventory.\n"
	here = 1
	butter_taken = 0
	while here == 1:
		input1 = (str(raw_input("Get, inv, back, drop, leave? ").lower()))
		if "get" in input1 and butter_taken != 1:
			print "\nButter taken."
			butter_taken = 1
			inventory.append('butter')
			input1 = ""
			honey()
		elif "get" in input1 and butter_taken == 1:
			print "\nButter already taken."
		elif "inv" in input1:
			show_inv()
		elif "back" in input1:
			here = 0
			table()
		elif "leave" in input1:
			print "You leave everything behind."
			here = 0
			exit(0)
		elif "drop" in input1:
			drop_what = (str(raw_input("Which one? ").lower()))
			if drop_what in inventory:
				inventory.remove(drop_what)
		else:
			print "I don't understand. Try butter, inv, back, drop, leave."
			
def honey():
	print "\nAs you take the butter from the pot you see another pot with honey in it."
	print "What do you do? Will you take some, eat some or leave it and get back?"
	print "Or abandon everything because you found something"
	print "sweet and you don't need to make cookies any more?\n"
	here = 1
	honey_taken = 0
	while here == 1:
		input1 = (str(raw_input("Get, yum, inv, drop, back or leave? ").lower()))
		if "get" in input1 and honey_taken != 1:
			print "\nHoney taken."
			inventory.append('honey')
			input1 = ""
		elif "get" in input1 and honey_taken == 1:
			print "\nHoney already taken."
		elif "yum" in input1 or "eat" in input1:
			print "\nYummy! That was delicious! Maybe I should get back.\n"
		elif "inv" in input1:
			show_inv()
		elif "drop" in input1:
			drop_what = (str(raw_input("Which one? ").lower()))
			if drop_what in inventory:
				inventory.remove(drop_what)
		elif "back" in input1:
			here = 0
			table()
		elif "leave" in input1:
			print "\nYou leave everything behind. You have your sweets now......... And I don't have my cookies. Ahhhh."
			here = 0
			exit(0)
		else:
			print "I don't understand. Try get, yum, inv, drop, back or leave.\n"

def def_sugar():
	print "\nSugar time!"
	print "Will you try to get some sugar, check inventory, drop something,\nget back to the table or leave?"
	print "What about the L?\n"
	here = 1
	sugar_taken = 0
	ladder_taken = 'ladder'
	if ladder_taken in inventory:
		while here == 1:
			input1 = (str(raw_input("Get, inv, drop, back, leave? ").lower()))
			if "get" in input1 and ladder_taken != 1:
				print "\nYou use the ladder to get the sugar."
				sugar_taken = 1
				inventory.append('sugar')
				inventory.remove('ladder')
				input1 = ""
			elif "back" in input1:
				here = 0
				table()
			elif "inv" in input1:
				show_inv()
			elif "drop" in input1:
				drop_what = (str(raw_input("Which one? ").lower()))
				if drop_what in inventory:
					inventory.remove(drop_what)
			elif "leave" in input1:
				print "\nYou suspend the cookie making. Maybe later? Bye!"
				here = 0
				exit(0)
			else:
				print "\nI don't understand. Give me get, inv, drop, back, leave."
	elif (ladder_taken in inventory) != 1:
		while here == 1:
			input1 = (str(raw_input("Get, inv, drop, back, leave? ").lower()))
			if "get" in input1 and ladder_taken != 1:
				print "\nThe sugar seems to be in a small cabinet above your head."
				print "Such an inconvenience. You can't reach it without a ladder."
				print "We will need a ladder. Will you search for some in the closet?\n"
				input2 = (str(raw_input("\nGo or stay? ").lower()))
				if "go" in input2:
					here = 0
					ladder()
				elif "stay" in input2:
					here = 0
					def_sugar()
				else:
					"\nChoose in a way I can understand, please."
			elif "get" in input1 and ladder_taken == 1:
				print "You use the ladder to get the sugar."
				sugar_taken = 1
				inventory.append('sugar')
				ladder_taken = 0
				input1 = ""
			elif "back" in input1:
				here = 0
				table()
			elif "inv" in input1:
				show_inv()
			elif "drop" in input1:
				drop_what = (str(raw_input("\nWhich one? ").lower()))
				if drop_what in inventory:
					inventory.remove(drop_what)
			elif "leave" in input1:
				print "\nYou suspend the cookie making. Maybe later? Bye!"
				here = 0
				exit(0)
			else:
				print "\nI don't understand. Give me get, inv, drop, back, leave.\n"
			
def ladder():
	print "\nYou find a ladder in the closet." 
	print "Now you can get it, go back, check you inventory,"
	print "drop something or leave everything and watch TV instead."
	print "Ladders were not in the cookie bargain!\n"
	here = 1
	ladder_taken = 0
	while here == 1:
		input1 = (str(raw_input("Get, inv, drop, stay, back, leave? ").lower()))
		if "get" in input1 and ladder_taken != 1:
			print "\nLadder taken. Let's go get the sugar."
			ladder_taken = 1
			inventory.append('ladder')
			input1 = ""
			here = 0
			def_sugar()
		elif "get" in input1 and ladder_taken == 1:
			print "\nLadder already taken."
		elif "back" in input1:
			here = 0
			table()
		elif "stay" in input1:
			print "\nYou stay and search more in the closet. You find an old lamp. You touch it but nothing happens. Sorry about that. Your Jinn is lazy today."
		elif "inv" in input1:
			show_inv()
		elif "drop" in input1:
			drop_what = (str(raw_input("Which one? ").lower()))
			if drop_what in inventory:
				inventory.remove(drop_what)
		elif "leave" in input1:
			print "\nYou suspend the cookie making. Maybe later? Bye!"
			here = 0
			exit(0)
		else:
			print "I don't understand. Please enter get, inv, drop, stay, back or leave.\n" 
			
def def_eggs():
	print "\nTime to get eggs. They are in the fridge. You open it and there they are."
	print "What will do now? Get them, check your inventory, go back or leave everything?\n"
	here = 1
	eggs_taken = 0
	while here == 1:
		input1 = (str(raw_input("Get, inv, drop, back, leave? ").lower()))
		if "get" in input1 and eggs_taken != 1:
			print "\nEggs taken."
			eggs_taken = 1
			inventory.append('eggs')
			input1 = ""
		elif "get" in input1 and eggs_taken == 1:
			print "\nEggs already taken."
		elif "back" in input1:
			here = 0
			table()
		elif "inv" in input1:
			show_inv()
		elif "drop" in input1:
			drop_what = (str(raw_input("\nWhich one? ").lower()))
			if drop_what in inventory:
				inventory.remove(drop_what)
				eggs_taken = 0
		elif "leave" in input1:
			print "\nYou suspend the cookie making. Maybe later? Bye!"
			here = 0
			exit(0)
		else:
			print "\nI don't understand. Please enter get, inv, drop, back or leave.\n"
			
def cooking():
	print "You combine the ingredients into a smooth mixture and then you shape the cookies up."
	print "Good job!"
	print "Now it's time to bake them. Get the mixture and put it in the oven.\n"
	here = 1
	mixture_taken = 0
	inventory = []
	while here == 1:
		input1 = (str(raw_input("Get, oven, leave? ").lower()))
		if "get" in input1 and mixture_taken != 1:
			mixture_taken = 1
			inventory = []
			inventory.append('mixture')
			input1 = ""
		elif "get" in input1 and mixture_taken == 1:
			print "Mixture already taken."
		elif "oven" in input1:
			here = 0
			def_oven()
		elif "leave" in input1:
			print "\nYou leave everything behind. So sad. You almost made the cookies........ Am I crying?\n"
			here = 0
			exit(0)
			
def def_oven():
	print"\nYou put the mixture into the oven. Count to 3 and get the cookies. Wait until they are not so hot and enjoy them."
	print "I am sure they are great!"
	inventory = []
	inventory.append('cookies')
	print "\nHere they are the mighty cookies!!!\n"
	print "Game over.\n"
	exit(0)
	
start()