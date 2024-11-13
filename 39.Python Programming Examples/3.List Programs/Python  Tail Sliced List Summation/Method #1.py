# Python code to demonstrate
# Tail Sliced List Summation
# using len() + list slicing + sum()

# initializing list
test_list = [1, 4, 6, 3, 5, 8]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 3

# using len() + list slicing + sum()
# Tail Sliced List Summation
res = sum(test_list[: len(test_list) - K])

# printing result
print ("The tail removed list summation : " + str(res))
