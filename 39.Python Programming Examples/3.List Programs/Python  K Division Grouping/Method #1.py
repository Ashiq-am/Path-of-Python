# Python3 code to demonstrate
# K Division Grouping
# using loops

# initializing list
test_list = [3, 12, 13, 22, 25, 30]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 7

# using loops
# K Division Grouping
res = []
dec = -1
for num in sorted(test_list):
	while num // K != dec:
		res.append([])
		dec += 1
	res[-1].append(num)

# print result
print("The list after grouping by K is : " + str(res))
