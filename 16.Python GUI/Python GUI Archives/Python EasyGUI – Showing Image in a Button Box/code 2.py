# importing easygui module
from easygui import *

# message to be displayed
text = "How much do you like the image given below"

# window title
title = "Window Title GfG"

# button list
button_list = []

# button 1
button1 = "Average"

# second button
button2 = "Good"

# third button
button3 = "Very Good"

# appending button to the button list
button_list.append(button1)
button_list.append(button2)
button_list.append(button3)

# a image of a dog
img = "dog_image.png"

# creating a button box
output = buttonbox(text, title, image = img, choices = button_list)

# title for the message box
title = "Message Box"

# message
message = "You selected : " + output

# creating a message box
msg = msgbox(message, title)
