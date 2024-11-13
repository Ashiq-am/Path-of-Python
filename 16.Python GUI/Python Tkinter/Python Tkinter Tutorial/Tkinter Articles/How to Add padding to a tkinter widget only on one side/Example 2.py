# Python program to add padding
# to a widget only from top

# Import the library tkinter
from tkinter import *

# Create a GUI app
app = Tk()

# Give title to your GUI app
app.title("Vinayak App")

# Maximize the window screen
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.geometry("%dx%d" % (width, height))

# Construct the button in your app
b1 = Button(app, text='Click Here!')

# Give the topmost padding
b1.grid(padx=(0, 0), pady=(200, 0))

# Make the loop for displaying app
app.mainloop()
