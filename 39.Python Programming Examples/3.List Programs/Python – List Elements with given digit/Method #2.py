# Python3 code to demonstrate working of
# Elements with K digit
# Using filter() + lambda + str()

# initializing list
test_list = [56, 72, 875, 9, 173]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 7

# using filter() and lambda to perform conditionals
# using str() to perform data type conversions
res = list(filter(lambda ele: str(K) in str(ele), test_list))

# printing result
print("Elements with digit K : " + str(res))
