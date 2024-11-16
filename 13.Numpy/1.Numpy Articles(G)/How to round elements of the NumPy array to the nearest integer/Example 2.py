import numpy as n

# create array
y = n.array([-0.2, 0.7, -1.4, -4.5, -7.6, -19.7])
print("Original array:", end=" ")
print(y)

# rount to nearest integer
y = n.rint(y)
print("After rounding off:", end=" ")
print(y)
