# Python3 code to demonstrate working of
# Split in Nested tuples
# map() + list()

# initializing list
test_list = [(3, ('Gfg', 'best')), (10, ('CS', 'good')), (7, ('Gfg', 'better'))]

# printing original list
print("The original list is : " + str(test_list))

# Split in Nested tuples
# map() + list()
res = []
for sub in test_list:
	res.append(list(map(str, (*[sub[0]], *[*sub[1]]))))

# printing result
print("The splitted elements : " + str(res))
