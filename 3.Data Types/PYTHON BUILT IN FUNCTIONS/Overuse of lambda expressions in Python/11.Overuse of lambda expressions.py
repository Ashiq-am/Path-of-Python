details = [{'p':100, 'r':0.01, 'n':2, 't':4},
		{'p':150, 'r':0.04, 'n':1, 't':5},
		{'p':120, 'r':0.05, 'n':5, 't':2}]
sorted_details = sorted(details,
						key=lambda x: x['p']*((1 + x['r']/
								x['n'])**(x['n']*x['t'])))
print(sorted_details)
