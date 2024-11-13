# import package
import turtle

# loop for pattern
for i in range(10):

	# set turtle delay
	turtle.delay(10 * i)

	# motion for pattern
	turtle.forward(50 + 10 * i)
	turtle.right(90)
