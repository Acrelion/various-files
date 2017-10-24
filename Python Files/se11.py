def grubo(a, b):
    return "%s is fat and %s is stupid.\n" % (a, b)
	
print "Let's offend two people.\n"
inp1 = raw_input("Name? ")
inp2 = raw_input("Second name? ")

obida = grubo(inp1, inp2)

print # blank row
print obida
print # blank row
print "Do you want to write it to a file?",
print "Press Enter to continue or CTRL+C to abort."
raw_input()

create_file = raw_input("Name the file and don't forget the extension: ")
open_file = open(create_file, "w").write(obida)

print # blank row
print "Done.\n"