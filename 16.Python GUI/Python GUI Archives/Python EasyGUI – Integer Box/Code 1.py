# importing easygui module
from easygui import *

# message to be displayed
text = "Enter Something (integer)"

# window title
title = "Window Title GfG"

# default integer
d_int = 10

# lower bound
lower = 0

# upper bound
upper = 99999

# creating a integer box
output = integerbox(text, title, d_int, lower, upper)

# title for the message box
title = "Message Box"

# creating a message
message = "Enterted Number : " + str(output)

# creating a message box
msg = msgbox(message, title)
