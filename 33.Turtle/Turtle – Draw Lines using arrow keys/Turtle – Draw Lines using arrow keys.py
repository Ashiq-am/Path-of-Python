# import for turtle module
import turtle

# making a workScreen
wn = turtle.Screen()

# defining 2 turtle instance
head = turtle.Turtle()
pen = turtle.Turtle()

# head is for telling which key is pressed
head.penup()
head.hideturtle()

# head is at 0,260 coordinate
head.goto(0, 260)
head.write("This is to tell which key is currently pressed",
		align="center", font=("courier", 14, "normal"))


def f():
	y = pen.ycor()
	pen.sety(y+100)
	head.clear()
	head.write("UP", align="center", font=("courier", 24, "normal"))


def b():
	y = pen.ycor()
	pen.sety(y-100)
	head.clear()
	head.write("Down", align="center", font=("courier", 24, "normal"))


def l():
	x = pen.xcor()
	pen.setx(x-100)
	head.clear()
	head.write("left", align="center", font=("courier", 24, "normal"))


def r():
	x = pen.xcor()
	pen.setx(x+100)
	head.clear()
	head.write("Right", align="center", font=("courier", 24, "normal"))


wn.listen()
wn.onkeypress(f, "Up") # when up is pressed pen will go up
wn.onkeypress(b, "Down") # when down is pressed pen will go down
wn.onkeypress(l, "Left") # when left is pressed pen will go left
wn.onkeypress(r, "Right") # when right is pressed pen will go right
