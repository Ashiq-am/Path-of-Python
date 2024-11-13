# Python3 code to demonstrate working of
# Remove Rows for similar Kth column element
# Using loop

# initializing list
test_list = [[3, 4, 5], [2, 3, 5], [10, 4, 3], [7, 8, 9], [9, 3, 6]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 1

res = []
memo = []
for sub in test_list:

    # in operator used to check if present or not
    if not sub[K] in memo:
        res.append(sub)
        memo.append(sub[K])

# printing result
print("The filtered Matrix : " + str(res))
