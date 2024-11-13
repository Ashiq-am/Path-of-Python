# Python3 code to demonstrate working of
# Maximum String value length of Key
# Using max() + len() + list comprehension

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
# Using max() + len() + list comprehension
temp = (sub[filt_key] for sub in test_list)
res = max(len(ele) for ele in temp if ele is not None)

# printing result
print("The maximum length key value : " + str(res))
