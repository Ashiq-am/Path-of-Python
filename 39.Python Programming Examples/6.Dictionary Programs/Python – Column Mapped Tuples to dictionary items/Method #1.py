# Python3 code to demonstrate working of
# Column Mapped Tuples to dictionary items
# Using loop

# initializing list
test_list = [[(5, 6), (7, 4), (1, 2)],
             [(7, 3), (10, 14), (11, 22)]]

# printing original list
print("The original list : " + str(test_list))

res = dict()

# loop for tuple lists
for idx in range(len(test_list) - 1):
    for idx2 in range(len(test_list[idx])):
        # column wise dictionary pairing
        res[test_list[idx][idx2][0]] = test_list[idx + 1][idx2][0]
        res[test_list[idx][idx2][1]] = test_list[idx + 1][idx2][1]

# printing result
print("The constructed dictionary : " + str(res))
