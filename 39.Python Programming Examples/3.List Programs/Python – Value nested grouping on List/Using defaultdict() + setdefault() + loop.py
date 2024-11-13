# Python3 code to demonstrate working of
# Value nested grouping on List
# Using loop + setdefault() + defaultdict()
from collections import defaultdict

# initializing list
test_list = [{ 'value' : 'Fruit'},
			{ 'tag' : 'Fruit', 'value' : 'mango'},
			{ 'value' : 'Car'},
			{ 'tag' : 'Car', 'value' : 'maruti'},
			{ 'tag' : 'Fruit', 'value' : 'orange'},
			{ 'tag' : 'Car', 'value' : 'city'}]


# printing original list
print("The original list is : " + str(test_list))

# Value nested grouping on List
# Using loop + setdefault() + defaultdict()
temp = defaultdict(dict)
res = {}
for sub in test_list:
	type = sub['value']
	if 'tag' in sub:
		tag = sub['tag']
		temp[tag].setdefault(type, temp[type])
	else:
		res[type] = temp[type]

# printing result
print("The dictionary after grouping : " + str(res))
