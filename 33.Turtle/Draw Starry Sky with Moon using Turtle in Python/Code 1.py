# importing turtle library
import turtle


# creating turtle object
t = turtle.Turtle()

# to activate turtle graphics screen
w = turtle.Screen()

# speed of turtle's pen
t.speed(0)

# creating star
for i in range(0, 5):
	t.fd(200)
	t.right(144)

# after clicking turtle graphics screen
# will be terminated
w.exitonclick()
