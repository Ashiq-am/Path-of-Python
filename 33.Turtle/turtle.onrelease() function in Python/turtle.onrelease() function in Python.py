# import package
import turtle


# methods to action
def fxn1(x, y):
    turtle.fillcolor("blue")


def fxn2(x, y):
    turtle.fillcolor("white")


# set screen and turtle
sc = turtle.Screen()
sc.setup(400, 300)

turtle.shape("turtle")
turtle.turtlesize(2)
turtle.speed(1)

# allow user to click for some action
turtle.onclick(fxn1)

# allow user to release for some action
turtle.onrelease(fxn2)
