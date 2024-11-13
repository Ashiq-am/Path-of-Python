# Python program to create a
# LabelFrame inside a Tkinter canvas

# Import the library tkinter
from tkinter import *

# Create and resizing a GUI app
app = Tk()
app.geometry("500x500")

# Creating and displaying a canvas
canvas = Canvas(app, bg="yellow", height=200, width=300)
canvas.pack()

# Creating and displaying a LabelFrame
label_frame = LabelFrame(canvas, text="Geeks For Geeks")
label = Label(label_frame, text="Data Structures")
label.pack()

# Displaying and resizing of LabelFrame inside Canvas
canvas.create_window(100, 100, window=label_frame, anchor='w')

# Make the infinite loop for displaying the app
app.mainloop()
