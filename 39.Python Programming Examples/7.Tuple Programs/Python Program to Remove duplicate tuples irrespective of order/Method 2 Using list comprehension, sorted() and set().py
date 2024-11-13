# initializing list
test_list = [(4, 6), (1, 2), (9, 2), (2, 1), (5, 7), (6, 4), (9, 2)]

# printing original list
print("The original list is : " + str(test_list))

# sorting tuples
temp = [tuple(sorted(sub)) for sub in test_list]

# removing duplicates
res = list(set(temp))

# printing result
print("Tuples after removal : " + str(res))
