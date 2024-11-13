def printdict(d):
	for key in d:
		print(key, "->", d[key])


hm = {0: 'first', 1: 'second', 2: 'third'}
printdict(hm)
print()

hm[3] = 'fourth'
printdict(hm)
print()

hm.popitem()
printdict(hm)
