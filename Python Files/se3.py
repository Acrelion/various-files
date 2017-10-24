# Do NOT run the program. It's infinite loop.

while True:
  for i in ["/", "-", "|", "\\", "|"] :
    print "%s\r" % i



# The script bellow is my solution to stop the while loop.
"""
simple_list = ["/", "-", "|", "\\", "|"] 
a = 0

while a < 2 * len(simple_list):
  for i in simple_list:
    print "%s\r" % i
    a = a + 1
"""
