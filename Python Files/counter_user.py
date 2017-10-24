# The script prompts for a string, then it attempts to print out the
#longest and the sortest word in it.
import string

txt = raw_input("Enter some text: ")
txt = txt.translate(None, string.punctuation)
txt = txt.lower()
words = txt.split()
word_lens = list()

for word in words:
    word_lens.append((len(word), word))

word_lens.sort(reverse=True)

for item in word_lens:
    if item[0] >= word_lens[0][0]:
        print "Longest word is \"%s\" with lenght of (%d) characters." % (
            item[1], item[0])
    if item[0] <= word_lens[-1][0]:
        print "Shortest word is \"%s\" with lenght of (%d) characters." % (
            item[1], item[0])
