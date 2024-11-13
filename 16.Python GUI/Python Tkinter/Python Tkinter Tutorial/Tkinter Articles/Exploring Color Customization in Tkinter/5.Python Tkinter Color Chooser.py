from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Tkinter Color Chooser Example")

def choose_color():
    color = colorchooser.askcolor(title="Choose color")
    print("Selected color:", color[1])  # Print the hexadecimal color value

button = Button(root, text="Choose Color", command=choose_color)
button.pack()

root.mainloop()
