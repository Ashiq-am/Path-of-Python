# Importing the tkinter module using import keyword
from tkinter import *

# Initialize parent object or master object as "parent"
parent = Tk()

# passing master object as parameter and set "COLOURS" as
# the name of the OptionMenu using set() method.
variable = StringVar(parent)
variable.set("COLOURS")

# Constructor of OptionMenu class intialized by giving
# the parametrs as master object, variable name and the
# list of options in the menu.
option_menu = OptionMenu(parent, variable, "Yellow",
						"Blue", "Green", "Purple",
						"Black", "White")

# Using pack() method in OptionMenu class to arrange the
# option menu.
option_menu.pack()

# Using mainloop() method from OptionMenu class before we
# run the code.
parent.mainloop()
