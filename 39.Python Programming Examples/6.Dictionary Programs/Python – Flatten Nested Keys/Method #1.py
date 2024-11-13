# Python3 code to demonstrate working of
# Flatten Nested Keys
# Using loop

# initializing list
test_list = [{'Gfg' : 1, 'id' : 1, 'data' : [{'rating' : 7, 'price' : 4},
			{'rating' : 17, 'price' : 8}]},
			{'Gfg' : 1, 'id' : 2, 'data' : [{'rating' : 18, 'price' : 19}]}]

# printing original list
print("The original list is : " + str(test_list))

# Flatten Nested Keys
# Using loop
res = []
for sub in test_list:
	temp1 = {
	'Gfg': sub['Gfg'],
	'id': sub['id']
	}
	for data in sub.get('data', []):
		res.append({
			**temp1,
			'rating': data['rating'],
			'price': data['price']})

# printing result
print("The flattened list : " + str(res))
