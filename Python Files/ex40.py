# Introduction to classes.
# The class is just a template for creating objects with the same properties
# as the class. Every such object is called instance of the class.
# You need to have __init__ method to initialise the class and self to
# point towards it.

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song([
"Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
