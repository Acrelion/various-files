
a = ["John", "Lisa", "Dick", "Jeny", "Katy"]
print a
b = raw_input("Add one more to the list: ")
a.append(b)
print a
c = input("Give me a number(0/5): ")
if c <= len(a):
    print a[c]
else:
    print "Sorry. Try again."
raw_input("I will insert John Smith and Marry Miller. Ready? Press Enter. ")
a = ['John Smith', 'Mary Miller'] + a
print a
a.insert(0, "Lizz")
print a
print a[0]



