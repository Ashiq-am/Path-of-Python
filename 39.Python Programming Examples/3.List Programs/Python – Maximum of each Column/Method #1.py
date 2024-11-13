# Python3 code to demonstrate
# Maximum of each Column
# using max() + list comprehension + zip()

# initializing list
test_list = [[3, 7, 6], [1, 3, 5], [9, 3, 2]]

# printing original list
print("The original list : " + str(test_list))

# using max() + list comprehension + zip()
# Maximum of each Column
res = [max(idx) for idx in zip(*test_list)]

# print result
print("The Maximum of each index list is : " + str(res))
