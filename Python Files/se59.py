languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python" , languages)

def filter(x):
    box = []
    for i in x:
        if i == "Python":
            box.append(i)
    return box

print filter(languages)


threes_and_fives = [x for x in range(1, 16)\
                    if x % 3 == 0 or x % 5 == 0 ]
print threes_and_fives



        
    
