# Python3 code to demonstrate
# String Matrix Concatenation
# Using list comprehension

# initializing list
test_list = [["geeksforgeeks", " is", " best"], [" I", " Love"], [" Gfg"]]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension
# count of all the elements in list
res = "".join([ele for sub in test_list for ele in sub])

# print result
print("The Matrix Concatenation is : " + str(res))
