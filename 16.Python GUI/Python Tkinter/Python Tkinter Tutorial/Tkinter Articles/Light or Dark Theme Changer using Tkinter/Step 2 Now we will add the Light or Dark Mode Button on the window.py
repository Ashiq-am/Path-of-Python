# Importing Tkinter library
# in the environment
from tkinter import *

# Creating a window
window = Tk()
window.title("Theme Changer")
window.geometry("600x800")
window.config(bg="white")

# Adding light and dark mode images
light = PhotoImage(file="light.png")
dark = PhotoImage(file="dark.png")

# Creating a button to toggle
# between light and dark themes
switch = Button(window, image=light,
				bd=0, bg="white")

# setting the position of the button
switch.pack(padx=50, pady=150)

window.mainloop()
