# Python code to illustrate generator expression
generator = (num ** 2 for num in range(10))
for num in generator:
	print(num)
