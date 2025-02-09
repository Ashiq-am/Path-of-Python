# Creating a multi-dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Calculating the sum of all elements
total_sum = np.sum(arr)
print("Total Sum:", total_sum)

# Calculating the mean of all elements
mean_value = np.mean(arr)
print("Mean Value:", mean_value)

# Calculating the standard deviation
std_dev = np.std(arr)
print("Standard Deviation:", std_dev)

# Summing along specific axes
sum_axis0 = np.sum(arr, axis=0)  # Sum along columns
print("Sum along axis 0 (columns):", sum_axis0)

sum_axis1 = np.sum(arr, axis=1)  # Sum along rows
print("Sum along axis 1 (rows):", sum_axis1)