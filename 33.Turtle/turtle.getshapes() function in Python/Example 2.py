# import package
import turtle

shapes = turtle.getshapes()

# set speed to slowest
turtle.speed(1)

# draw all shapes
for i in range(len(shapes)):
    # shape
    turtle.shape(shapes[i])

    # motion

    turtle.forward(100)
    turtle.right(51.42)
    turtle.stamp()
