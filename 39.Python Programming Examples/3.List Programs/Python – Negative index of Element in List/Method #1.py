# Python3 code to demonstrate working of
# Negative index of Element
# Using index() + len()

# initializing list
test_list = [5, 7, 8, 2, 3, 5, 1]

# printing original list
print("The original list is : " + str(test_list))

# initializing Element
K = 3

# getting length using len() and subtracting index from it
res = len(test_list) - test_list.index(K)

# printing result
print("The required Negative index : -" + str(res))
