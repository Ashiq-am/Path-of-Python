# Python3 code to demonstrate working of
# Convert Matrix to dictionary
# Using dictionary comprehension + enumerate()

# initializing list
test_list = [[5, 6, 7], [8, 3, 2], [8, 2, 1]]

# printing original list
print("The original list is : " + str(test_list))

# enumerate used to perform assigning row number
res = {idx: val for idx, val in enumerate(test_list, start = 1)}

# printing result
print("The constructed dictionary : " + str(res))
