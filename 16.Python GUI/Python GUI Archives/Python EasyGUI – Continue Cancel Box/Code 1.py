# importing easygui module
from easygui import *

# message / information to be displayed on the screen
message = "You want to learn more about EasyGUI ?"

# title of the window
title = "GfG - EasyGUI"

# creating a continue cancel box
output = ccbox(message, title)

# if user pressed continue
if output:

    # message / information to be displayed on the screen
    message = "Go to GeeksforGeeks to learn more about EasyGUI"

    # title of the window
    title = "GfG - EasyGUI"

    # creating a message box
    msg = msgbox(message, title)

# if user pressed cancel
else:

    # message / information to be displayed on the screen
    message = "Ok No Problem"

    # title of the window
    title = "GfG - EasyGUI"

    # creating a message box
    msg = msgbox(message, title)
