# Python3 code to demonstrate working of
# Ordered tuples extraction
# Using list comprehension + sorted()

# initializing list
test_list = [(5, 4, 6, 2, 4), (3, 4, 6), (9, 10, 34), (2, 5, 6), (9, 1)]

# printing original list
print("The original list is : " + str(test_list))

# sorted() used to order, comparison operator to test
res = [sub for sub in test_list if tuple(sorted(sub)) == sub]

# printing result
print("Ordered Tuples : " + str(res))
