from os.path import exists
settings_file = "proba.bin"

default_setting_for_digits = bin(4)
default_setting_for_difficulty = bin(10)

def insert_default_values():
	my_default_dictionary = str({1: default_setting_for_digits, 2: default_setting_for_difficulty})
	return my_default_dictionary

def write_def():
	open_fle_w = open(settings_file, "w")
	write_data = open_fle_w.write(insert_default_values())
	open_fle_w.close()

	
def read_file():
	if not exists(settings_file):
		write_def()
		read_file()
	else:
		open_fle_r = open(settings_file, "r")
		read_data_str = open_fle_r.read()
		read_data_eval = eval(read_data_str)
		# read_data_eval becomes dict from str
		print int(read_data_eval[1], 2)
		print int(read_data_eval[2], 2)

		
		
def start_all():
	print "1. Write with default settings."
	print "2. Read the file."
	choose_action = input("Choose action: ")
	while choose_action != 1 and choose_action != 2:
		choose_action = input("Choose action: ")
	else:
		if choose_action == 1:
			write_def()
		if choose_action == 2:
			read_file()

start_all()