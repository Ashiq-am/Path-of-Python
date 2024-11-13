# Python3 code to demonstrate
# Incremental value initialization in Dictionary
# using Dictionary comprehension + enumerate()

# initializing list
test_list = ['Nikhil', 'Akshat', 'Akash', 'Manjeet']

# printing original list
print("The original list : " + str(test_list))

# initialization K
K = 4

# using Dictionary comprehension + enumerate()
# Incremental value initialization in Dictionary
res = {val : (K * (idx + 1)) for idx, val in enumerate(test_list)}

# print result
print("The Dictionary after index keys : " + str(res))
