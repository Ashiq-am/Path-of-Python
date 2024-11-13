# create an empty dictionary
dictionary_of_list = {}

# for loop to convert list of dict
# to dict of list
for item in data:
	name = item['name']
	dictionary_of_list[name] = item

# display
dictionary_of_list
