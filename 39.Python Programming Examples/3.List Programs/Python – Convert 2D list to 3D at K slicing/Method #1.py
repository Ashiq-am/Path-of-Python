# Python3 code to demonstrate working of
# Convert 2D list to 3D at K slicing
# Using loop

# initializing list
test_list = [[6, 5], [2, 3], [3, 1], [4, 6], [3, 2], [1, 6]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# Convert 2D list to 3D at K slicing
# Using loop
res = []
subl = []
cnt = 0
for sub in test_list:
	subl.append(sub)
	cnt = cnt + 1
	if cnt >= K:
		res.append(subl)
		subl = []
		cnt = 0

# printing result
print("Records after conversion : " + str(res))
