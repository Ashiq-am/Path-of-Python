# Python3 code to demonstrate working of
# Extract rows with Even length strings
# Using all() + list comprehension + len()

# initializing list
test_list = [["gfg", "is", "best"], ["best", "good", "geek"], ["is", "better"], ["for", "cs"]]

# printing original list
print("The original list is : " + str(test_list))

# checking for all elements in row
res = [row for row in test_list if all(len(ele) % 2 == 0 for ele in row)]

# printing result
print("Rows with even length : " + str(res))
