# importing easygui module
from easygui import *

# message to be displayed
text = "Message to be displayed on the window GfG"

# window title
title = "Window Title GfG"

# button list
button_list = []

# button 1
button1 = "First"

# second button
button2 = "Second"

# third button
button3 = "Third"

# appending button to the button list
button_list.append(button1)
button_list.append(button2)
button_list.append(button3)


# creating a button box
output = buttonbox(text, title, button_list)

# printing the button pressed by the user
print("User selected option : ", end = " ")
print(output)
