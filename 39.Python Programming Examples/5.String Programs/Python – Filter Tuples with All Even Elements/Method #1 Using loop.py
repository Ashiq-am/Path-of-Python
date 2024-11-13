# Python3 code to demonstrate working of
# Filter Tuples with All Even Elements
# Using loop

# initializing list
test_list = [(6, 4, 2, 8), (5, 6, 7, 6), (8, 0, 2), (7,)]

# printing original list
print("The original list is : " + str(test_list))

res_list = []
for sub in test_list:
    res = True

    # check if all are even
    for ele in sub:
        if ele % 2 != 0:
            res = False
            break
    if res:
        res_list.append(sub)

    # printing results
print("Filtered Tuples : " + str(res_list))
