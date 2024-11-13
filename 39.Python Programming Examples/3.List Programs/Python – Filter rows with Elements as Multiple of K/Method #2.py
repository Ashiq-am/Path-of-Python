# Python3 code to demonstrate working of
# Access element at Kth index in String
# Using filter() + lambda + all()

# initializing string list
test_list = [[5, 10, 15], [4, 8, 3], [100, 15], [5, 10, 23]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# using all() to check for all elements being multiples of K
res = list(filter(lambda sub : all(ele % K == 0 for ele in sub), test_list))

# printing result
print("Rows with K multiples : " + str(res))
