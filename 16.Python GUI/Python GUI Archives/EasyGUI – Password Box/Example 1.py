# importing easygui module
from easygui import *

# message to be displayed
text = "Enter the password to enter GeeksforGeeks"

# window title
title = "Window Title GfG"

# default password
default_password = "geeksforgeeks"

# creating a integer box
output = passwordbox(text, title, default_password)

# title for the message box
title = "Message Box"

# creating a message
message = "Password entered by user : " + str(output)

# creating a message box
msg = msgbox(message, title)
