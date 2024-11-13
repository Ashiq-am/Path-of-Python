from collections import Counter

# initializing list
test_list = [{'gfg': 1, 'is': 4, 'best': 9},
			{'gfg': 6, 'is': 3, 'best': 8},
			{'gfg': 1, 'is': 4, 'best': 9},
			{'gfg': 1, 'is': 1, 'best': 9},
			{'gfg': 6, 'is': 3, 'best': 8}]

# printing original list
print("The original list is : " + str(test_list))

# getting frequencies
temp = Counter(tuple(sorted(sub.items())) for sub in test_list)

# converting back to Dictionaries
res = [(dict([tuple(ele) for ele in sub]), temp[sub]) for sub in temp]

# printing result
print("Dictionaries frequencies : " + str(res))
