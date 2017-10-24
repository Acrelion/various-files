# Ex with functions. I am calling functions inside of other functions.
# The script prints out the first and the last word of a given string.
# The function returns its output by using return.



def break_words(stuff):
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)
	
def print_first_word(words):
    word = words.pop(0)
    print word
	
def print_last_word(words):
    word = words.pop(-1)
    print word
	
def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)
	
def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

print_first_and_last("I am a robot")
