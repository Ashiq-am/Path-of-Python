# import package
import turtle

# set screen
sc = turtle.Screen()
sc.setup(500, 350)

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

    # tilt turtleshpae by 180
    turtle.tilt(180)

    # print turtleshape
    turtle.stamp()

    # move to right by 60
    turtle.right(60)

# hide the turtle
turtle.ht()
