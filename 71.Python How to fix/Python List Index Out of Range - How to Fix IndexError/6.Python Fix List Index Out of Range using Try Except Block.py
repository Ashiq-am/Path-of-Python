my_list = [1, 2, 3]
try:
	print(my_list[3])
except IndexError:
	print("Index is out of range")
