# Python3 code to demonstrate
# to generate successive difference list
# using zip()

# initializing list
test_list = [1, 4, 5, 3, 6]

# printing original list
print ("The original list is : " + str(test_list))

# using zip()
# generate successive difference list
res = [j - i for i, j in zip(test_list[: -1], test_list[1 :])]

# printing result
print ("The computed successive difference list is : " + str(res))
