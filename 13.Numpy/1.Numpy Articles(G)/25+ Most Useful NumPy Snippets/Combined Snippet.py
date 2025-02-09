import numpy as np

# 1. Array Creation
# Creating 1D and 2D arrays
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:\n", array_1d)
print(' ')
print("2D Array:\n", array_2d)
print(' ')


# Using built-in functions
zeros_array = np.zeros((2, 3))
ones_array = np.ones((3, 3))
arange_array = np.arange(0, 10, 2)
linspace_array = np.linspace(0, 1, 5)

print("\nZeros Array:\n", zeros_array)
print(' ')
print("Ones Array:\n", ones_array)
print(' ')
print("Arange Array:\n", arange_array)
print(' ')
print("Linspace Array:\n", linspace_array)
print(' ')


# 2. Mathematical Operations
# Element-wise arithmetic operations
addition_result = array_1d + 10
multiplication_result = array_1d * 2

print("\nAddition Result:\n", addition_result)
print(' ')
print("Multiplication Result:\n", multiplication_result)
print(' ')

# Using universal functions (ufuncs)
squared_array = np.square(array_1d)
print("\nSquared Array:\n", squared_array)
print(' ')

# Aggregate functions
mean_value = np.mean(array_1d)
std_dev_value = np.std(array_1d)

print("\nMean Value:", mean_value)
print(' ')
print("Standard Deviation:", std_dev_value)
print(' ')

# 3. Indexing and Slicing
sliced_array = array_1d[1:4]
boolean_indexed_array = array_1d[array_1d > 2]

print("\nSliced Array (Index 1 to 3):\n", sliced_array)
print(' ')
print("Boolean Indexed Array (Values > 2):\n", boolean_indexed_array)
print(' ')

# 4. Reshaping and Flattening Arrays
reshaped_array = array_2d.reshape(3, 2) # Reshape to (3,2)
flattened_array = array_2d.flatten()

print("\nReshaped Array (3x2):\n", reshaped_array)
print(' ')
print("Flattened Array:\n", flattened_array)
print(' ')

# 5. Reading and Writing Data
# Saving an array to a text file
np.savetxt('array_data.txt', array_2d)

# Loading the saved data
loaded_data = np.loadtxt('array_data.txt')
print("\nLoaded Data from Text File:\n", loaded_data)
print(' ')

# Exception Handling Example
try:
    # Attempting an operation that may fail
    invalid_operation = np.array([1, 'two', 3]) + np.array([4, 5])
except TypeError as e:
    print("\nTypeError occurred:", e)
    print(' ')

# Conclusion: Demonstrating integration with other libraries (optional)
import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame from a NumPy array
df = pd.DataFrame(array_2d, columns=['Column1', 'Column2', 'Column3'])
print("\nDataFrame from NumPy Array:\n", df)

# Plotting the DataFrame using Matplotlib
df.plot(kind='bar')
plt.title('Bar Plot of DataFrame')
plt.xlabel('Index')
plt.ylabel('Values')
plt.show()