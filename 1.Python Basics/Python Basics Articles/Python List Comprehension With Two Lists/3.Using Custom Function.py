list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]

def custom_function(a, b):
	return a**2 + b**2

result = [custom_function(a, b) for a, b in zip(list_a, list_b)]
print(result)
