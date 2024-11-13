def generator_1():
	yield 1
	yield 2
	yield 3
	yield 4
	yield 5


for x in generator_1():
	print(x)
