import random
from sys import exit

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
	
def user_inp():
	user_input = raw_input("Number? ")
	while input_check(user_input) != True:
		user_input = raw_input("Number? ") # Change 19:32
	else:
		return int(user_input)
	
def user_inp_for_menu():
	user_input = raw_input(">>> ")
	while input_check(user_input) != True:
		user_input = raw_input(">>> ") # Change 19:32
	else:
		return int(user_input)	

def input_check(user_input):
	if str(user_input) in "123456789" and int(user_input) > 0:
		return True
	else:
		return False
		
def ask_user():
	print "Do you want to change the default length of the number?"
	print "1. Yes/ 2. No/ 3. Exit"
	inp1 = user_inp_for_menu()
	while inp1 != 1 and inp1 != 2:
		inp1 = user_inp_for_menu()
	else:
		if inp1 == 1:
			generate_four_digit_number((user_inp()))
		elif inp1 == 2:
			generate_four_digit_number("no")
		elif inp1 == 3:
			exit(0)
			
def main_menu():
	print "1. Generate number with default length."
	print "2. Change the length."
	print "3. Exit"
	inp1 = user_inp_for_menu()
	while inp1 != 1 and inp1 != 2 and inp1 != 3:
		inp1 = user_inp_for_menu()
	else:
		if inp1 == 1:
			generate_four_digit_number("no")
		elif inp1 == 2:
			ask_user()
		elif inp1 == 3:
			exit(0)
			
main_menu()