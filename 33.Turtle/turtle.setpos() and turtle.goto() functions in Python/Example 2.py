# import package
import turtle


# method to raw pattern
# of circle with rad radius
def draw(rad):
    # draw circle
    turtle.circle(rad)

    # set the position by using setpos()
    turtle.up()
    turtle.setpos(0, -rad)
    turtle.down()


# loop for pattern
for i in range(5):
    draw(20 + 20 * i)
