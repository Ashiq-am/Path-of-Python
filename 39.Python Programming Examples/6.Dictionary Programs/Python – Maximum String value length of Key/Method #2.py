# Python3 code to demonstrate working of
# Maximum String value length of Key
# Using max() + len() + list comprehension (one liner)

# initializing list
test_list = [{'Gfg' : "abcd", 'best' : 2},
			{'Gfg' : "qwertyui", 'best' : 2},
			{'Gfg' : "xcvz", 'good' : 3},
			{'Gfg' : None, 'good' : 4}]

# printing original list
print("The original list is : " + str(test_list))

# initializing Key
filt_key = 'Gfg'

# Maximum String value length of Key
# Using max() + len() + list comprehension (one liner)
res = len(max(test_list, key = lambda sub: len(sub[filt_key])
				if sub[filt_key] is not None else 0)[filt_key])

# printing result
print("The maximum length key value : " + str(res))
