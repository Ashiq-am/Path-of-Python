# Python3 code to demonstrate working of
# Extract Particular data type rows
# Using filter() + lambda + isinstance()

# initializing list
test_list = [[4, 5, "Hello"], [2, 6, 7], ["g", "f", "g"], [9, 10, 11]]

# printing original list
print("The original list is : " + str(test_list))

# initializing data type
data_type = int

# checking data type using isinstance
# filter() used to get filter
res = list(filter(lambda row: all(isinstance(ele, data_type)
								for ele in row), test_list))

# printing result
print("Filtered Rows : " + str(res))
