def fav_rec(userStr, size = 10):
    str_lenght = len(userStr)
    big = size * (userStr + " ")
    small = userStr + " " + ( (" " * str_lenght) * (size - 2))+ \
            ((size - 3) * " ") + " " + userStr

    print big
    print small
    print small
    print big
    
