# importing easygui module
from easygui import *

# message / information to be displayed on the screen
message = "Select any one button"

# title of the window
title = "GfG - EasyGUI"

# creating a index box
output = indexbox(message, title)

# showing new message according to the buttons pressed
# if index is 0
if output == 0:

    # message / information
    message = "First"
# if index is 1
elif output == 1:

    # message / information
    message = "Second"

# message
message = message + " Button Pressed"

# title of the window
title = "GfG - EasyGUI"

# creating a message box
msg = msgbox(message, title)

