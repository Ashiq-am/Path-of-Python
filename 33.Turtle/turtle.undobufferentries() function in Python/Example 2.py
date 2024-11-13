# import package
import turtle

# loop for motion
for i in range(50):
	turtle.forward(20+2*i)
	turtle.right(90)

# call undo() method till the
# undobuffer length
while turtle.undobufferentries():
	turtle.undo()
