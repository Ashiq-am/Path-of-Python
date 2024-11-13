# import modules
import tkinter as tk

# object of tkinter
# and background set for light grey
master = tk.Tk()
master.configure(bg = 'light grey')

# create label
l = tk.Label(master,
			text = "Welcome to geeksforgeeks",
			bg = "red")

# using dictionary label object
print("Label text: ", l["text"])

l.pack()
tk.mainloop()
