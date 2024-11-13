# initializing list
test_list = [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1]

# printing original list
print("The original list is : " + str(test_list))

# initializing N
N = 3

res = []
for idx in range(0, len(test_list) // N):

	# getting incremented chunks
	res.append(test_list[0: (idx + 1) * N])

# printing result
print("Constructed Chunk Matrix : " + str(res))
