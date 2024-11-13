# importing turtle module
import turtle

# size
n = 10

# creating instance of turtle
pen = turtle.Turtle()

# loop to draw a side
for i in range(n * 3):
    # drawing side of
    # length i*10
    pen.forward(i * 10)

    # changing direction of pen
    # by 120 degree in clockwise
    pen.right(120)

# closing the instance
turtle.done()
