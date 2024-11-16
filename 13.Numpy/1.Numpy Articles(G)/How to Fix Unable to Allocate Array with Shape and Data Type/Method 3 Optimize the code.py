import numpy as np


def inplace_operation(array):  # Function to perform an in-place operation on a NumPy array
    array **= 2  # Example: Squaring each element in-place


large_array = np.random.rand(10000, 10000)  # Create a large array

view_of_array = large_array[:, :500]  # Use views instead of creating new arrays

inplace_operation(view_of_array)  # Call the in-place operation function on the view
# Now 'large_array' has been modified in-place without creating a new array
print(f"Memory usage of large_array:", (large_array.nbytes))  # Display memory usage
