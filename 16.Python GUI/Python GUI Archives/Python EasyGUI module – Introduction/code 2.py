# importing easygui module
from easygui import *

# choices which user can select
choices = ["Geek", "Super Geek", "Super Geek 2", "Super Geek God"]

# mesaage / question to be asked
msg = "Select any one option"

# opening a choice box using our msg and choices
reply = choicebox(msg, choices = choices)

# printing the selected option
print("You selected : ", end = "")
print(reply)
