# Python3 code to demonstrate working of
# Extract rows with Even length strings
# Using filter() + lambda + len()

# initializing list
test_list = [["gfg", "is", "best"], ["best", "good", "geek"], ["is", "better"], ["for", "cs"]]

# printing original list
print("The original list is : " + str(test_list))

# checking for all elements in row
# filtering done using filter() and lambda
res = list(filter(lambda row : all(len(ele) % 2 == 0 for ele in row), test_list))

# printing result
print("Rows with even length : " + str(res))
