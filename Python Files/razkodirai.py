gg = str(raw_input("The Incripted message: "))
msg = filter(lambda x: x != "X",gg)
print msg[::-1]
