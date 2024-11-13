# Python program to obtain value after button click

# Import the libraries BeautifulSoup, tkinter and os
from bs4 import BeautifulSoup as bs
import os
from tkinter import *

# Remove the last segment of the path
base = os.path.dirname(os.path.abspath('gfg3.py'))

# Open the HTML in which you want to make changes
html = open(os.path.join(base, 'gfg.html'))

# Parse HTML file in Beautiful Soup
soup = bs(html, 'html.parser')

# Find the value which you want to obtain after button click
value = soup.find("li", {"id": "here"}).text

# Construct the app for clicking of button
app = Tk()

# Give title to your GUI app
app.title("Vinayak App")

# Set dimensions for the app
app.geometry('600x400')


def apple():

	# Open the file in which you want to obtain the value
	with open('text_file.txt', "w", encoding='utf-8') as f_output:

		# Writing the value in the file
		f_output.write(value)


# Construct the button in your app
b1 = Button(app, text='Click Here!', command=apple)

# Display the button created in previous step
b1.grid(padx=250, pady=150)

# Make the loop for displaying app
app.mainloop()
