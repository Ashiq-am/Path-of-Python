# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Create a boolean mask
mask = array > 3

# Change the elements that meet the condition
array[mask] = 10

print(array)
