# Python3 code to demonstrate working of
# Remove Kth Index Duplicates in Tuple
# Using loop

# initializing lists
test_list = [(4, 5, 6), (2, 3, 4), (1, 3, 4), (7, 6, 4), (1, 2, 6)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# Remove Kth Index Duplicates in Tuple
# Using loop
keep = set()
res = []
for sub in test_list:
    if sub[K] not in keep:
        res.append(sub)
        keep.add(sub[K])

# printing result
print("Filtered Tuples : " + str(res))
