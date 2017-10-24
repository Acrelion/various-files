inp0 = raw_input("Enter a number between 0 and 9: ")
inp = int(inp0)
numbers = []

print
print "-" * 10

while inp < 10:
    print inp
    numbers.append(inp)
    inp = inp + 1

print "-" * 10
print
print "Current list's lenght:", len(numbers)


