# Python3 code to demonstrate
# Chunked interleave of Lists
# using loop + extend()

# Initializing lists
test_list1 = [4, 5, 6, 8, 10, 11]
test_list2 = [6, 7, 8, 9, 8, 12]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Initializing step
step = 3

# Chunked interleave of Lists
# using loop + extend()
num = len(test_list1)
iters = int(num / step) + 1
res = []
for idx in range(iters):
	start = step * idx
	end = step * (idx + 1)
	res.extend(test_list1[start : end])
	res.extend(test_list2[start : end])

# printing result
print ("List after chunked merge : " + str(res))
