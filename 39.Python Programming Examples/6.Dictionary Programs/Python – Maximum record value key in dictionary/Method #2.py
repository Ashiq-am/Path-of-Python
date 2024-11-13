# Python3 code to demonstrate working of
# Maximum record value key in dictionary
# Using max() + lambda function

# initializing dictionary
test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
			'is' : {'Manjeet' : 8, 'Himani' : 9},
			'best' : {'Manjeet' : 10, 'Himani' : 15}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing search key
key = 'Himani'

# Maximum record value key in dictionary
# Using max() + lambda function
res = max(test_dict, key = lambda sub: test_dict[sub][key])

# printing result
print("The required key is : " + str(res))
