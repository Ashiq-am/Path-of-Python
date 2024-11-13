# Python3 code to demonstrate working of
# Omit K length Rows
# Using loop + len()

# initializing list
test_list = [[4, 7],
             [8, 10, 12, 8],
             [10, 11],
             [6, 8, 10]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

res = []
for row in test_list:

    # checking rows not K length
    if len(row) != K:
        res.append(row)

# printing result
print("Filtered Matrix : " + str(res))
