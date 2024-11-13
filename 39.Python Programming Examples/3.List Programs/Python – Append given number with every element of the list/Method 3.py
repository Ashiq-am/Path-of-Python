input = [1, 2, 3, 4, 5]
key = 7

result = []
for x, y in zip(input, [key]*len(input)):
	result.extend([x, y])

print(result)
