l = [1, 2, 3] # define a list
l_iter = iter(l) # create list_iterator

while True:
	# item will be "end" if iteration is complete
	item = next(l_iter, "end")
	if item == "end":
		break
	print(item)
