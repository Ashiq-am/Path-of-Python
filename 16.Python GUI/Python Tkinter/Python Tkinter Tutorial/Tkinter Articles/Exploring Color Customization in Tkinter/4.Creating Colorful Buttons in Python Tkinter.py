from tkinter import *

root = Tk()
root.title("Tkinter Color Button Example")

# Create a button with active background and foreground colors
button = Button(root, text="Click Me", activebackground="blue", activeforeground="white")
button.pack()


root.mainloop()
