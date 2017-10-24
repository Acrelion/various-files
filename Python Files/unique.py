import random


def generate_four_digit_number(x):
	return_list = [0] * x
			
	for index in range(len(return_list)):
		return_list[index] = random.randint(0,9)
	return return_list
	
	
def is_number_unique(my_list): #########################
	checked = []
	for digit in my_list:
		if digit not in checked:
			checked.append(digit)
	while len(checked) < len(my_list): # Change 23.9.14
		return False
	else:
		return True	
		
def guessing_number():
	return_list = generate_four_digit_number(user_inp())
	while is_number_unique(return_list) != True:
		return_list = generate_four_digit_number(user_inp())
	return return_list
	
def user_inp():
	user_input = raw_input("Number? ")
	return int(user_input)



		
def ask_user():
	print "\nGenerating number:\n"
	z = guessing_number()
	print z
			
ask_user()
