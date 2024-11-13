# Python3 code to demonstrate working of
# K Divident Indices List
# using list comprehension

# initialize list
test_list = [5, 6, 10, 4, 7, 1, 19]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# K Divident Indices List
# using list comprehension
res = [idx for idx, ele in enumerate(test_list) if ele % K == 0]

# printing result
print("Indices list modulo K elements is : " + str(res))
