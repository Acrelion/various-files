def boolo(argument):
    if argument == "True":
        return True
    else:
        return False

inp = raw_input("> ")
a = boolo(inp)
print a
print
b = boolo(False)
print b
c = boolo(True)
print c

