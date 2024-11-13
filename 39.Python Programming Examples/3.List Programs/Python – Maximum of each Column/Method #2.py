# Python3 code to demonstrate
# Maximum index value
# using max() + map() + zip()

# initializing list
test_list = [[3, 7, 6], [1, 3, 5], [9, 3, 2]]

# printing original list
print("The original list : " + str(test_list))

# using max() + map() + zip()
# Maximum index value
res = list(map(max, zip(*test_list)))

# print result
print("The Maximum of each index list is : " + str(res))
