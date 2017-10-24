#Creating a class HelloWorld with one method (the __init__ method is created
# internally), which prints the message. Also an instance of the class is
#created and the method is used on it.

class HelloWorld(object):
    def say(self):
        print "Hello World!"

greeting = HelloWorld()
greeting.say()



# The basic way we know and learned when we first started:
# print "Hello world!"
