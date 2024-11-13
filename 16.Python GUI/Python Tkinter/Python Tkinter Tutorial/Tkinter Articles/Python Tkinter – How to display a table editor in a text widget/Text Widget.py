# Import tkinter
from tkinter import *

# Create an instance of tkinter window
window = Tk()

# Size of the tkinter window
window.geometry("200x200")

# Create text widget
text = Text(window, width=15, height=2)

# insert text into the text field
text.insert(INSERT, "Hello world!")

# Set the position of the widget
text.grid(row = 0,column = 0)

window.mainloop()
