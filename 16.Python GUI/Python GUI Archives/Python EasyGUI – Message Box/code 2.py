# importing easygui module
from easygui import *

# message / information to be displayed on the screen
message = "This is a Mesage Box in EasyGUI (GeeksforGeeks)"

# title of the window
title = "GfG - EasyGUI"

# creating a message box
output = msgbox(message, title)

# printing the output
print("User pressed : " + output)
