# importing easygui module
from easygui import *

# message to be displayed
text = "Enter your Geek name !!"

# window title
title = "Window Title GfG"

# default text
d_text = "Enter here.."

# creating a enter box
output = enterbox(text, title, d_text)

# title for the message box
title = "Message Box"

# creating a message
message = "Enterted Name : " + str(output)

# creating a message box
msg = msgbox(message, title)
