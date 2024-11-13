# import package
import turtle

# set turtle speed to fastest
# for bettrt understandings
turtle.speed(10)


# method to draw a part
def fxn():
    # motion
    turtle.circle(50, 180)
    turtle.right(90)
    turtle.circle(50, 180)

# loop to draw pattern
for i in range(12):
    fxn()

# set turtle at home
turtle.up()
turtle.home()
turtle.down()

# set position
turtle.left(30 * (i + 1))
