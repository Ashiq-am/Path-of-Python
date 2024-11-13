# IMPORTING THE REQUIRED LIBRARIES
import turtle
import pandas

# SETTING UP THE WINDOW THAT OPENS
# IN WHICH WE PLAY OUR GAME

# creating a blank window from Screen()
# class of turtle library
screen = turtle.Screen()

# give a title to our window using
# title method of screen object
screen.title("Guess the Names of Indian States")

# give the window height and width
# in which our map fits perfectly
screen.setup(width=500, height=500)

# use addshape method of screen object
# to add an image to our program
image = 'blank_map.gif'
screen.addshape(image)

# give the turtle the shape of our image
turtle.shape(image)

# SETTING UP THE TURTLE

# create a turtle from Turtle class
pen = turtle.Turtle()

# we don't want to see it hovering
# over our map, so we hide it
pen.hideturtle()

# we don't want to draw anything,
# so we lift it up from screen.
# like lifting the pen from paper
# to leave a blank space while writing
pen.penup()

# this method keep the window on for
# diplay until the user himself closes it.
# this method should always be the last
# line fo our code whenever using turtle.
turtle.mainloop()
