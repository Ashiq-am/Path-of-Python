# Python3 code to demonstrate working of
# Filter dictionaries with ordered values
# Using sorted() + values() + list comprehension

# initializing list
test_list = [{'gfg': 2, 'is': 8, 'good': 10},
			{'gfg': 1, 'for': 10, 'geeks': 9},
			{'love': 3, 'gfg': 4}]

# printing original list
print("The original list is : " + str(test_list))

# sorted to check with ordered values
# values() extracting dictionary values
res = [sub for sub in test_list if sorted(
	list(sub.values())) == list(sub.values())]

# printing result
print("The filtered Dictionaries : " + str(res))
