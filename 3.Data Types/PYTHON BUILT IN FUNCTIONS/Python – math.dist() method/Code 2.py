# Python Program to explain math.dist() method

# Importing math module
import math

# Two dimensional Point

# Coordinates of Point P
Px = 3
Py = 7

# Coordinates of point Q
Qx = -5
Qy = -9

# Calculate the Euclidean distance
# between points P and Q
eDistance = math.dist([Px, Py], [Qx, Qy])
print(eDistance)


# Three-dimensional point

# Coordinates of Point P
P = [3, 6, 9]

# Coordinates of point Q
Q = [1, 0, -2]

# Calculate the Euclidean distance
# between points P and Q
eDistance = math.dist(P, Q)
print(eDistance)
