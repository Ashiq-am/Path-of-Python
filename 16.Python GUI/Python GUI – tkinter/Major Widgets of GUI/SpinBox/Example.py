from tkinter import *

top = Tk()

top.geometry("200x200")

spin = Spinbox(top, from_=0, to=100)

spin.pack()

top.mainloop()