# importing easygui module
from easygui import *

# message to be displayed
text = "Enter the new password for GeeksforGeeks"

# window title
title = "Window Title GfG"

# creating a integer box
output = passwordbox(text, title)

# title for the message box
title = "Message Box"

# creating a message
message = "Password entered by user : " + str(output)

# creating a message box
msg = msgbox(message, title)
