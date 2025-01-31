# Python3 code to demonstrate
# Dictionary with index as value
# using dict() + zip()

# initializing list
test_list = ['Nikhil', 'Akshat', 'Akash', 'Manjeet']

# printing original list
print("The original list : " + str(test_list))

# using dict() + zip()
# Dictionary with index as value
res = dict(zip(test_list, range(1, len(test_list)+1)))

# print result
print("The Dictionary after index keys : " + str(res))
