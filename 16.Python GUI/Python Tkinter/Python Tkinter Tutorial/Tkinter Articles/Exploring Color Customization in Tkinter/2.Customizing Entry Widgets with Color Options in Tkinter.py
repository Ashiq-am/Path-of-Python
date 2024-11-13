from tkinter import *

root = Tk()
root.title("Tkinter Color Text Example")

# Create an Entry widget with selection colors
entry = Entry(root, selectbackground="lightblue", selectforeground="black")
entry.pack()

root.mainloop()
