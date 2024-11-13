# Python3 code to demonstrate working of
# Filter Tuple with Elements capped on K
# Using loop

# initializing list
test_list = [(4, 5, 3), (3, 4, 7), (4, 3, 2), (4, 7, 8)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

res_list = []
for sub in test_list:
    res = True
    for ele in sub:

        # check if any element is greater than K
        if ele > K:
            res = False
            break
    if res:
        res_list.append(sub)

# printing result
print("The filtered tuples : " + str(res_list))
