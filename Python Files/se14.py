def rooms():
    choise = raw_input("r or l? ").lower()
    if choise == "r":
        print "You turn right."
    elif choise == "l":
        print "You turn left."
    else:
        print "You continue forward."
    rooms()

rooms()
