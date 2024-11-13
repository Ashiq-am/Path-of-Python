# Python program to solve linear
# equation and return 3-d graph

# IMport the libraries
import numpy as np

x1, y1, z1, w1 = 1, -2, 3, 9

# Take the input for equation-2
x2, y2, z2, w2 = -1, 3, -1, -6

# Take the input for equation-3
x3, y3, z3, w3 = 2, -5, 5, 17

# Create an array for LHS variables
LHS = np.array([[x1, y1, z1],
				[x2, y2, z2],
				[x3, y3, z3]])

# Create another array for RHS variables
RHS = np.array([w1, w2, w3])

# Apply linear algebra on any numpy
# array created and printing the output
sol = np.linalg.solve(LHS, RHS)
print(sol)
