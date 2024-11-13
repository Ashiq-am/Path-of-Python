# import package
import turtle

# set speed
turtle.speed(1)

# loop for motion
for i in range(4):
    # motion
    turtle.forward(100)

    # undo previous work
    turtle.undo()

    # turn
    turtle.left(90)
