# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

# Create Buttons
button_1 = Button(root , text = "Button 1")

# Set grid
button_1.grid(row = 0,column = 0)

# Execute tkinter
root.mainloop()
