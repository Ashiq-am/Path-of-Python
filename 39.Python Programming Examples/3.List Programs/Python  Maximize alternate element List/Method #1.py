# Python3 code to demonstrate
# Maximize alternate element List
# using list comprehension + list slicing + max()

# initializing list
test_list = [2, 1, 5, 6, 8, 10]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + list slicing + max()
# Maximize alternate element List
res = [max(test_list[i : : 2]) for i in range(len(test_list) // (len(test_list)//2))]

# print result
print("The alternate elements maximum list : " + str(res))
