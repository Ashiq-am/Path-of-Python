# Python3 code to demonstrate working of
# Key with Maximum element at Kth index
# in Dictionary Value List Using sorted()
# + dictionary comprehension + lambda

# initializing dictionary
test_dict = {'Gfg': [4, 6],
			'is': [1, 4, 5, 9, 4, 5, 7],
			'best': [2, 3, 4, 10],
			'for': [4],
			'geeks': [2, 10, 1, 10]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 3

# sorted sorting all the values in reverse order
# Maximum element is found at 1st position
temp = sorted({key: val[K] if K <= len(val) else -1 for key,
			val in test_dict.items()}.items(),
			key=lambda sub: sub[1], reverse=True)

# getting all maximum keys in case of multiple
res = []
for idx, ele in enumerate(temp):
	res.append(temp[idx][0])
	if temp[idx][1] != temp[idx + 1][1]:
		break

# printing result
print("The extracted key : " + str(res))
