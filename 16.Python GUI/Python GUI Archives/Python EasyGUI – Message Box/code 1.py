# importing easygui module
from easygui import *

# message / information to be displayed on the screen
message = "This is a Mesage Box in EasyGUI"

# title of the window
title = "GfG - EasyGUI"

# text of the Ok button
ok_btn_txt = "Continue"

# creating a message box
output = msgbox(message, title, ok_btn_txt)

# printing the output
print("User pressed : " + output)
