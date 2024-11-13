# Python3 code to demonstrate working of
# Reform K digit elements
# Using list comprehension + join()

# initializing list
test_list = [223, 67, 332, 1, 239, 2, 931]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# converting to string
temp = ''.join([str(ele) for ele in test_list])

# getting K digit slices
# using 1 liner list comprehension
res = [int(temp[idx: idx + K]) for idx in range(0, len(temp), K)]

# printing result
print("Reforming K digits : " + str(res))
