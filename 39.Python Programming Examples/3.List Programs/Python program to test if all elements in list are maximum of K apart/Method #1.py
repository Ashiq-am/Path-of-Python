# Python3 code to demonstrate working of
# Test if all elements are in range size
# Using sort()

# initializing list
test_list = [475, 503, 425, 520, 470, 500]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 100

# sorting list
test_list.sort()

# checking if greater than range
res = test_list[-1] - test_list[0] < K

# printing result
print("Are elements in range ? : " + str(res))
