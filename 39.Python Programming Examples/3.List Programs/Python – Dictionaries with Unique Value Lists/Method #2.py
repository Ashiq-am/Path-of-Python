# Python3 code to demonstrate working of
# Unique Value Lists Dictionaries
# Using list comprehension

# initializing lists
test_list = [{'Gfg': [2, 3], 'is' : [7, 8], 'best' : [10]},
			{'Gfg': [2, 3], 'is' : [7], 'best' : [10]},
			{'Gfg': [2, 3], 'is' : [7, 8], 'best' : [10]}]

# printing original list
print("The original list : " + str(test_list))

# list comprehension to encapsulate logic in one liner
res = []
[res.append(val) for val in test_list if val not in res]

# printing result
print("List after duplicates removal : " + str(res))
