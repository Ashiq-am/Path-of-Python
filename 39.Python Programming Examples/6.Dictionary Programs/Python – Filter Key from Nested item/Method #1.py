# Python3 code to demonstrate working of
# Filter Key from Nested item
# Using loop + __contains__

# initializing dictionary
test_dict = {'gfg' : {'best' : 4, 'good' : 5},
			'is' : {'better' : 6, 'educational' : 4},
			'CS' : {'priceless' : 6},
			'Maths' : {'good' : 5}}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing dictionary
que_dict = {'good' : 5}

# Filter Key from Nested item
# Using loop + __contains__
res = []
for key, val in test_dict.items():
    if(test_dict[key].__contains__('good')):
        if(test_dict[key]['good'] == que_dict['good']):
            res.append(key)

# printing result
print("Match keys : " + str(res))
