def position(userStr, userChar):
    found_at = []
    for i in range(len(userStr)):
        if userStr[i] == userChar:
            found_at.append(i)


    return found_at        
