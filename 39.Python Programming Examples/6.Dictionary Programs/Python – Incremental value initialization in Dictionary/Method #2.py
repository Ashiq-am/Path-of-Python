# Python3 code to demonstrate
# Incremental value initialization in Dictionary
# using dict() + zip()

# initializing list
test_list = ['Nikhil', 'Akshat', 'Akash', 'Manjeet']

# printing original list
print("The original list : " + str(test_list))

# initialization K
K = 4

# using dict() + zip()
# Incremental value initialization in Dictionary
res = dict(zip(test_list, range(K, len(test_list) * (K + 1), K)))

# print result
print("The Dictionary after index keys : " + str(res))
