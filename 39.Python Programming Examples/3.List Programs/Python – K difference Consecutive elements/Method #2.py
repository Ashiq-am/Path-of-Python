# Python3 code to demonstrate working of
# K difference Consecutive elements
# Using zip() + list comprehension

# initializing list
test_list = [5, 6, 3, 2, 5, 3, 4]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 3

# using list comprehension and abs() to compute result
# zip() used to pair Consecutive elements list
res = [abs(a - b) == K for a, b in zip(test_list, test_list[1:])]

# printing result
print("The difference list result : " + str(res))
