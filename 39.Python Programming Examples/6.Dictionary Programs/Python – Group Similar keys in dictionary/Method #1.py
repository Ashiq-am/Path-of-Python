# Python3 code to demonstrate working of
# Group Similar keys in dictionary
# Using loop

# initializing Dictionary
test_dict = {'gfg1' : 1, 'is1' : 2, 'best1' : 3,
			'gfg2' : 9, 'is2' : 8, 'best2' : 7,
			'gfg3' : 10, 'is3' : 5, 'best3' : 6}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Group Similar keys in dictionary
# Using loop
res = []
res1, res2, res3 = {}, {}, {}
for key, value in test_dict.items():

    if 'gfg' in key:
        res1[key] = value

    elif 'is' in key:
        res2[key] = value

    elif 'best' in key:
        res3[key] = value

res.append(res1)
res.append(res2)
res.append(res3)

# printing result
print("The grouped similar keys are : " + str(res))
