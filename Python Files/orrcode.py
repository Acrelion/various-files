def code(message):

    num_vals = {" ": 100, ",": 101, ".": 102, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
                "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
                "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
                "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

    vocals = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5, "y": 6}
    vocalidxs = {1: 1, 5: 2, 9: 3, 15: 4, 21: 5, 25: 6}
    vindexes = [1,5,9,15,21,25]

    # strip whitespaces, convert to lower, split the message
    message = message.strip()
    message = message.lower()
    splitted = list(message)

    # convert the strings into numbers
    converted = []

    for i in range(len(splitted)):
        converted.append(num_vals[splitted[i]])

    full_coded = [0]

    for i in range(len(converted)):
        if converted[i] in vindexes:
                if i == 0:
                    full_coded.append( "0" + str(converted[i]))
                else:
                    if converted[i - 1] in vindexes:
                        full_coded.append( "0" + str(converted[i]))
                    else:
                        continue
        
        # if it not a vocal letter and it is not the last one
        elif converted[i] not in vindexes and i < (len(converted) - 1):
            if converted[i + 1] in vindexes:              
                added_v = str(vocalidxs[converted[i + 1]]) + str(converted[i] + converted[i + 1])
                full_coded.append(added_v)
            else:
                if converted[i] in [100, 101, 102]:
                    full_coded.append(str(converted[i]))
                else:
                    full_coded.append( "0" + str(converted[i]))
        else:
            full_coded.append( "0" + str(converted[i]))

    print full_coded    
   
            

