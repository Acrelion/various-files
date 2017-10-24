def user(name):
    print "Nice to meet you, %s" % inp1

print

def cond(status):
    if status == "ok" or "fine":
        print "I am glad that you are %s." % status
    elif status == "bad" or "not good":
        print "I am sorry that you feel %s." % status
    else:
        print "I didn't understand. I am sorry."


inp1 = raw_input("Hi, what is your name? ")
user(inp1)
inp2 = raw_input("How are you, %s? " % inp1).lower()
cond(inp2)

    
