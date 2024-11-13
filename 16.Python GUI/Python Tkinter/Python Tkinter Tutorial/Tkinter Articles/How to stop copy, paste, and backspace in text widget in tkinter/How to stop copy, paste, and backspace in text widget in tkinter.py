# Python program to stop, copy, and backspace
# in a text widget in Tkinter

# Import the library tkinter
from tkinter import *

# Create a GUI widget
app=Tk()

# Set the geometry of the app
app.geometry("700x350")

# Create and display text field widget
text=Text(app, font="Calibri, 14")
text.pack(fill= BOTH, expand= True)

# Bind the paste key with the event handler
text.bind('<Control-v>', lambda _:'break')

# Bind the copy key with the event handler
text.bind('<Control-c>', lambda _:'break')

# Bind the backspace key with the event handler
text.bind('<BackSpace>', lambda _:'break')

# Make infinite loop for displaying app
# on the screen
app.mainloop()
