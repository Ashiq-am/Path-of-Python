# Python3 code to demonstrate working of
# Filter similar elements Tuples
# Using filter() + lamdba + set() + len()

# initializing list
test_list = [(5, 6, 5, 5), (6, 6, 6), (1, 1), (9, 10)]

# printing original list
print("The original list is : " + str(test_list))

# end result converted to list object
# filter extracts req. tuples
res = list(filter(lambda sub: len(set(sub)) == 1, test_list))

# printing results
print("Filtered Tuples : " + str(res))
