# import package
import turtle

# make turtle objects
# and set position
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.up()
t1.setpos(-70, 0)
t1.down()
t2.up()
t2.setpos(70, 0)
t2.down()

# loop for pattern
for i in range(20):
	t1.forward(2+2*i)
	t1.left(45)
	t2.forward(2+2*i)
	t2.left(90)

# reset first turtle
# another remain as it is
t1.reset()
