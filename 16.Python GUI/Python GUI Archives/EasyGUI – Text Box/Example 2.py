# importing easygui module
from easygui import *

# message to be displayed
message = "Below is the text to edit"

# window title
title = "Window Title GfG"

# creating a multi password box
output = textbox(message, title)

# showing the output
print("Alterted Text ")
print("================")
print(output)
