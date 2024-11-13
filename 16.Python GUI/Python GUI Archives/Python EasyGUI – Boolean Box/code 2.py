# importing easygui module
from easygui import *

# message / information to be displayed on the screen
message = "Select any one button"

# title of the window
title = "GfG - EasyGUI"

# buttons
buttons = ["First", "Second"]

# creating a boolean box
output = boolbox(message, title, buttons)

# showing new message according to the buttons pressed
# if output is 1
if output == 1:

    # message / information
    message = "First Button is pressed"


# if output is 0
elif output == 0:

    # message / information
    message = "Button rather than first button is pressed"

# title of the window
title = "GfG - EasyGUI"

# creating a message box
msg = msgbox(message, title)

