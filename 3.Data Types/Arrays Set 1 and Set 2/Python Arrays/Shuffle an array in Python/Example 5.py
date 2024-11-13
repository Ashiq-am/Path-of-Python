# Import required module
import random
import numpy as np


# A function to generate a random
# permutation of array
def shuffler(arr, n):
    # We will Start from the last element
    # and swap one by one.
    for i in range(n - 1, 0, -1):
        # Pick a random index from 0 to i
        j = random.randint(0, i + 1)

        # Swap arr[i] with the element at random index
        arr[i], arr[j] = arr[j], arr[i]
    return arr


# Driver code

# Assign array
arr = np.array([1, 2, 3, 4, 5, 6])

# Display original array
print("Original array: ", arr)

# Get length of array
n = len(arr)

# Use shuffler() function to get shuffled array
print("Shuffled array: ", shuffler(arr, n))
