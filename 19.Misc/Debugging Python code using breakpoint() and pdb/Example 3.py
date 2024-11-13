def debugger(a):
	import pdb; pdb.set_trace()
	result = [a[element] for element in range(0, len(a)+5)]
	return result

print(debugger([1, 2, 3]))
