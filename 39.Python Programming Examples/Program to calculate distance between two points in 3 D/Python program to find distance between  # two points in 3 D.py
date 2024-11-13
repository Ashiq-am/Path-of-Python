# Python program to find distance between
# two points in 3 D.

import math


# Function to find distance
def distance(x1, y1, z1, x2, y2, z2):
    d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) + math.pow(z2 - z1, 2) * 1.0)
    print("Distance is ")
    print(d)


# Driver Code
x1 = 2
y1 = -5
z1 = 7
x2 = 3
y2 = 4
z2 = 5

# function call for distance
distance(x1, y1, z1, x2, y2, z2)
