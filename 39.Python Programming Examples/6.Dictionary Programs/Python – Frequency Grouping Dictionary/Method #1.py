# Python3 code to demonstrate working of
# Frequency Grouping Dictionary
# Using defaultdict() + list comprehension
from collections import defaultdict

# initializing list
test_list = [{'Gfg' : 1, 'best' : 2},
			{'Gfg' : 1, 'best' : 2},
			{'Gfg' : 2, 'good' : 3},
			{'Gfg' : 2, 'best' : 2},
			{'Gfg' : 2, 'good' : 3}]

# printing original list
print("The original list is : " + str(test_list))

# Frequency Grouping Dictionary
# Using defaultdict() + list comprehension
temp = defaultdict(int)
for sub in test_list:
	key = sub['Gfg']
	temp[key] += 1

res = [{"Gfg": key, "freq": val} for (key, val) in temp.items()]

# printing result
print("The frequency dictionary : " + str(res))
