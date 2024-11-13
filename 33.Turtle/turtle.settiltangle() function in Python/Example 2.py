# import package
import turtle

# set turtle
turtle.speed(1)
turtle.up()
turtle.setpos(-50, 100)
turtle.down()
turtle.shape("turtle")
turtle.width(2)

# loop for pattern
for i in range(6):
    # motion
    turtle.forward(100)

    # set tilt angle by 180
    turtle.settiltangle(180)

    # print turtleshape
    turtle.stamp()

    # move to right by 60
    turtle.right(60)

# hide the turtle
turtle.ht()
