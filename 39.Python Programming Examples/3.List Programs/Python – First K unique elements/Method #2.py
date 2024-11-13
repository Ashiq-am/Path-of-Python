# Python3 code to demonstrate working of
# First K unique elements
# Using set() + filter() + lambda

# initializing list
test_list = [6, 7, 6, 7, 8, 3, 9, 11]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# First K unique elements
# Using set() + filter() + lambda
store = set(list({ele for ele in test_list})[:K])
res = list(filter(lambda ele: ele in store, test_list))

# printing result
print("The extracted elements : " + str(res))
