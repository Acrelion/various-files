"""Creates 2 lists, declared as global variables and changes them. It does
so 2 times. This is only for testing purposes."""

import random

def generate_random_len_for_list():
    return int(random.randint(0, 6))


def generate_list():
    global my_first_list
    my_first_list = list("a" * generate_random_len_for_list())
    return my_first_list

def copy_global_list(def_list):
    global my_second_list
    my_second_list = list(def_list)
    return my_second_list
    
def change_both_lists(def_list, copied_list):
    def_list[0] = "b"
    copied_list[-1] = "b"

def play():

    def_list = generate_list()
    print "This is the default list I created:", def_list

    copied_list = copy_global_list(def_list)
    print "This is the copied list", copied_list

    change_both_lists(my_first_list, my_second_list)

    print "My first list:", my_first_list
    print "M second list:", my_second_list
    print "-" * 15

play()
play()

