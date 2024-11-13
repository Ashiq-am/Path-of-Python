# Python3 code to demonstrate working of
# Check if all tuples have element difference less than K
# Using all()

# initializing list
test_list = [(3, 4), (1, 2), (7, 8), (9, 8)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# shorthand to solve this problem
res = all(abs(sub1 - sub2) < K for sub1, sub2 in test_list)

# printing result
print("Are all elements difference less than K ? : " + str(res))
