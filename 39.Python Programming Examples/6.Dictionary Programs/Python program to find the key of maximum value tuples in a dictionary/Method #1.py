# Python3 code to demonstrate working of
# Maximum tuple value key
# Using max() + values() + next()

# initializing dictionary
test_dict = {'gfg': ("a", 3), 'is': ("c", 9), 'best': (
	"k", 10), 'for': ("p", 11), 'geeks': ('m', 2)}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# getting maximum value
max_val = max(test_dict.values(), key=lambda sub: sub[1])

# getting key with maximum value using comparison
res = next(key for key, val in test_dict.items() if val == max_val)

# printing result
print("The maximum key : " + str(res))
