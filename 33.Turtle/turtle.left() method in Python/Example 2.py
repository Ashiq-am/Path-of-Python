# importing package
import turtle

# Loop for pattern
for i in range(10):
    # move the turtle forward by
    # 100+variable unit distance
    # in the direction of head of
    # turtle
    turtle.forward(100 + 10 * i)

    # change the direction of turtle
    # by 90 degrees to the left.
    turtle.left(90)
