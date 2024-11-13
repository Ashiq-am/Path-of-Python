# Python3 code to demonstrate working of
# Mutiple Column Sort in Tuples
# Using sorted() + lambda

# initializing list
test_list = [(6, 7), (6, 5), (1, 4), (8, 10)]

# printing original list
print("The original list is : " + str(test_list))

# Mutiple Column Sort in Tuples
# Using sorted() + lambda
res = sorted(test_list, key = lambda sub: (-sub[0], sub[1]))

# printing result
print("The sorted records : " + str(res))
