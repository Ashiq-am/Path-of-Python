# Python3 code to demonstrate working of
# Ordered tuples extraction
# Using filter() + lambda + sorted()

# initializing list
test_list = [(5, 4, 6, 2, 4), (3, 4, 6), (9, 10, 34), (2, 5, 6), (9, 1)]

# printing original list
print("The original list is : " + str(test_list))

# sorted() used to order, comparison operator to test
res = list(filter(lambda sub: tuple(sorted(sub)) == sub, test_list))

# printing result
print("Ordered Tuples : " + str(res))
