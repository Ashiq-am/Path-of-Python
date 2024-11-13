# Python3 code to demonstrate working of
# Convert Matrix to overlapping Tuple Pairs
# Using loop

# initializing list
test_list = [[5, 6, 7], [8, 6, 5], [2, 5, 7]]

# printing original list
print("The original list is : " + str(test_list))

# Convert Matrix to overlapping Tuple Pairs
# Using loop
res = []
for sub in test_list:
    res.append((sub[0], sub[1]))
res.append((sub[1], sub[2]))

# printing result
print("Filtered tuples : " + str(res))
