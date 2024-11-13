# import package
import turtle

# set turtle
turtle.speed(1)
turtle.shape("turtle")
turtle.fillcolor("blue")

# loop for motion
for i in range(4):

	# set turtle length
	turtle.turtlesize(stretch_len=(i+1)*0.5)
	turtle.forward(100)
	turtle.right(90)
