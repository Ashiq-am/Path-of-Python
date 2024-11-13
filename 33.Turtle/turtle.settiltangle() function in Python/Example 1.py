# import package
import turtle

# set turtle position
turtle.up()
turtle.setpos(-100,0)
turtle.down()

# set turtle speed
turtle.speed(1)

# set tilt angle to 90
turtle.settiltangle(90)

# motion
turtle.forward(100)

# set tilt angle to 270 (not 90+270=360)
turtle.settiltangle(270)

# motion
turtle.forward(100)
