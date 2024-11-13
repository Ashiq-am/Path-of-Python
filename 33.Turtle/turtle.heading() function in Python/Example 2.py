# import package
import turtle

# set turtle speed
# for better inderstandings
turtle.speed(1)

# loop for pattern
for i in range(4):
    turtle.forward(100)

    # get heading value
    val = turtle.heading()

    # write it
    turtle.write(str(val))
    turtle.backward(100)
    turtle.left(90)
