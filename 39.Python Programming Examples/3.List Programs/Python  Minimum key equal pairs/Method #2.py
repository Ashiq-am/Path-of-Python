# Python3 code to demonstrate working of
# Minimum key equal pairs
# using setdefault() + items() + loop + list comprehension

# initialize list
test_list = [(4, 3), (2, 3), (3, 10), (5, 10), (5, 6)]

# printing original list
print("The original list : " + str(test_list))

# Minimum key equal pairs
# using setdefault() + items() + loop + list comprehension
temp = {}
for val, key in test_list:
	if val < temp.setdefault(key, val):
		temp[key] = val
res = [(val, key) for key, val in temp.items()]

# printing result
print("Minimum key equal pairs : " + str(res))
