# Load the arrays from the .npz file
loaded_data = np.load('multiple_arrays.npz')

# Access individual arrays by their names
loaded_array1 = loaded_data['array1']
loaded_array2 = loaded_data['array2']
loaded_array3 = loaded_data['array3']

# Now you can use the loaded arrays as needed
print(loaded_array1)
print(loaded_array2)
print(loaded_array3)
