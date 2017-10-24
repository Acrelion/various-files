# In this script we are trying to check the array for punched brands
# and to repunch them into two respective variables.

qu = [
    [1, 'not0', 0],
    [2, 'selected1', 1],
    [3, 'not2', 0],
    [4, 'not3', 0],
    [5, 'not4', 0],
    [6, 'selected2', 1],
    [7, 'not6', 0],
]


brand1 = ""
brand2 = ""


for i in range(len(qu)):
    if qu[i][2] == 1 and brand1 == "":
        brand1 = qu[i][1]
        
    elif qu[i][2] == 1 and brand2 == "":
        brand2 = qu[i][1]



print brand1
print brand2

        
