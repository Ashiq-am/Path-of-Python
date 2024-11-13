# Python code explaining min() and max()
l = [{'name':'ramu', 'score':90, 'age':24},
	{'name':'golu', 'score':70, 'age':19}]

# here anonymous function takes item as an argument.
print(max(l, key = lambda item:item.get('age')))
