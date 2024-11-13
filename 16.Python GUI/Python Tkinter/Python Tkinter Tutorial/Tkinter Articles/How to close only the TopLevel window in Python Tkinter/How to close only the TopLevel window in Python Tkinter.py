# Python program to close only the
# TopLevel window in Python Tkinter

# Import the library tkinter
from tkinter import *

# Create a GUI app
app = Tk()

# Set the title and geometry of app
app.title("Main App")
app.geometry('300x100')

# Make a function to create a Top Level window
def top_level():

	# Create a Top Level Window
	top = Toplevel()

	# Create a title and geometry for Top
	# Level Window
	top.title("TopLevel Window")
	top.geometry('200x200')

	# Display a message on Top Level Window
	msg = Message(top, text="Text on TopLevel window", width=150)
	msg.pack()

	# Make a function for exit button
	def exit_btn():
		top.destroy()
		top.update()

	# Create a button to exit Top Level Window
	btn = Button(top, text='EXIT', command=exit_btn)
	btn.pack()

# Create a button to go to Top Level Window
# in GUI app
Button(app, text="Create a TopLevel window", command=top_level).pack()

# Make infinite loop for displaying app on screen
app.mainloop()
