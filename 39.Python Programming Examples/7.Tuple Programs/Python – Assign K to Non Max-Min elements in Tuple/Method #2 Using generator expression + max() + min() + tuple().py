# Python3 code to demonstrate working of
# Assign K to Non Max-Min elements in Tuple
# Using generator expression + max() + min() + tuple()

# initializing tuple
test_tuple = (5, 6, 3, 6, 10, 34)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# initializing K
K = 4

# Assign K to Non Max-Min elements in Tuple
# Using generator expression + max() + min() + tuple()
res = tuple(ele if ele in [min(test_tuple), max(test_tuple)] else K for ele in test_tuple)

# printing result
print("The tuple after conversion: " + str(res))
