# Sample list with duplicate strings
original_list = ['apple', 'orange', 'banana', 'apple', 'grape', 'banana']

# Remove duplicates using OrderedDict.fromkeys()
unique_list = list(dict.fromkeys(original_list))

print(unique_list)
