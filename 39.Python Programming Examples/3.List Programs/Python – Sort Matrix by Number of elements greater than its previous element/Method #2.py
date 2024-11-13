# Python3 code to demonstrate working of
# Sort Matrix by Next Greater Frequency
# Using sorted() + len() + lambda

# initializing list
test_list = [[4, 6, 2, 9, 10], [5, 3, 2, 5], [2, 4, 5, 6, 7, 7], [6, 3, 2]]

# printing original list
print("The original list is : " + str(test_list))

# performing one-liner sorting
# avoiding external fnc. call
res = sorted(test_list, key=lambda row: len(
	[row[idx] for idx in range(0, len(row) - 1) if row[idx] < row[idx + 1]]))

# printing result
print("Sorted rows : " + str(res))
