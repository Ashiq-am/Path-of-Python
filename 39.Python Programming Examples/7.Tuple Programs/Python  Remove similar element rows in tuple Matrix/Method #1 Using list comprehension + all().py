# Python3 code to demonstrate working of
# Remove similar element rows in tuple Matrix
# using list comprehension + all()

# initialize tuple
test_tup = ((1, 3, 5), (2, 2, 2),
			(9, 10, 10), (4, 4, 4))

# printing original tuple
print("The original tuple : " + str(test_tup))

# Remove similar element rows in tuple Matrix
# using list comprehension + all()
res = tuple(ele for ele in test_tup if not all(sub == ele[0] for sub in ele))

# printing result
print("The tuple after removal of like-element rows : " + str(res))
