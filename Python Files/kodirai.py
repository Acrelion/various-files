msg = str(raw_input("Message: "))
djur_ip = msg[::-1]
guz = [] # Malko kvadraten guz. I koi te kara da gleda6 koda?
for i in djur_ip:
    guz.append((i + "X"))

gg = "".join(guz)
print gg
