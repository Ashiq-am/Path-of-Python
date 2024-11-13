stack = []

def top():
	if len(stack) == 0:
		return None
	return stack[-1]


# Pushing the elements in the list
stack.append(1)
stack.append(2)
stack.append(3)

print("Top Element of Stack is : ", top())
