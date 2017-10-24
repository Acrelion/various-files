print (" " * 8), "Vanast ast Raast ast pichoast!"
print "Napisast -> stop <- ast ast spreast programaast"
print (" " * 8), "-" * 29
c = 0
v = 0
while v < 20:
    text = raw_input("\n> ")
    new = text.split(" ")
    if "stop" in new:
        break
    elif "zmei" and "golem" in new:
        print "Ti si mngo golem Zmei, ei!"
    else:
        print
        for i in new:
            print i[0:-2] + "ast",
            c += 1
            v += 1
else:
    print "20 puti stigat. Spri za edna minuta."



# print i[0:-2] + i[len((new[c])) - 2] + "ast",
