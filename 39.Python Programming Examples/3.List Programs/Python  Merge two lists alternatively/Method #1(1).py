def countList(lst1, lst2):
	return [item for pair in zip(lst1, lst2 + [0])
								for item in pair]
