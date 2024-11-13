# Python3 code to demonstrate working of
# Index Ranks of Elements
# Using loop + filter() + list comprehension. + set() + sum() + loop

# initializing list
test_list = [3, 4, 6, 5, 3, 4, 9,
             1, 2, 1, 8, 3, 2, 3, 9]

# printing original list
print("The original list is : " + str(test_list))

res = []
all_ele = set(test_list)
for ele in all_ele:
    # getting indices of each element
    indices = list(filter(lambda sub: test_list[sub] == ele, range(len(test_list))))

    # index rank
    idx_rank = sum(indices) / ele
    res.append((ele, idx_rank))

# printing result
print("Index rank of each element : " + str(res))
