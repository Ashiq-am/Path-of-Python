# Python3 code to demonstrate working of
# Convert dictionary string values to Dictionaries List
# Using loop
from collections import defaultdict

# initializing dictionary
test_dict = {"Gfg": "1:2:3:7:9", "best": "4:8", "good": "2"}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# create empty mesh
temp = defaultdict(dict)
for key in test_dict:

	# iterate for each of splitted values
	for idx in range(len(test_dict[key].split(':'))):
		try:
			temp[idx][key] = test_dict[key].split(':')[idx]

		# handle case with No value in split
		except Exception as e:
			temp[idx][key] = None

res = []
for key in temp:

	# converting nested dictionaries to list of dictionaries
	res.append(temp[key])

# printing result
print("Required dictionary list : " + str(res))
