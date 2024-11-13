# Importing tkinter module as tk
import tkinter as tk

# Importing all functions/methods
# from math module
from math import *

# Import messagebox class from tkinter
from tkinter import messagebox


# function for evaluating the expression
from unittest import result


def eval_expression(event):
    result.configure(text=" Result: " + str(eval(entry.get())))

    messagebox.showinfo("Evaluate Expression","Successfully evaluated")


# creating Tk window
root = tk.Tk()

# set geometry of root window
root.geometry('300x150+600+200')

# set the title of root window
root.title('Evaluate Expression')

# label and entry field
input_label = tk.Label(root,text=" Enter Your Expression:", ).grid(row=1)
entry = tk.Entry(root)

# bind 'enter' event to the
# eval_expression() through
# entry widget
entry.bind()
