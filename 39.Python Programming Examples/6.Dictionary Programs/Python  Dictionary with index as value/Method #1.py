# Python3 code to demonstrate
# Dictionary with index as value
# using Dictionary comprehension + enumerate()

# initializing list
test_list = ['Nikhil', 'Akshat', 'Akash', 'Manjeet']

# printing original list
print("The original list : " + str(test_list))

# using Dictionary comprehension + enumerate()
# Dictionary with index as value
res = {val : idx + 1 for idx, val in enumerate(test_list)}

# print result
print("The Dictionary after index keys : " + str(res))
