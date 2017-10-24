# Second GUI script (as my second ever).
from Tkinter import *

# create the window
master = Tk()

#modify main window
master.title("D.D.")
master.geometry("300x150")

app = Frame(master)
app.grid()
frame1 = Frame(app, relief = GROOVE, borderwidth = 2)
frame1.grid()


label = Label(frame1, text = "Whoa, what does this button do?!", relief = GROOVE, borderwidth = 2)
label.grid(row = 0, column = 1)

button1 = Button(frame1, text = "BIG RED BUTTON", bg = "red", relief = FLAT)
button1.grid(row = 5, column = 1)


#starts the event loop
master.mainloop()
