# Python3 code to demonstrate
# Consecutive Product list
# using zip()

# initializing list
test_list = [1, 4, 5, 3, 6]

# printing original list
print ("The original list is : " + str(test_list))

# using zip()
# Consecutive Product list
res = [i * j for i, j in zip(test_list[: -1], test_list[1 :])]

# printing result
print ("The computed successive product list is : " + str(res))
