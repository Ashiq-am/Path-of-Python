# importing package
import turtle

# method to draw a star
def star():
	for i in range(5):
		turtle.forward(60)
		turtle.right(144)

# method to set position
# and fill color in star
def draw(x,y,col):
	turtle.up()
	turtle.setpos(x,y)
	turtle.down()
	turtle.fillcolor(col)
	turtle.begin_fill()
	star()
	turtle.end_fill()

# Driver Code
draw(-100,0,"red")
draw(-50,0,"yellow")
draw(0,0,"blue")
draw(50,0,"green")

# hide the turtle
turtle.hideturtle()
