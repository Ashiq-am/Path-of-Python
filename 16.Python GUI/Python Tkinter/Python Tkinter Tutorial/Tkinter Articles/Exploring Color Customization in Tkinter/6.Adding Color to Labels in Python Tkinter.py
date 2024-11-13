from tkinter import *

root = Tk()
root.title("Tkinter Color Label Example")

# Create a label with background and foreground colors
label = Label(root, text="Hello, Tkinter!", bg="lightgray", fg="black")
label.pack()

root.mainloop()
