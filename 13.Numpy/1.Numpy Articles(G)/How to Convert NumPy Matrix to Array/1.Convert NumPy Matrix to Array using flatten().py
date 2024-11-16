import numpy as np

# Create NumPy 2-D array
matrix= np.matrix([[5, 10, 15],[20, 25, 30],[35, 40, 45]])

print("Given Matrix:",matrix)
print(type(matrix))

# Convert numpy matrix to array using flatten()
resulting_array = matrix.flatten()
print('After Conversion:',resulting_array)
print(type(matrix))
