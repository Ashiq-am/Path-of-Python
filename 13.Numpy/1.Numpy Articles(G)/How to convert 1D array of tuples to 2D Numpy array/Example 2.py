import numpy as np

arr = [(1, 2, 3), ('Hi', 'Hello', 'Hey')]
x = []
for arrs in arr:
	items = []
	for item in arrs:
		items.append(item)
	x.append(items)

x = np.array(x)
print(x)
print(x.ndim)
