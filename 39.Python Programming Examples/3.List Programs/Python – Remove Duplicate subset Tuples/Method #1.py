# Python3 code to demonstrate working of
# Remove Duplicate subset Tuples
# Using setdefault() + list comprehension

# initializing lists
test_list = [(6, 9, 17, 18), (15, 34, 56), (6, 7), (6, 9), (15, 34)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# Remove Duplicate subset Tuples
# Using setdefault() + list comprehension
temp = {}
for sub in test_list:
	temp2 = sub[:K]
	temp.setdefault(temp2, []).append(sub)
res = [sub for sub in test_list if len(sub) > K or len(temp[sub]) == 1]

# printing result
print("Tuple list after removal : " + str(res))
