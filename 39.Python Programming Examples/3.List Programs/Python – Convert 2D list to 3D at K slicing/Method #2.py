# Python3 code to demonstrate working of
# Convert 2D list to 3D at K slicing
# Using zip() + list comprehension

# initializing list
test_list = [[6, 5], [2, 3], [3, 1], [4, 6], [3, 2], [1, 6]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# Convert 2D list to 3D at K slicing
# Using zip() + list comprehension
test_list = iter(test_list)
temp = [test_list] * K
res = [list(ele) for ele in zip(*temp)]

# printing result
print("Records after conversion : " + str(res))
