# initializing list
test_list = [3, 19, 4, 8, 10, 13]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# sorting list
test_list = sorted(test_list)

idx = 0
while idx < len(test_list) - 1:

    # checking for difference
    if test_list[idx] + K > test_list[idx + 1]:

        # deleting if K closer
        del test_list[idx + 1]
    else:
        idx += 1

# printing result
print("Required List : " + str(test_list))
