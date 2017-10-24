from sys import argv
script, out_file = argv

def always(a, b):
    return "%s + %s = Always together" % (a, b)
	
inp1 = raw_input("She ")
inp2 = raw_input("He ")
zaedno = always(inp1, inp2)

print zaedno
open_file = open(out_file, "w").write(zaedno)
