# import package
import turtle

# set turtle
turtle.speed(1)
turtle.shape("turtle")
turtle.fillcolor("blue")

# loop for motion
for i in range(4):
    # set turtlesize properties all together
    turtle.turtlesize(stretch_wid=(i + 1) * 0.5,
                      stretch_len=(i + 1) * 0.5,
                      outline=(i + 1)
                      )
    turtle.forward(100)
    turtle.right(90)
