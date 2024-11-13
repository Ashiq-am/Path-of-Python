# Python3 code to demonstrate
# Maximum product using K elements
# using max() + sort() + list comprehension

# Initializing list
test_list = [8, 5, 9, 11, 3, 7]

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 3

# Maximum product using K elements
# using max() + sort() + list comprehension
test_list.sort()
res = max(test_list[0] * test_list[1] * test_list[-1], test_list[-1] * test_list[-2] * test_list[-3])

# printing result
print ("Maximum product using K elements : " + str(res))
