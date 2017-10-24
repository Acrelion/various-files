"""
def name1(ask1):
    print "Nice to meet you, %s" % ask1

print

def name2(ask2):
    print "And nice to meet you too, %s" % ask2

inp1 = raw_input("Hi, what is your name? ")
inp2 = raw_input("Heya, what's you name? ")

name1(inp1)
name2(inp2)
"""

def greetings(name1, name2):
    print
    gr = "Nice to meet you, %s and %s" % (inp1, inp2)
    print gr
    if inp1 == "Ivan" and inp2 == "Lora":
        print
        print "Oh, you've unlocked the secret level."
    else:
        print

inp1 = raw_input("What's your name? ")
inp2 = raw_input("And your name is? ")

greetings(inp1, inp2)
