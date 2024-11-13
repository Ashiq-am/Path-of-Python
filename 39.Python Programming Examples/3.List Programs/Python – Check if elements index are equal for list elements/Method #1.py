# Python3 code to demonstrate working of
# Check if elements index are equal for list elements
# Using loop

# initializing lists
test_list1 = [2, 6, 9, 7, 8]
test_list2 = [2, 7, 9, 4, 8]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# initializing check_list
check_list = [9, 8, 2]

res = True
for idx, ele in enumerate(test_list1):

    # check for indifference and containment
    if test_list1[idx] != test_list2[idx] and ele in check_list:
        res = False
        break

# printing result
print("Are elements at same index for required instances ?: " + str(res))
