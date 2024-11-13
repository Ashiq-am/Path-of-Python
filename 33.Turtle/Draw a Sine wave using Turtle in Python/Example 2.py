import math
import turtle

win = turtle.Screen()
win.bgcolor("white")

# coordinate setting
win.setworldcoordinates(-90, -1, 90, 1)
t = turtle.Turtle()

# Draw a Horizantal line
t.goto(-90, 0)
t.goto(90, 0)
t.penup()
t.goto(0, 0)
t.pendown()

# Draw a vertical line
t.goto(0, 1)
t.goto(0, -1)
t.penup()
t.goto(-90, -1)
t.pendown()
t.pencolor("blue")
t.pensize(4)

# Generate wave form
for x in range(-90, 90):
	y = math.sin(math.radians(x))
	t.goto(x, y)
