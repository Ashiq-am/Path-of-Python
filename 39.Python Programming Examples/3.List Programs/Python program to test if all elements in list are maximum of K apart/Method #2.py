# Python3 code to demonstrate working of
# Test if all elements are in range size
# Using min() + max()

# initializing list
test_list = [475, 503, 425, 520, 470, 500]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 100

# using min() and max() rather than
# changing order
res = max(test_list) - min(test_list) < K

# printing result
print("Are elements in range ? : " + str(res))
