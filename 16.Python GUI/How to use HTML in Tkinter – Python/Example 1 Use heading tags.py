# Import Module
from tkinter import *
from tkhtmlview import HTMLLabel

# Create Object
root = Tk()

# Set Geomerty
root.geometry("400x400")

# Add label
my_label = HTMLLabel(root, html=""" 
		<h1>GEEKSFORGEEKS</h1> 
		<h2>GEEKSFORGEEKS</h2> 
		<h3>GEEKSFORGEEKS</h3> 
		<h4>GEEKSFORGEEKS</h4> 
		<h5>GEEKSFORGEEKS</h5> 
		<h6>GEEKSFORGEEKS</h6> 
	""")

# Adjust label
my_label.pack(pady=20, padx=20)

# Execute Tkinter
root.mainloop()
