for ne6to in xrange(0, 10, 2):
    if ne6to == 6:
        continue
    print ne6to

print

computer_brands = ['Asus', "Apple", "Dell", "Lenovo", "MSI", "Acer", "Toshiba"]
var1 = 0
print "Lenght of the list is:", len(computer_brands)
while var1 < len(computer_brands):
    print computer_brands[var1]
    var1 = var1 + 1
    if var1 == 5:
            break

print
a = raw_input("Enter a number between 0 and 99: ")
a = int(a)

if a <= 99:
    print "Good job!"
else:
    print "Number is too large."

print
b = raw_input("Type Day or Night: ")

if b == "Day":
    print "There is the sun."
elif b == "Night":
    print "There is the moon"
else:
    print "Bad choise."
