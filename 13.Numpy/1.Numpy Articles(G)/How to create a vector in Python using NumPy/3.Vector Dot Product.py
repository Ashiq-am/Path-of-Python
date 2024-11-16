# importing numpy
import numpy as np

# creating a 1-D list (Horizontal)
list1 = [5, 6, 9]

# creating a 1-D list (Horizontal)
list2 = [1, 2, 3]

# creating first vector
vector1 = np.array(list1)

# printing vector1
print("First Vector : " + str(vector1))

# creating secodn vector
vector2 = np.array(list2)

# printing vector2
print("Second Vector : " + str(vector2))

# getting dot product of both the vectors
# a . b = (a1 * b1 + a2 * b2 + a3 * b3)
# a . b = (a1b1 + a2b2 + a3b3)
dot_product = vector1.dot(vector2)

# printing dot product
print("Dot Product : " + str(dot_product))
