# Python3 code to demonstrate working of
# Most common Combination in Matrix

# import required modules
from collections import Counter
from itertools import combinations

# initializing list
test_list = [[4, 5, 6, 2], [7, 6, 3, 2],
			[4, 2, 6, 7], [1, 2, 4, 6]]

# printing original list
print("The original list is : " + str(test_list))

res = Counter()
for sub in test_list:

	# ignoring 1 sized substring
	if len(sub) < 2:
		continue

	# sorting for common ordering
	sub.sort()

	# getting and storing combinations
	for size in range(2, len(sub) + 1):
		for comb in combinations(sub, size):
			res[comb] += 1

# getting most common combinations
res = [cmb for cmb,
	cnt in res.items() if cnt == res.most_common(1)[0][1]]

# printing result
print("The Most common combination : " + str(res))
