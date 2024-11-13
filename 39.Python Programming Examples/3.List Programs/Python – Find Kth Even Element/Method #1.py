# Python3 code to demonstrate working of
# Kth Even Element
# Using list comprehension

# initializing list
test_list = [4, 6, 2, 3, 8, 9, 10, 11]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# list comprehension to perform iteration and % 2 check
res = [ele for ele in test_list if ele % 2 == 0][K]

# printing result
print("The Kth Even Number : " + str(res))
