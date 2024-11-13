# Python3 code to demonstrate working of
# Test if all rows contain any common element with other Matrix
# Using loop any() "+" loop

# initializing lists
test_list1 = [[5, 6, 1], [2, 4], [9, 3, 5]]
test_list2 = [[9, 1, 2], [9, 8, 2], [3, 7, 10]]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

res = True
for idx in range(0, len(test_list1)):

    # checking for common element in list 2 in same index
    temp = any(ele in test_list2[idx] for ele in test_list1[idx])

    # if any element not found, Result is false
    if not temp:
        res = False
        break

# printing result
print("All row contain commmon elements with other Matrix : " + str(res))
