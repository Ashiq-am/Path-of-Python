# Python3 code to demonstrate working of
# Test if tuple list has Single element
# Using loop

# initializing list
test_list = [(3, 3, 3), (3, 3), (3, 3, 3), (3, 3)]

# printing original list
print("The original list is : " + str(test_list))

# checking for similar elements in list
res = True
for sub in test_list:
    flag = True
    for ele in sub:

        # checking for element to be equal to initial element
        if ele != test_list[0][0]:
            flag = False
            break
    if not flag:
        res = False
        break

# printing result
print("Are all elements equal : " + str(res))
