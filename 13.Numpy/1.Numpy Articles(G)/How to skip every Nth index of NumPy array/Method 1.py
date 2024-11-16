# importing required packages
import numpy as np

# declaring a numpy array
x = np.array([1.2, 3.0, 6.7, 8.7, 8.2,
              1.3, 4.5, 6.5, 1.2, 3.0,
              6.7, 8.7, 8.2, 1.3, 4.5,
              6.5])

# skipping every 4th element
n = 4

# declaring new list
new_arr = []

# maintaining cntr
cntr = 0

# looping over array
for i in x:

    # checking if element is nth pos
    if (cntr % n != 0):
        new_arr.append(i)

    # incrementing counter
    cntr += 1

print("Array after skipping nth element")
print(new_arr)
