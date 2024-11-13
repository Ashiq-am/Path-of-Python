stack = []
def is_empty():
	if len(stack) == 0:
		return 1
	else:
		return 0


# Pushing the elements in the list
stack.append(1)
stack.append(2)
stack.append(3)

print( is_empty())
