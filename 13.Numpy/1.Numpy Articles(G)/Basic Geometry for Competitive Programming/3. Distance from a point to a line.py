import math

# Method to get the magnitude of a vector
def get_magnitude(v):
	return math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])

# Method to calculate the cross product of two vectors v1
# and v2
def get_cross_product(v1, v2):
	cross_product = [0, 0, 0]
	cross_product[0] = v1[1] * v2[2] - v1[2] * v2[1]
	cross_product[1] = v1[2] * v2[0] - v1[0] * v2[2]
	cross_product[2] = v1[0] * v2[1] - v1[1] * v2[0]
	return cross_product

# Point from which we need to calculate the distance
pointA = [1, 4, -2]

# Points on the line P
pointB = [3, 1, -2]
pointC = [6, -2, 1]

# vector BA
vecBA = [pointA[0] - pointB[0], pointA[1] - pointB[1], pointA[2] - pointB[2]]
# vector BC
vecBC = [pointC[0] - pointB[0], pointC[1] - pointB[1], pointC[2] - pointB[2]]

# vector to store the cross product
cross_product = get_cross_product(vecBA, vecBC)

# Variable to store the distance of point A from line P
dist = get_magnitude(cross_product) / get_magnitude(vecBC)

print(dist)
