mylist = []

try:
	res = mylist.pop()
	print(res)
except IndexError:
	print('The list is empty')
