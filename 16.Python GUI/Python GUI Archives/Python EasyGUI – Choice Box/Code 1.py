# importing easygui module
from easygui import *

# message to be displayed
text = "Selected any one item"

# window title
title = "Window Title GfG"

# item choices
choices = ["Geek", "Super Geeek", "Super Geek 2", "Super Geek God"]

# creating a button box
output = choicebox(text, title, choices)

# title for the message box
title = "Message Box"

# message
message = "You selected : " + str(output)

# creating a message box
msg = msgbox(message, title)
