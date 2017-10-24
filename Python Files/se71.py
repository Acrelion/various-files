from os.path import exists
settings_file = "proba.bin"

default_setting_for_digits = bin(4)
default_setting_for_difficulty = bin(10)

def insert_default_values():
	my_default_dictionary = str({1: default_setting_for_digits, 2: default_setting_for_difficulty})
	return my_default_dictionary
	
def insert_user_values():
	my_user_dictionary = str({1: replace_value_for_digits(), 2: replace_value_for_difficulty()})


def replace_value_for_digits():
	replace_value_for_digits = input("Enter value for digits: ")
	return bin(replace_value_for_digits)
	
def replace_value_for_difficulty():
	replace_value_for_difficulty = input("Enter value for difficulty: ")
	return bin(replace_value_for_difficulty)


def print_def():
	with open(settings_file, "w") as some_text_file:
		some_text_file.write(insert_default_values())

	with open(settings_file, "r") as a_name:
		settings_returned = eval(a_name.read())
		print int(settings_returned[1], 2)
		print int(settings_returned[2], 2)
	if not a_name.closed():
		a_name.close()

def print_user_main():
	choise = raw_input("1(W)/ 2(R)? ")
	if choise == 1:
		print_user_1()
	if choise == 2:
		print_user_2()

def print_user_1():
	with open(settings_file, "w") as opened_for_write_again:
		return opened_for_write_again.write(str(insert_user_values())
	
def print_user_2():	
	do_it = open(settings_file, "r").read():
	show_me_new = eval(do_it.read())
	end_print()


def end_print():		
	print int(show_me_new[1], 2)
	print int(show_me_new[2], 2)
		
		
def start_all():
	print "1. Default settings"
	print "2. User settings"
	choose_action = input("Choose action: ")
	if choose_action == 1:
		print_def()
	elif choose_action == 2:
		print_user_main()
	else:
		choose_action = input("Choose action: ")
		
start_all()