# import package
import turtle

# add shape to the shape list as above
turtle.addshape(name="gfg.gif",shape=None)

# set turtle with new shape
# and new position
turtle.shape("gfg.gif")
turtle.up()
turtle.setpos(-10,10)
turtle.down()

# loop for motion
for i in range(22):
	turtle.fd(40+5*i)
	turtle.right(90)
