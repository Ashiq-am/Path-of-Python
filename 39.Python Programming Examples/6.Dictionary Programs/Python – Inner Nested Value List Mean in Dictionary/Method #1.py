# Python3 code to demonstrate working of
# Inner Nested Value List Mean in Dictionary
# Using mean() + loop
from statistics import mean

# initializing dictionary
test_dict = {'Gfg' : {'a' : [1, 5, 6, 7], 'b' : [6, 7, 8, 9]}, 'is' : {'best' :[2, 8, 9, 0]}}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Inner Nested Value List Mean in Dictionary
# Using mean() + loop
for sub in test_dict.values():
	for key in sub:
		sub[key] = mean(sub[key])

# printing result
print("The modified dictionary : " + str(test_dict))
