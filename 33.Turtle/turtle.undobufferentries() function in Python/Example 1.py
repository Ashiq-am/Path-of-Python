# import package
import turtle

# loop for motion
for i in range(50):
	turtle.forward(20+2*i)
	turtle.right(90)

# check the undo buffer size
# it is loop iteration*turtle's statement
# i.e; 50*2 = 100
print(turtle.undobufferentries())
