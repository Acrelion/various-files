# Codes and decodes a message.

from sys import exit

def kodirai(x):
    x = str(x)
    djur_ip = x[::-1]
    guz = []
    for i in djur_ip:
        guz.append((i + "X"))
    gg = "".join(guz)
    print gg
    nachalo()


def razkodirai(y):
    msg = filter(lambda x: x != "X",y)
    print msg[::-1]
    nachalo()


def nachalo():
    inp0 = int(raw_input("\n1. Kodirane, 2. Razkodirane, 3. Stop: "))
    if inp0 == 1:
        inp1 = str(raw_input("Message: "))
        kodirai(inp1)
    elif inp0 == 2:
        inp2 = str(raw_input("The Incripted message: "))
        razkodirai(inp2)
    elif inp0 == 3:
        exit(0)
    else:
        print "Enter 1, 2 or 3 only."

nachalo()
