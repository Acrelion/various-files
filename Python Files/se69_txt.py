import random
from sys import exit
from os.path import exists
print "*" * 10, "Welcome to Bulls and Cows!", "*" * 10
settings_file = "settings_bulls_cows.bin"
default_setting_for_digits = bin(4)
default_setting_for_difficulty = bin(10)
custom_setting_for_digit = ""
custom_setting_for_difficulty = ""


def insert_default_values():
	my_default_dictionary = {1: default_setting_for_digits, 2: default_setting_for_difficulty}
	return my_default_dictionary
	
my_default_dictionary = insert_default_values()


def is_number_unique(my_list):
	if my_list[0] == 0 or\
	my_list[0] == my_list[1] or\
	my_list[0] == my_list[2] or\
	my_list[0] == my_list[3] or\
	my_list[1] == my_list[2] or\
	my_list[1] == my_list[3] or\
	my_list[2] == my_list[3]:
		return False
	else:
		return True

def generate_four_digit_number():
	if not settings_file:
		return_list = [0] * int(default_setting_for_digits)
	elif settings_file:
		if int(default_setting_for_digits) != int(custom_setting_for_digit, 2):
			return_list = [0] * int(custom_setting_for_digit, 2)
		else:
			return_list = [0] * int(default_setting_for_digits)
	for index in range(len(return_list)):
		return_list[index] = random.randint(0,9)
	return return_list
	
def guessing_number():
	return_list = generate_four_digit_number()
	while is_number_unique(return_list) != True:
		return_list = generate_four_digit_number()
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
	if len(input_to_check) != 4:
		return False
	for item in input_to_check:
		if int(item) < 0 or int(item) > 9:
			return False
	return is_number_unique(input_to_check)
	
def guess(guessing_list):
	user_input = get_user_input()
	bulls_count = 0
	bulls_indexes = [0] * 4
	cows_count = 0
	
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

	if bulls_count == 4:
		print "Congratulations, you win!"
		exit(0)
	else:
		print "You have %d bull%s and %d cow%s.%s" % (
	bulls_count, "s" if bulls_count != 1 else "", cows_count, "s" if cows_count \
	!= 1 else "", " Nice Try!" if bulls_count > 2 else "")
		guess(guessing_list)

def play():
	print "\t1. Play the game."
	print "\t2. Settings."
	print "\t3. Help."
	print "\t4. Exit"
	if not exists(settings_file):
		creating_file_with_def_values()
	user_select_option = input("\nEnter a number to choose: ")
	if user_select_option == 1:
		guessing_list = guessing_number()
		guess(guessing_list)
	elif user_select_option == 2:
		settings()
	elif user_select_option == 3:
		help()
	elif user_select_option == 4:
		exit(0)
	else:
		user_select_option = input("\nEnter a number to choose: ")
		
def settings():
	print "-" * 10, "Settings", "-" * 10
	print "\t1. Select number of digits to play with. Default = 4. Range 4-7."
	print "\t2. Select difficulty. Default = 10 tries. Range: 5 - 30."
	print "\t3. Go back to main menu."
	
	option_selected = input("\n Choose an option: ")
	if option_selected == 1:
		option_chosen_1()
	elif option_selected == 2:
		option_chosen_2()
	elif option_selected == 3:
		play()
	else:
		option_selected = input("\n Choose an option: ")
		
def creating_file_with_def_values():
		with open(settings_file, "w") as some_text_file:
			some_text_file.write(str(insert_default_values()))
			
	
def option_chosen_1():
	if exists(settings_file):
		with open(settings_file, "r") as settings_opened:
			settings_returned = eval(settings_opened.readline())
			print "\nCurrent number of digits:", int(settings_returned[1], 2)
		change_digits = input("\n1. Change/ 2. Leave:")
		if change_digits == 1:
			custom_setting = my_default_dictionary[1]= number_of_digits()
			with open(settings_file, "rb+") as entering_change_to_digits:
				custom_setting_for_digit = (entering_change_to_digits.write(str(custom_setting)))
				print "Done."
			settings()
		elif change_digits == 2:
			settings()
		else:
			change_digits = input("1. Change/ 2. Leave:")
	else:
		if not exists(settings_file):
			creating_file_with_def_values()
			
			
def option_chosen_2():
	if exists(settings_file):
		with open(settings_file, "r") as reading_from_file:
			settings_returned2 = eval(reading_from_file.readline())
			print "\nCurrent difficulty:", int(settings_returned2[2], 2)
		change_difficulty = input("\n1. Change/ 2. Leave:")
		if change_difficulty == 1:
			custom_setting = my_default_dictionary[2]= difficulty()
			with open(settings_file, "rb+") as entering_change_to_dfficulty:
				custom_setting_for_difficulty = entering_change_to_dfficulty.write(str(custom_setting))
				print "Done."
			settings()
		elif change_difficulty == 2:
			settings()
		else:
			change_difficulty = input("1. Change/ 2. Leave:")
	else:
		if not exists(settings_file):
			creating_file_with_def_values()


def number_of_digits():
	user_input_for_digits = input("Digits: ")
	if user_input_for_digits >= 4 and user_input_for_digits <=7:
		return bin(user_input_for_digits)
	else:
		user_input_for_digits = input("Digits: ")
	
def difficulty():
	user_input_for_difficulty = input("Difficulty: ")
	if user_input_for_difficulty >= 5 and user_input_for_difficulty <=30:
		return bin(user_input_for_difficulty)
	else:
		user_input_for_difficulty = input("Difficulty: ")

def help():
	print "-" * 10, "Rules", "-" * 10
	print "\n You are required to enter a four digit number."
	print "\t1. It has to have unique digits only."
	print "\t2. If you guess the number and its position, that's a Bull."
	print "\t3. If you only guess the number but not its position, that's a Cow."
	print "\t4. Score four Bulls to win."
	raw_input("\nPress Enter\\Return to go back to the main menu.\n")
	play()
	
	
play()