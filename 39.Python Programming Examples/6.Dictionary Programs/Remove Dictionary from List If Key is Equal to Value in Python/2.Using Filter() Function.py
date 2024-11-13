# Input
list_dictionary = [{'geeks':'geeks','letters':4},
					{'name':'gfg', 3:3},
					{'name':'geeksforgeek', 'letters':12}]

# Remove dictionaries where key is equal to value
result = list(filter(lambda d: not any(k == v for k, v in d.items()), list_dictionary))

# Output
print(result)
