from os.path import exists

num = 0

def file_not_exists():
    if not exists("settings.txt"):
        return False
    else:
        return True
    
def read_file():
    print "read_file in action"
    return 10

def the_number():
    # gets the number from the file and stores it in ???
    global num
    num = (read_file() if file_not_exists() != False else 10)
    
def minus_one_try():
    global num
    num = num - 1
    
def call_it():
	global num
	if num >= 1:
		if user_input() == 1:
			minus_one_try()
			if num != 0:
				print num # Technical command
			call_it()
	elif num == 0:
		print "Game over."
     
        
def user_input():
    my_input = input("Number? ")
    return my_input
        
        
the_number()
call_it()