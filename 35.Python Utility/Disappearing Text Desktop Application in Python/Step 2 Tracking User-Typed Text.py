from tkinter import *

# LOGIC

user_text = ""
timer = None


# method to do the main calculations
def start_calculating(event):
    # global keyword tells the function to use the following identifiers
    # are variables outside this function.
    global timer, user_text

    if timer is not None:
        window.after_cancel(timer)

    # keysym property of event simply tell us which key was pressed
    if event.keysym == "BackSpace":
        user_text = user_text[0: len(user_text) - 1]

    # we access the character of the key using char property.
    elif event.char:
        user_text += event.char
        timer = window.after(5000, reset_app)

    return
