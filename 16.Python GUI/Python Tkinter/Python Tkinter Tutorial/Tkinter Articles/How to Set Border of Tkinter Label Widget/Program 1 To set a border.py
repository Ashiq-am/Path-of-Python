# import tkinter
from tkinter import *

# Create Tk object
window = Tk()

# Set the window title
window.title('With_Border')

# set the window size
window.geometry('300x100')

# take one Label widget
label = Label(window, text="WELCOME TO GFG", borderwidth=1, relief="solid")

# place that label to window
label.grid(column=0, row=1, padx=100, pady=10)
window.mainloop()
