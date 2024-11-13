# Input
list_dictionary = [{'geeks':'geeks','letters':4},
					{'name':'gfg', 3:3},
					{'name':'geeksforgeek', 'letters':12}]

# Remove dictionaries where key is equal to value
result = [d for d in list_dictionary if all(k != v for k, v in d.items())]

# Output
print(result)
