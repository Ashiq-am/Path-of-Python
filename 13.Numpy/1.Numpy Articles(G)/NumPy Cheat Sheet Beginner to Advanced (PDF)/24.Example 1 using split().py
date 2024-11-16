# Making of a 3x3 array
a = np.arange(9).reshape(3, 3)
print(a)

# Horizontal splitting of array 'a'
# using 'split' with axis parameter = 1.
print("Splitted array in horizontal form:\n", np.split(a, 3, 1))

# Vertical splitting of array 'a'
# using 'split' with axis parameter = 0.
print("\nSplitted array in vertical form:\n", np.split(a, 3, 0))
