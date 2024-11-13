# importing easygui module
from easygui import *

# message to be displayed
text = "Enter the details to go further"

# window title
title = "Window Title GfG"

# list of entry fields
fields = ["Email ID", "Geek ID", "Password"]

# default text
default_values = ["email@abc.com", "G-111", "password"]

# creating a multi password box
output = multpasswordbox(text, title, fields, default_values)

# showing details entered by the user
print("Details entered by user")
print("==================================")

# traversing the output
for i in range(len(fields)):
    # showing field and entered value
    print(fields[i] + " : " + str(output[i]))
