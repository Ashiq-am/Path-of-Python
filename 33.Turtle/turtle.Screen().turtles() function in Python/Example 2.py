# import package
import turtle

# make screen object and set size
sc = turtle.Screen()
sc.setup(400, 300)

# make first turtle and do something
t1 = turtle.Turtle(shape='square')
t1.color("red")
t1.circle(50)

# make another turtle and do something
t2 = turtle.Turtle(shape='circle')
t2.color("green")
t2.circle(40)

# get all turtles object
turt = sc.turtles()

# use first turtle object
turt[0].circle(-40)

# use another turtle object
turt[1].circle(-50)
