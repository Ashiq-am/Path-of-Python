# importing package
import turtle

# set turtle
turtle.speed(1)
turtle.up()
turtle.goto(-40,40)
turtle.down()

# set shear and apply to
# all shapes
turtle.shearfactor(0.5)

# get shape
sh=turtle.getshapes()

# loop for pattern
for i in range(len(sh)):
	turtle.shape(sh[i])
	turtle.forward(100+10*i)
	turtle.right(90)
	turtle.forward(100+10*i)
	turtle.right(90)
