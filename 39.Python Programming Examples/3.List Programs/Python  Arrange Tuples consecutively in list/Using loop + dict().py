# Python3 code to demonstrate working of
# Arranging Tuples consecutively in list
# using loop + dict()

# initialize list
test_list = [(5, 6), (11, 8), (6, 11), (8, 9) ]

# printing original list
print("The original list is : " + str(test_list))

# Arranging Tuples consecutively in list
# using loop + dict()
temp = dict(test_list)
ele = test_list[0][0]
res = []
for _ in range(len(test_list)):
	res.append((ele, temp[ele]))
	ele = temp[ele]

# printing result
print("The arranged list is : " + str(res))
