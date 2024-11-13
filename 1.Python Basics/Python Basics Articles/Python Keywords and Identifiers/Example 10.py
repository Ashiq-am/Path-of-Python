def Generator():
	for i in range(6):
		yield i+1

t = Generator()
for i in t:
	print(i)
