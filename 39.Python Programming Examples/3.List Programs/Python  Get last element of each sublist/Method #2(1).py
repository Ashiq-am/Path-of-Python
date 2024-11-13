def Extract(lst):
	return list(list(zip(*map(reversed, lst)))[0])
