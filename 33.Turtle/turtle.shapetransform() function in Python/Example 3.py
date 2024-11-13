# import package
import turtle

# loop for pattern
for i in range(5):
    for j in range(10):
        # motion
        turtle.forward(5 + 5 * (i + j))
        turtle.left(45)

    # transform the shape
    turtle.shapetransform(i + 1, 0, 0, i + 1)
