def countList(lst):
	return sum(type(el)== type([]) for el in lst)
