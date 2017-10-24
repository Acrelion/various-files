# Note that it will throw an error if the file does not exists.

def read_file():
	my_file = open("proba.txt", "r")
	data = my_file.read()
	return int(data)

guesses_left = read_file()

while guesses_left > 0:
	print guesses_left
	guesses_left = guesses_left - 1