# Creating a 3d-array of elements
arr = [[[4, 6, 3], [2, 6, 8], [3, 5, 12]],
	[[32, 11, 4], [23, 53, 89], [19, 17, 10]],
	[[14, 22, 52], [56, 43, 99], [20, 37, 32]]]

# Referring elements of the 3d-array
# by 3d index to new variables
first_second_second = arr[0][1][1]
second_first_third = arr[1][0][2]
third_third_first = arr[2][2][0]

# Print the variables
print("First Second Second Value =", first_second_second)
print("Second First Third Value =", second_first_third)
print("Third Third First Value =", third_third_first)
