# import tkinter
from tkinter import *

# make an object of Tk interface
window = Tk()

# Give the title to out window
window.title('GFG')

# creating canvas
canvas = Canvas(window, width=300, height=200)
canvas.pack()

# draw line to out canvas
canvas.create_line(0, 0, 300, 200)
canvas.create_line(0, 200, 300, 0)

# draw oval to out canvas
canvas.create_oval(50, 25, 250, 175, fill="yellow")

window.mainloop()
