# Python3 code to demonstrate working of
# Sort Dictionary by Value Difference
# Using sorted() + lambda + abs() + dictionary comprehension

# initializing dictionary
test_dict = {'gfg' : [34, 87],
			'is' : [10, 13],
			'best' : [19, 27],
			'for' : [10, 50],
			'geeks' : [15, 45]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Sort Dictionary by Value Difference
# Using sorted() + lambda + abs() + dictionary comprehension
res = dict(sorted(test_dict.items(), key = lambda sub: abs(sub[1][0] - sub[1][1])))

# printing result
print("The sorted dictionary : " + str(res))
