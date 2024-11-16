# Load the saved arrays
data = np.load('multiple_arrays_compressed.npz')
loaded_array1 = data['array1']
loaded_array2 = data['array2']
loaded_array3 = data['array3']

print(loaded_array1)
print(loaded_array2)
print(loaded_array3)
