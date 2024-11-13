# Python3 code to demonstrate working of
# Elements Maximum till current index in List
# Using loop

# initializing list
test_list = [3, 5, 2, 6, 7, 9, 3]

# printing original list
print("The original list : " + str(test_list))

# Using loop
res = []
for idx in range(1, len(test_list)):
	cnt = 0

	# inner loop to count element less than current
	for idx2 in range(idx):
		if test_list[idx] > test_list[idx2]:
			cnt = cnt + 1
	if cnt == idx:
		res.append(test_list[idx])

# printing result
print("Extracted Maximum elements : " + str(res))
