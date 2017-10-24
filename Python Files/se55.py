# This script replaces the word with * in two different ways

text = "This is hard"
word = "hard"

# This is v1
new = text.split(" ")
ast = "*" * len(word)
ls = []
for i in new:
    if i == word:
        ls.append(ast)
    else:
        ls.append(i)
print " ".join(ls)


#This is v2
def censor(text, word):
    new = text.split(" ")
    ast = "*" * len(word)
    return text.replace(word, ast)

print censor(text, word)   