def sortList(lst):
	return sorted(lst, key = lambda x:(sum(map(int, str(x)))))
