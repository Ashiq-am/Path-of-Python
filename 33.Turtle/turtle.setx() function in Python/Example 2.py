# import package
import turtle

# set turtle direction
turtle.left(90)

# loop for pattern
for i in range(4):
    # motion
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(100)

    # set the x cordinate
    turtle.up()
    turtle.setx(40 * (i + 1))
    turtle.down()

    # change the direction
    turtle.left(180)
