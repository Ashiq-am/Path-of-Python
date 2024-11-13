# Python3 code to demonstrate
# Finding missing elements in List
# using list comprehension

# initializing list
test_list = [3, 5, 6, 8, 10]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension
# Finding missing elements in List
res = [ele for ele in range(max(test_list)+1) if ele not in test_list]

# print result
print("The list of missing elements : " + str(res))
