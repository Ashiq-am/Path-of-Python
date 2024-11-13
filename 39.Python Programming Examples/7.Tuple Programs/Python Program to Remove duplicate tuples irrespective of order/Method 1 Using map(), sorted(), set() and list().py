# initializing list
test_list = [(4, 6), (1, 2), (9, 2), (2, 1), (5, 7), (6, 4), (9, 2)]

# printing original list
print("The original list is : " + str(test_list))

# using map() to get all sorted
# set removes duplicates
res = list({*map(tuple, map(sorted, test_list))})

# printing result
print("Tuples after removal : " + str(res))
