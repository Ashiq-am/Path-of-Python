# Python3 code to demonstrate working of
# Fill gaps in consecutive Records
# Using loop

# initializing list
test_list = [(1, 4), (3, 5), (4, 6), (7, 8), (9, 11)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K value
K = "New"

# Fill gaps in consecutive Records
# Using loop
res = []
cnt = 0
for i, j in test_list:
	if i - cnt > 1:
		for k in range(cnt + 1, i):
			res.append((k, K))
	res.append((i, j))
	cnt = i

# printing result
print("The list after filling gaps : " + str(res))
