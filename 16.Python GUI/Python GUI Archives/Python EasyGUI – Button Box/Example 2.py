# importing easygui module
from easygui import *

# message to be displayed
text = "Message to be displayed on the window GfG"

# window title
title = "Window Title GfG"

# creating a button box
output = buttonbox(text, title)

# printing the button pressed by the user
print("User selected option : ", end = " ")
print(output)
