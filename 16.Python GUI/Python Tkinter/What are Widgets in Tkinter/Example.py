from tkinter import *


# create root window
root = Tk()

# frame inside root window
frame = Frame(root)

# geometry method
frame.pack()

# button inside frame which is
# inside root
button = Button(frame, text ='Welcome')
button.pack()

# Tkinter event loop
root.mainloop()
