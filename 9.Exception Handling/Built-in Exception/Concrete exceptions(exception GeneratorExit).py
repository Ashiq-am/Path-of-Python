def my_generator():
	try:
		for i in range(5):
			print('Yielding', i)
			yield i
	except GeneratorExit:
		print('Exiting early')

g = my_generator()
print(g.next())
g.close()

