garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message

# Tova shifrova suobshtenieto.
message2 = message
garbled2_ip = message2[::-1]
box = []
for i in garbled2_ip:
    box.append((i + 'X'))

gg = "".join(box)
print gg


# Tova razshifrova suobshtenieto.
msg = filter(lambda x: x != "X",gg)
print msg[::-1]
