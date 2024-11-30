import numpy as np

# Take input for the number of elements
n = int(input("Enter the number of elements: "))

# Use list comprehension to collect elements
val = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]

# Convert to NumPy array
arr = np.array(val)
print(arr)