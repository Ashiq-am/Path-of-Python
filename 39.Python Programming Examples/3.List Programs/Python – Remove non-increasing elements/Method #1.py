# Python3 code to demonstrate working of
# Remove non-increasing elements
# Using loop

# initializing list
test_list = [5, 3, 4, 5, 7, 3, 9, 10, 3, 10, 12, 13, 3, 16, 1]

# printing original list
print("The original list is : " + str(test_list))

res = [test_list[0]]
for ele in test_list:

    # checking preceeding element to decide for greater element
    if ele >= res[-1]:
        res.append(ele)

# printing result
print("The list after removing non-increasing elements : " + str(res))
