def debugger(a, b):
	import pdb; pdb.set_trace()
	result = a / b
	return result

print(debugger(5, 0))
