# Python3 code to demonstrate working of
# Group Consecutive elements by Sign
# Using loop

# initializing list
test_list = [5, -3, 2, 4, 6, -2, -1, -7,
             -9, 2, 3, 10, -3, -5, 3]

# printing original list
print("The original list is : " + str(test_list))

res = [[]]
for (idx, ele) in enumerate(test_list):

    # checking for similar signs by XOR
    if ele ^ test_list[idx - 1] < 0:
        res.append([ele])
    else:
        res[-1].append(ele)

# printing result
print("Elements after sign grouping : " + str(res))
