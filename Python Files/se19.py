"""num1 = raw_input("Write a number, please. ")
inum1 = int(num1)

operation = (((((inum1 + 3) * 2) - 4) - inum1 * 2) + 3)
print
print "New number =", operation
"""

def oper1(number):
    operation = (((((integer_num + 3) * 2) - 4) - integer_num * 2) + 3)
    print "New number:", operation

user_num = raw_input("Tell me a number. ")
integer_num = int(user_num)
oper1(integer_num)
