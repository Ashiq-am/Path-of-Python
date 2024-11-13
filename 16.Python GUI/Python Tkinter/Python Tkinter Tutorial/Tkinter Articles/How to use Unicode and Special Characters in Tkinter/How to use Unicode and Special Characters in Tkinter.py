# Import Tkinter
from tkinter import *

# Create Object
root = Tk()

# Set geometry
root.geometry("100x200")

# Unicodes values
unicodes_values = [
'\u00A1',
'\u00A2',
'\u00A3',
'\u00A4',
'\u00A5',
'\u00A6',
'\u00A7'
]

# Iterate through all unicode values
for unicodes_value in unicodes_values:
	Label(root, text = u'{unicodes_value}'.format(
	unicodes_value = unicodes_value)).pack()

# Execute Tkinter
root.mainloop()
