# The scripts prompts for a file name, opens it and attempts to
# find and print out the longest and the shortest word in the file.
import string

file_name = raw_input("Enter file name: ")
try:
    handler = open(file_name, 'r')
except:
    print "File name error."
    exit()

counts = dict()

for line in handler:
    line = line.translate(None, string.punctuation)
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[len(word)] = word

    
word_lens = []
for i in counts:
    word_lens.append((i, counts[i]))


word_lens.sort(reverse=True)

for item in word_lens:
    if item[0] >= word_lens[0][0]:
        print "Longest word is \"%s\" with lenght of (%d) characters." % (
            item[1], item[0])
    if item[0] <= word_lens[-1][0]:
        print "Shortest word is \"%s\" with lenght of (%d) character%s." % (
            ( item[1].upper() if item[1] == 'i' else item[1]),
            item[0], ('s' if item[0] != 1 else ""))

# Should never forget to close the files which I've opened.
handler.close()
