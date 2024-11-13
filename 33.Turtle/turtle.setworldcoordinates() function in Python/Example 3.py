# importing package
import turtle

# make screen object and
# set mode to world
sc = turtle.Screen()
sc.mode('world')

# set world coordinates
turtle.setworldcoordinates(-50, -50, 50, 50)

# do some motion
for i in range(16):
	turtle.forward(1+1*i)
	turtle.right(90)

# set world coordinates
turtle.setworldcoordinates(-40, -40, 40, 40)

# do some motion
for i in range(16):
	turtle.forward(1+1*(i+16))
	turtle.right(90)

# set world coordinates
turtle.setworldcoordinates(-30, -30, 30, 30)

# do some motion
for i in range(16):
	turtle.forward(1+1*(i+32))
	turtle.right(90)
