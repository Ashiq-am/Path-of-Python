# Use vectorize function of numpy
length_checker = np.vectorize(len)

# Find the length of each element
arr_len = length_checker(arr)

# Print the length of each element
print(arr_len)
