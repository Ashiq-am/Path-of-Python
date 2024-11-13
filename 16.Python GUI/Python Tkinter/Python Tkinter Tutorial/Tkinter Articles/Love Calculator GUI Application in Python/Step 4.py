# import tkinter
from tkinter import *
# import random module
import random
# Creating GUI window
root = Tk()
# Defining the container size, width=400, height=240
root.geometry('400x240')
root.title('Love Calculator????') # Title of the container

# Function to calculate love percentage between the user and partner
def calculate_love():
	# value will contain digits between 0-9
	st = '0123456789'
	result=0
	# result will be in double digits
	digit = 2
	temp = "".join(random.sample(st, digit))
	result.config(text=temp)


# Starting the GUI
root.mainloop()
