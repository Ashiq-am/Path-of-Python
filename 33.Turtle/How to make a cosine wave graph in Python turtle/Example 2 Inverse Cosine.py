import math
import turtle
win = turtle.Screen()
win.bgcolor("white")

# coordinate setting
win.setworldcoordinates(-1, -180, 1, 180)
t = turtle.Turtle()

# Draw a Horizantal line
t.goto(1, 0)
t.goto(-1, 0)
t.penup()
t.goto(0, 0)
t.pendown()

# Draw a vertical line
t.goto(0, 180)
t.goto(0, -180)
t.penup()
t.goto(1, 0)
t.pendown()
t.pencolor("blue")
t.pensize(4)

# Generate wave form
for y in range(0, 180):
	x = math.cos(math.radians(y))
	t.goto(x, y)
