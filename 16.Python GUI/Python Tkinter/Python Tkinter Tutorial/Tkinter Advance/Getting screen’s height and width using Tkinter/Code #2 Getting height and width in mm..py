# importing tkinter module
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# getting screen's height in mm
height = root.winfo_screenmmheight()

# getting screen's width in mm
width = root.winfo_screenmmwidth()

print("\n width x height = %d x %d (in mm)\n" %(width, height))
# infinite loop
mainloop()
