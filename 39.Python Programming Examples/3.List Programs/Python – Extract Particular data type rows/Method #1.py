# Python3 code to demonstrate working of
# Extract Particular data type rows
# Using isinstance() + all() + list comprehension

# initializing list
test_list = [[4, 5, "Hello"], [2, 6, 7], ["g", "f", "g"], [9, 10, 11]]

# printing original list
print("The original list is : " + str(test_list))

# initializing data type
data_type = int

# checking data type using isinstance
res = [row for row in test_list if all(
	isinstance(ele, data_type) for ele in row)]

# printing result
print("Filtered Rows : " + str(res))
