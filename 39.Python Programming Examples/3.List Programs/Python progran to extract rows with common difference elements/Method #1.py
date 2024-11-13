# Python3 code to demonstrate working of
# Extract rows with common difference elements
# Using loop

# initializing list
test_list = [[4, 7, 10],
             [8, 10, 12],
             [10, 11, 13],
             [6, 8, 10]]

# printing original list
print("The original list is : " + str(test_list))

res = []
for row in test_list:
    flag = True
    for idx in range(0, len(row) - 1):

        # check for common difference
        if row[idx + 1] - row[idx] != row[1] - row[0]:
            flag = False
            break
    if flag:
        res.append(row)

# printing result
print("Filtered Matrix : " + str(res))
