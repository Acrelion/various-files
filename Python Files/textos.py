import os

def create_file():
	os.chdir("C:/Users/Omicron/Desktop")
	first_file = open ("first.txt", "w")
	first_file.write("C:/Users/Omicron/Desktop/Folder1")
	first_file.close()
	
def read_first():
	os.chdir("C:/Users/Omicron/Desktop")
	read_first_file = open("first.txt")
	readed = read_first_file.read()
	read_first_file.close()
	return os.path.join(readed)
	
	
def make_dir():
	os.mkdir("Folder1")
	
def change_dir():
	
	os.chdir(read_first())
	
def create_second():
	first_file = open ("C:/Users/Omicron/Desktop/first.txt")
	first_data = first_file.read()
	second_file = open("second.txt", "w")
	second_file.write(first_data)
	first_file.close()
	second_file.close()
	
def print_both():
	first_file = open ("C:/Users/Omicron/Desktop/first.txt")
	print first_file.read()
	first_file.close()
	change_dir()
	second_file = open("second.txt")
	print second_file.read()
	second_file.close()
	
	
	
create_file()
read_first()
make_dir()
change_dir()
create_second()
print_both()


