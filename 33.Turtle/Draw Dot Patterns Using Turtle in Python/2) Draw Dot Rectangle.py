# import package and making object
import turtle

pen = turtle.Turtle()


# method to draw rectangle with dots
# space --> distance between dots
# x	 --> height of rectangle
# y	 --> width of rectangle
def draw(space, x, y):
    for i in range(x):
        for j in range(y):
            # dot
            pen.dot()

            # distance for another dot
            pen.forward(space)
        pen.backward(space * y)

        # direction
        pen.right(90)
        pen.forward(space)
        pen.left(90)

    # Main Section


pen.penup()
draw(10, 5, 12)

# hide the turtle
pen.hideturtle()
