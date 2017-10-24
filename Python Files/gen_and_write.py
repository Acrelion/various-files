# Generates a four digit number and writes it down into a file.

import random
from sys import exit
from os.path import exists

settings_file = "proba.bin"

default_setting_for_digits = bin(4)
default_setting_for_difficulty = bin(10)

def generate_four_digit_number(x):
	if x == "no":
		return_list = [0] * 4
	elif x:
		return_list = [0] * x
	else:
		print "Problem."
			
	for index in range(len(return_list)):
		return_list[index] = random.randint(0,9)
	print return_list

def file_not_exists():
	if not exists(settings_file):
		print "File does not exists. So I will use default value for digits.\n"
		return "no"
	elif exists(settings_file):
		return read_file()
	
def insert_default_values():
	my_default_dictionary = str({1: default_setting_for_digits, 2: default_setting_for_difficulty})
	return my_default_dictionary
	
def insert_user_values():
	my_user_dictionary = str({1: bin(user_inp()), 2: bin(user_inp())})
	return my_user_dictionary
		
def write_def():
	open_fle_w = open(settings_file, "w")
	write_data = open_fle_w.write(insert_default_values())
	open_fle_w.close()
	
def write_user():
	open_fle_w = open(settings_file, "w")
	write_data = open_fle_w.write(insert_user_values())
	open_fle_w.close()

def read_file(): 	# TO DO: Add a check if the file is empty. If it is, use default values.
	open_fle_r = open(settings_file, "r")
	read_data_str = open_fle_r.read()
	read_data_eval = eval(read_data_str)
	# read_data_eval becomes dict from str
	return int(read_data_eval[1], 2)
		
	
def user_inp():
	user_input = raw_input("Number? ")
	while input_check(user_input) != True:
		user_input = raw_input("Number? ") 
	else:
		return int(user_input)
	
def user_inp_for_menu():
	user_input = raw_input(">>> ")
	while input_check(user_input) != True:
		user_input = raw_input(">>> ") # Change 19:32
	else:
		return int(user_input)	

def input_check(user_input):
	#if str(user_input) in "1234567890" and int(user_input) > 0: 22:19, 20.9.2014
	if user_input.isdigit() and int(user_input) > 0:
		return True
	else:
		return False


	
		
def ask_user():
	print "Do you want to change the default length of the number?"
	print "1. Yes/ 2. No/ 3. Cancel"
	inp1 = user_inp_for_menu()
	while inp1 != 1 and inp1 != 2 and inp1 != 3:
		inp1 = user_inp_for_menu()
	else:
		if inp1 == 1:
			write_def()
			write_user() 
		elif inp1 == 2:
			generate_four_digit_number("no")
		elif inp1 == 3:
			main_menu()
			
def main_menu(): # ->
	print "1. Generate number with default length."
	print "2. Change the length."
	print "3. Exit"
	print "4. To write default values." #TO DO: Delete this when done.
	inp1 = user_inp_for_menu()
	while inp1 != 1 and inp1 != 2 and inp1 != 3 and inp1 != 4: # TO DO: Delete 4 when done.
		inp1 = user_inp_for_menu()
	else:
		if inp1 == 1:
			generate_four_digit_number(file_not_exists())
		elif inp1 == 2:
			ask_user()
		elif inp1 == 3:
			exit(0)
		elif inp1 == 4: # TO DO: Delete
			write_def() # - // -
			
main_menu()
