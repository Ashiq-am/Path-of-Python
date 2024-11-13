# importing easygui module
from easygui import *

# message to be displayed
message = "Below is the text to edit"

# window title
title = "Window Title GfG"

# long text
text = ["EasyGUI is a module for very simple, very easy GUI ",
        "programming in Python. EasyGUI is different from other",
        "GUI generators in that EasyGUI is NOT event-driven."]

# creating a multi password box
output = textbox(message, title, text)

# showing the output
print("Alterted Text ")
print("================")
print(output)
