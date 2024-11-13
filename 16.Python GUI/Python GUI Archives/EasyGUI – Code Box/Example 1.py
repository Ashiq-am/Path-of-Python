# importing easygui module
from easygui import *

# message to be displayed
message = "Below is the text to edit"

# window title
title = "Window Title GfG"

# long code text
text = """<gfg>

EasyGUI
is a module for very simple,
very easy GUI programming in Python.
EasyGUI
is different from otherGUI generators
in that EasyGUI is NOT event-driven.

</gfg>"""

# creating a code box
output = codebox(message, title, text)

# showing the output
print("Alterted Text ")
print("================")
print(output)
