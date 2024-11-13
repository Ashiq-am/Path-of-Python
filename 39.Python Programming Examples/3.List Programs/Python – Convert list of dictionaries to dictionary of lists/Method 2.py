# consider the list of dictionary
data = [{'manoj': 'java', 'bobby': 'python'},
		{'manoj': 'php', 'bobby': 'java'},
		{'manoj': 'cloud', 'bobby': 'big-data'}]

# convert into dictionary of list
# with list as values
print({key: [i[key] for i in data] for key in data[0]})
