# import package
import turtle

# set turtle screen
sc=turtle.Screen()
sc.setup(500,300)

# set turtle
turtle.speed(1)
turtle.up()
turtle.setpos(-200,0)
turtle.down()
turtle.shape("square")
turtle.width(2)

# motion
turtle.forward(200)

# tilt turtleshape by 45
turtle.tilt(45)

# motion
turtle.forward(200)
