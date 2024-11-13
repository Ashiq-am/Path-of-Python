# importing easygui module
from easygui import *

# message to be displayed
text = "Enter Something"

# window title
title = "Window Title GfG"


# creating a enter box
output = enterbox(text, title)

# title for the message box
title = "Message Box"

# creating a message
message = "Enterted string : " + str(output)

# creating a message box
msg = msgbox(message, title)
