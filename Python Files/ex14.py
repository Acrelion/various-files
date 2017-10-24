# Unpacking multiple variables. Note that we mention them when we write:
# python ex14.py Omicron
# Strings can be made using """  """

from sys import argv

script, user_name = argv
prompt = "Your answer: "

print #empty
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (
likes, lives, computer
)
