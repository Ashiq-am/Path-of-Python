# Python3 code to demonstrate working of
# K difference Consecutive elements
# Using list comprehension

# initializing list
test_list = [5, 6, 3, 2, 5, 3, 4]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 3

# using list comprehension and abs() to compute result
res = [True if abs(test_list[idx] - test_list[idx + 1]) == K else False
       for idx in range(len(test_list) - 1)]

# printing result
print("The difference list result : " + str(res))
