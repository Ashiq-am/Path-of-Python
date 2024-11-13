# import package
import turtle

# set turtle
turtle.speed(1)
turtle.shape("turtle")
turtle.fillcolor("blue")

# loop for motion
for i in range(4):
    # set turtle outline
    turtle.turtlesize(outline=i + 1)
    turtle.forward(100)
    turtle.right(90)
