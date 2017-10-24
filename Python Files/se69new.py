##############################################
# Cows and Bulls game. Console version.
# Last edited by I.Ivanov, 28.10.2014
# The program can save the user's preferences
# to a binary file in the same directory.
#
##############################################

import random
from sys import exit
from os.path import exists

# Global variables used for default settings.

settings_file = "settings.bin"
guesses_left = 10
default_setting_for_digits = bin(4)
default_setting_for_difficulty = bin(10)

def file_not_exists():
	"""
	Function checks if the settings file exists.
	If it does, it returns the value for number of digits.
	"""
	if not exists(settings_file):
		return False
	elif exists(settings_file):
		return read_file()
		
def file_not_exists_2():
	"""
	Function checks if the settings file exists.
	If it does, it returns the value for difficulty.
	"""
	if not exists(settings_file):
		return 10
	elif exists(settings_file):
		return read_file_2()
		
	
def insert_default_values():
	"""
	If there is no settings file present, the game
	starts with the default values for digits and difficulty.
	"""
	my_default_dictionary = str({1: default_setting_for_digits, 2: default_setting_for_difficulty})
	return my_default_dictionary
	
def insert_user_values():
	"""
	Gets the user's input and conveys it to
	write_user() to be written in a settings file.
	"""
	my_user_dictionary = str({1: bin(user_inp()), 2: bin(user_inp())})
	return my_user_dictionary
		
def write_def():
	"""Writes the default values to the file in binary format. """
	open_fle_w = open(settings_file, "w")
	write_data = open_fle_w.write(insert_default_values())
	open_fle_w.close()
	
def write_user():
	"""Writes the user defined settings to a file in binary format. """
	open_fle_w = open(settings_file, "w")
	write_data = open_fle_w.write(insert_user_values())
	open_fle_w.close()
	play()

def read_file(): 	# TO DO: Add a check if the file is empty. If it is, use default values.
	"""Opens the file and reads the file. Returns an integer with base 2. """
	open_fle_r = open(settings_file, "r")
	read_data_str = open_fle_r.read()
	read_data_eval = eval(read_data_str)
	# read_data_eval becomes dict from str
	return int(read_data_eval[1], 2)
	
def read_file_2():
	"""Does the same like the function above except it is used by different function."""
	open_fle_r = open(settings_file, "r")
	read_data_str = open_fle_r.read()
	read_data_eval = eval(read_data_str)
	# read_data_eval becomes dict from str
	return int(read_data_eval[2], 2)

def user_inp():
	"""Accepts the user input while playing. It is checked if it is valid before passed over."""
	user_input = raw_input("Number? ")
	while input_check(user_input) != True:
		user_input = raw_input("Number? ") 
	else:
		return int(user_input)
	
def user_inp_for_menu():
	"""Same as above. Used in the menu where options are represented by single digits."""
	user_input = raw_input(">>> ")
	while input_check(user_input) != True:
		user_input = raw_input(">>> ") # Change 19:32
	else:
		return int(user_input)	

def input_check(user_input):
	"""Check if the user input is digit and if that digit is positive number."""
	if user_input.isdigit() and int(user_input) > 0:
		return True
	else:
		return False
		
def ask_user():
	"""Changes the settings for the game. They are being written into a file."""
	print "\nDefault value for number of digits is 4 and for difficulty is 10."
	print "Please note that you can only change them at the same time."
	print "Digits range: 3-7/ Difficulty: 2- 50.\n"
	print "Do you want to change the values for the number of digits and difficulty?"
	print "1. Yes/ 2. No/"
	inp1 = user_inp_for_menu()
	while inp1 != 1 and inp1 != 2:
		inp1 = user_inp_for_menu()
	else:
		if inp1 == 1:
			write_def()
			write_user() 
		elif inp1 == 2:
			play()

			
	
def is_number_unique(my_list): #########################
	"""Checks if every digit in the generated number is unique."""
	checked = []
	for digit in my_list:
		if digit not in checked:
			checked.append(digit)
	while len(checked) < len(my_list): # Change 23.9.14
		return False
	else:
		return True
		

def generate_four_digit_number(x):
	""""Generates a four digit number by default or at user defined range. We will have to guess it."""
	if x == False:
		return_list = [0] * 4
	elif x:
		return_list = [0] * x
	else:
		print "Problem."

	for index in range(len(return_list)):
		return_list[index] = random.randint(0,9)
	return return_list
	
def guessing_number():
	"""Function to give us a four digit number. Check if its sufficient. If not, calls the generator again."""
	return_list = generate_four_digit_number(file_not_exists())
	while is_number_unique(return_list) != True:
		return_list = generate_four_digit_number(file_not_exists())
	return return_list
	
def get_user_input():
	user_input = raw_input("Your guess: ")
	while is_user_input_valid(user_input) != True:
		user_input = raw_input("Your guess: ")
	else:
		return user_input
		
def is_user_input_valid(input_to_check):
	if not input_to_check.isdigit():
		return False
	if file_not_exists() == False: ##################################
		if len(input_to_check) != 4: 
			return False
	if file_not_exists():
		if len(input_to_check) != read_file():
			return False # Last edited 1:26, 24.9.2014
			
	for item in input_to_check:
		if int(item) < 0 or int(item) > 9:
			return False
	return is_number_unique(input_to_check)
	
def guess(guessing_list): # Changed: 10.10.2014, 17:46
	""""Most important function. Compares the generated number with the users guess.
		Also counts the number of turns remaining.
		Cows and bulls are determined by adding 1 or 2 into a new list. If there are [2, 2, 2, 2] by
		default, player wins the game."""
	global guesses_left
	
	if guesses_left == 0:
		print "You ran out of guesses. Game over!\n"
		print "Press any key to continue."
		raw_input()
		play()
	else:
		
		print "Guesses left %d.\n" % guesses_left
		guesses_left -= 1
		user_input = get_user_input()
		bulls_count = 0
		bulls_indexes = [0] * (read_file() if file_not_exists() != False else 4) 
		cows_count = 0
		

			#print "You have %d left.\n" % guesses_left
			
		for index in (range(len(user_input))):
			if int(user_input[index]) == int(guessing_list[index]):
				bulls_count += 1
				bulls_indexes[index] = 1
			
		for index1 in (range(len(user_input))):
			for index2 in (range(len(guessing_list))):
				if int(user_input[index1]) == int(guessing_list[index2]):
					if bulls_indexes[index1] != 1 and bulls_indexes[index2] !=1:
						cows_count += 1
						break

		if bulls_count == (read_file() if file_not_exists() != False else 4): ################################ TO DO: Check if it works. 18:47, It was 4.
			print "Congratulations, you win!\n"
			play()
		else:
			print "\nYou have %d bull%s and %d cow%s.%s" % (
			bulls_count, "s" if bulls_count != 1 else "", cows_count, "s" if cows_count \
			!= 1 else "", " Nice Try!" if bulls_count > 2 else "")
			
			guess(guessing_list)		
		
		
def play():
	"""Control function which starts the game. Acts as a hub."""
	print "\n", "-" * 10, "Cows and Bulls 2.0", "-" * 10, "\n"
	print "\t1. Play the game."
	print "\t2. Settings."
	print "\t3. Help."
	print "\t4. Exit"
	print "\n", "-" * 10, "I&Dinc. Have fun!!!", "-" * 10, "\n"
	user_select_option = user_inp_for_menu()
	while user_select_option != 1 and user_select_option != 2 and user_select_option != 3 and user_select_option != 4:
		user_select_option = user_inp_for_menu()
	if user_select_option == 1:
		if file_not_exists() != False:
			print "Your currents settings are %d for digits and %d for difficulty.\n" % (
				read_file(), read_file_2())
		global guesses_left
		guesses_left = (read_file_2() if file_not_exists_2() != 10 else 10)
		guessing_list = guessing_number()
		guess(guessing_list)
	elif user_select_option == 2:
		ask_user()
	elif user_select_option == 3:
		help()
	elif user_select_option == 4:
		exit(0)
	else:
		user_select_option = input("\nEnter a number to choose: ")
	
def help():
	"""Function which gives the rules of the game."""
	print "-" * 10, "Rules", "-" * 10
	print "\n You are required to enter a four digit number (You can change the settings)."
	print "\t1. It must have unique digits only."
	print "\t2. If you guess the number and its position, that's a Bull."
	print "\t3. If you only guess the number but not its position, that's a Cow."
	print "\t4. Find out where all the bulls are to win.\n"
	print "-" * 10, "Rules", "-" * 10
	raw_input("\nPress Enter\\Return to go back to the main menu.\n")
	play()

play()