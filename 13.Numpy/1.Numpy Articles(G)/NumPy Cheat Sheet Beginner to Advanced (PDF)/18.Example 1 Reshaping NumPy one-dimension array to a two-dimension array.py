# creating a numpy array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

# printing array
print("Array: " + str(array))

# reshaping numpy array
# converting it to 2-D from 1-D array
reshaped1 = array.reshape((4, array.size//4))

# printing reshaped array
print("First Reshaped Array:")
print(reshaped1)

# creating another reshaped array
reshaped2 = np.reshape(array, (2, 8))

# printing reshaped array
print("\nSecond Reshaped Array:")
print(reshaped2)
