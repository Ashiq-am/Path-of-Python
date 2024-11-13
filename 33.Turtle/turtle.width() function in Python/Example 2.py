# import package
import turtle

# loop for pattern
for i in range(15):
    # set turtle width
    turtle.width(15 - i)

    # motion for pattern
    turtle.forward(50 + 15 * i)
    turtle.right(90)
