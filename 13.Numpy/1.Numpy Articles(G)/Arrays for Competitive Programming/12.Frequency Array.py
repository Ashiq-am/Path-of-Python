arr = [4, 2, 2, 5, 4, 4, 1, 5, 4]
hash_table = [0] * len(arr)

for element in arr:
	hash_table[element] += 1
