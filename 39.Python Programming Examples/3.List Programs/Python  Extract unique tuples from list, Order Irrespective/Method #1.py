# Python3 code to demonstrate working of
# Extract unique tuples from list(Order Irrespective)
# using list comprehension + set()

# initialize tuples list
test_list = [(1, 3), (4, 5), (3, 1), (1, 10), (5, 4)]

# printing original list
print("The original list : " + str(test_list))

# Extract unique tuples from list(Order Irrespective)
# using list comprehension + set()
res = set()
temp = [res.add((a, b)) for (a, b) in test_list
			if (a, b) and (b, a) not in res]

# printing result
print("The list after duplicated removal : " + str(list(res)))
