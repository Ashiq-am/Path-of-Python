# Python3 code to demonstrate working of
# Scoring Matrix using Dictionary
# Using list comprehension + sum()

# initializing list
test_list = [['gfg', 'is', 'best'], ['gfg', 'is', 'for', 'geeks']]

# printing original list
print("The original list is : " + str(test_list))

# initializing test dict
test_dict = {'gfg' : 5, 'is' : 10, 'best' : 13, 'for' : 2, 'geeks' : 15}

# Scoring Matrix using Dictionary
# Using list comprehension + sum()
res = [sum(test_dict[word] if word.lower() in test_dict else 0 for word in sub) for sub in test_list]

# printing result
print("The Row scores : " + str(res))
