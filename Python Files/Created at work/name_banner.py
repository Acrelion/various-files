# This script prints a banner of someones name.
# After loading this module, please call the function.
# name - string

def banner(name):
    name_len = len(name) #gets the lenght of the name
    
    middle = "* "        #define the side of the banner

    total_len = name_len + (2 * len(middle) ) #the total lenght of the banner
    full_row = "*" * total_len                #creates the top and bottom rows
  
    middle_whole = middle + name + middle[::-1] #creates middle (with sides)

    # prints the banner, one row per time
    print full_row
    print middle_whole
    print full_row
    
