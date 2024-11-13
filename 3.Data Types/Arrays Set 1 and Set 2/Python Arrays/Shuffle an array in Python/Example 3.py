# Import required module
import random
import array

# Assign array
# here q indicates that the array
# contains signed integer
arr = array.array('q', [1, 2, 3, 4, 5, 6])

# Display original array
print("Original array: ", arr)

# Shuffle array
# Here sample() returns a list, so we
# are typecasting list into array
arr = array.array('q', random.sample(list(arr), 6))

# Display shuffled array
print("Shuffled array: ", arr)
