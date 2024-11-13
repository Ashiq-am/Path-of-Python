# importing easygui module
from easygui import *

# message to be displayed
text = "Enter the following details"

# window title
title = "Window Title GfG"

# list of multiple inputs
input_list = ["Geek Name", "Geek ID", "Experiance"]


# creating a integer box
output = multenterbox(text, title, input_list)

# title for the message box
title = "Message Box"

# creating a message
message = "Enterted details are in form of list : " + str(output)

# creating a message box
msg = msgbox(message, title)
