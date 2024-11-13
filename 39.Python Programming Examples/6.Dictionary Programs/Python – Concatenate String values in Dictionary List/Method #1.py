# Python3 code to demonstrate working of
# Concatenate String values in Dictionary List
# Using loop

# initializing list
test_list = [{'gfg' : "geeksfor", 'id' : 12, 'best' : (1, 2)},
			{'gfg' : "geeks", 'id' : 12, 'best' : (6, 2)},
			{'gfg' : "good", 'id' : 34, 'best' : (7, 2)}]

# printing original list
print("The original list is : " + str(test_list))

# initializing compare key
comp_key = 'id'

# initializing concat key
conc_key = 'gfg'

# Concatenate String values in Dictionary List
# Using loop
res = []
for ele in test_list:
	temp = False
	for ele1 in res:
		if ele1[comp_key] == ele[comp_key]:
			ele1[conc_key] = ele1[conc_key] + ele[conc_key]
			temp = True
			break
	if not temp:
		res.append(ele)

# printing result
print("The converted Dictionary list : " + str(res))
