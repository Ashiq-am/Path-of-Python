# Python3 code to demonstrate working of
# Associated Values Frequencies in Dictionary
# Using defaultdict() + Counter()
from collections import defaultdict, Counter

# initializing list
test_list = [{'gfg' : 1, 'is' : 3, 'best' : 4},
			{'gfg' : 3, 'is' : 2, 'best' : 4},
			{'gfg' : 3, 'is' : 5, 'best' : 2},
			{'gfg' : 5, 'is' : 2, 'best' : 1},
			{'gfg' : 2, 'is' : 4, 'best' : 3},
			{'gfg' : 1, 'is' : 3, 'best' : 5},
			{'gfg' : 1, 'is' : 3, 'best' : 2}]

# printing original list
print("The original list is : " + str(test_list))

# Associated Values Frequencies in Dictionary
# Using defaultdict() + Counter()
res = defaultdict(Counter)
for sub in test_list:
	for key, val in sub.items():
		res[key][val] += 1

# printing result
print("The list after Frequencies : " + str(dict(res)))
