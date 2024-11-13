# importing easygui module
from easygui import *

# message to be displayed
text = "Enter a number !!"

# window title
title = "Window Title GfG"

# creating a integer box
output = integerbox(text, title)

# title for the message box
title = "Message Box"

# creating a message
message = "Enterted Number : " + str(output)

# creating a message box
msg = msgbox(message, title)
