
"""
def censor(text, word = [0, len()]):
    new = text.split(" ")
    
    return text.replace(word, ast)

print censor(text, word)  
"""


input = str(raw_input("Go go go: "))
new = input.split(" ")
print new
b = []
ast = "ast"
for i in new:
	#b = str(i[:-2]) + "ast"
	b = i.replace((i[-3:-1]), ast)

print " ".join(b)
"""
for i in new:
	new.append("ast")
	
print new
"""