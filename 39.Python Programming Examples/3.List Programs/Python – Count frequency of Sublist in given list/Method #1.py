# Python3 code to demonstrate working of
# Sublist Frequency
# Using list comprehension + slicing

# initializing list
test_list = [4, 5, 3, 5, 7, 8, 3, 5, 7, 2, 7, 3, 2]

# printing original list
print("The original list is : " + str(test_list))

# initializing Sublist
sublist = [3, 5, 7]

# slicing is used to extract chunks and compare
res = len([sublist for idx in range(len(test_list)) if test_list[idx : idx + len(sublist)] == sublist])

# printing result
print("The sublist count : " + str(res))
