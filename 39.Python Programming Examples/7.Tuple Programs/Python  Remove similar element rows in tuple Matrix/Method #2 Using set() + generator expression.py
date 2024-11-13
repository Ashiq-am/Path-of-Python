# Python3 code to demonstrate working of
# Remove similar element rows in tuple Matrix
# using set() + generator expression

# initialize tuple
test_tup = ((1, 3, 5), (2, 2, 2),
			(9, 10, 10), (4, 4, 4))

# printing original tuple
print("The original tuple : " + str(test_tup))

# Remove similar element rows in tuple Matrix
# using set() + generator expression
res = tuple(ele for ele in test_tup if len(set(ele)) > 1)

# printing result
print("The tuple after removal of like-element rows : " + str(res))
