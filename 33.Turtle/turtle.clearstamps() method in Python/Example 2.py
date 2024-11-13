# import package
import turtle

# loop to create motion
# with stamps
for i in range(12):
    # motion
    turtle.forward(50)

    # stamp
    turtle.stamp()
    turtle.right(30)

# hide the turtle for
# better understandings
turtle.ht()

# clear the first 8 stamps
turtle.clearstamps(8)
