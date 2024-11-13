# importing easygui module
from easygui import *

# message / information to be displayed on the screen
message = "Select any one button"

# title of the window
title = "GfG - EasyGUI"

# list of buttons
buttons = ["First", "Second", "Third", "Fourth"]

# creating a index box
output = indexbox(message, title, buttons)

# showing new message according to the buttons pressed
# if index is 0
if output == 0:

    # message / information
    message = "First"
# if index is 1
elif output == 1:

    # message / information
    message = "Second"

# if index is 2
elif output == 2:

    # message / information
    message = "Third"

# if index is 3
elif output == 3:

    # message / information
    message = "Fourth"

# message
message = message + " Button Pressed"
# title of the window
title = "GfG - EasyGUI"

# creating a message box
msg = msgbox(message, title)

