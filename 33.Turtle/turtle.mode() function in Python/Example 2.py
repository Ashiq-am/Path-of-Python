# importing package
import turtle

# motion with default mode (standard)
# default direction of turtle head
# is north in standard mode
turtle.forward(180)

# set mode to 'logo' mode
turtle.mode(mode='logo')

# do some motion
# default direction of turtle head
# is east in logo mode
turtle.forward(120)

# set mode to 'world' mode
turtle.mode(mode='world')

# do some motion
turtle.forward(100)

# set coordinates of the turtle
# mode (world) by choice of user
turtle.setworldcoordinates(-500,-500,500,500)
