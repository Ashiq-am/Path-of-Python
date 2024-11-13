# import package
import turtle

# set background image
turtle.bgpic("gfg.png")

# loop for motion
for i in range(20):
	turtle.forward(5+5*i)
	turtle.right(90)

# delete background image
turtle.bgpic("nopic")
