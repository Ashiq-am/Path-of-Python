# Python3 code to demonstrate
# Summation of each column in Matrix
# using map() + sum() + zip()

# initializing list
test_list = [[3, 7, 6], [1, 3, 5], [9, 3, 2]]

# printing original list
print("The original list : " + str(test_list))

# using map() + sum() + zip()
# Summation of each column in Matrix
res = list(map(sum, zip(*test_list)))

# print result
print("The Summation of each index list is : " + str(res))
