# importing easygui module
from easygui import *

# message to be displayed
text = "Selected any item from the list gievn below"

# window title
title = "Window Title GfG"


# creating a multi choice box
output = multchoicebox(text, title)

# title for the message box
title = "Message Box"

# message
message = "Selected items : " + str(output)

# creating a message box
msg = msgbox(message, title)
