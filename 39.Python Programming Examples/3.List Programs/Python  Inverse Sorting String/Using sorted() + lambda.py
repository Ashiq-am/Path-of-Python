# Python3 code to demonstrate working of
# Inverse sorting String, Integer tuple list
# Using sorted() + lambda

# initializing list
test_list = [("Geeks", 5), ("For", 3), ("Geeks", 6), ("Is", 5),
			("Best", 7 ), ("For", 5), ("CS", 3)]

# printing original list
print("The original list is : " + str(test_list))

# Inverse sorting String, Integer tuple list
# Using sorted() + lambda
res = sorted(test_list, key = lambda sub: (-sub[1], sub[0]))

# printing result
print("The list after inverse sorted tuple elements : " + str(res))
