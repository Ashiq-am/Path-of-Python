# Python code to demonstrate
# find average of similar tuples in list

# initialising list of tuples
ini_list = [('Akshat', 10), ('Garg', 10), ('Akshat', 2),
							('Garg', 9), ('Akshat', 10)]

# finding average of similar entries
temp_dict = dict()

for tuple in ini_list:
	key, val = tuple
	temp_dict.setdefault(key, []).append(val)

result = []
for name, values in temp_dict.items():
	result.append((name, (sum(values)/len(values))))

# printing result
print("Resultant list of tuples: {}".format(result))
