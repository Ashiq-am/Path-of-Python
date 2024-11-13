# Python3 program to demonstrate
# the atan2() method

# imports math
import math

# prints the theta value of
# two negative co-ordinates
theta1 = math.atan2(-0.9, -0.9)
print("atan2(-0.9, -0.9) : ", theta1)

# prints the theta value of
# two positive co-ordinates
theta2 = math.atan2(1.2, 1.5)
print("atan2(1.2, 1.5) : ", theta2)

# prints the theta value of one
# positive and one negative co-ordinates
theta3 = math.atan2(1.2, -1.5)
print("atan2(1.2, -1.5):", theta3)
