# importing package
import turtle

# make screen objcet and
# set screen mode to world
sc = turtle.Screen()
sc.mode('world')

# set world coordinates
turtle.setworldcoordinates(-20, -20, 20, 20)

# loop for some motion
for i in range(20):
	turtle.forward(1+1*i)
	turtle.right(90)
