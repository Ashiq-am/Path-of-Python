# Python3 code to demonstrate working of
# Test for all Even elements in List Range
# Using loop

# initializing list
test_list = [3, 1, 4, 6, 8, 10, 1, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 2, 5

res = True
for idx in range(i, j + 1):

    # check if any odd
    if test_list[idx] % 2:
        res = False
        break

# printing result
print("Are all elements even in range : " + str(res))
