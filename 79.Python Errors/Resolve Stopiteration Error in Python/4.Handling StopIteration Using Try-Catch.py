list1 = [1, 2, 3, 4, 5]
iterator = iter(list1)

while True:
	try:
		x = next(iterator)
		print(x)
	except StopIteration:
		break
