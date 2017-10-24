import random
from sys import exit

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
	return_list = [0] * 4
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
	print "*" * 10, "Welcome to Bulls and Cows!", "*" * 10
	print "\n You are required to enter a four digit number."
	print "\t1. It has to have only unique digits."
	print "\t2. If you guess the number and its position, that's a Bull."
	print "\t3. If you only guess the number but not its position, that's a Cow."
	print "\t4. Score four Bulls to win.\n"
	guessing_list = guessing_number()
	guess(guessing_list)

play()