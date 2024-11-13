# Python3 program to demonstrate the atan() method

# imports math
import math

# list containing x and y coordinates
y = [1, 2, 3, 4]
x = [6, 3, 7, 8]

# traversing in range to get theta
# for all y and x co-ordinates
for i in range(len(x)):
	theta = math.atan2(y[i], x[i])
	print(theta)
