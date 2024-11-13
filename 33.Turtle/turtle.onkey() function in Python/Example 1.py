# import package
import turtle

# method for key call
def fxn():
	turtle.forward(40)

# set turtle screen size
sc=turtle.Screen()
sc.setup(600,300)

# motion
turtle.forward(40)

# call method on Right key
turtle.onkey(fxn,'Right')

# to listen by the turtle
turtle.listen()
