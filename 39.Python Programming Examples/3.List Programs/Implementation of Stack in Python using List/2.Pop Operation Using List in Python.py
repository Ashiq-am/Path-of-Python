stack = []

def pop(stack):
	if len(stack) == 0:
		return None
	else:
		return stack.pop()

# Pushing the elements in the list
stack.append(1)
stack.append(2)
stack.append(3)

print("Initial Stack")
print(stack)

print("Popped Element: ", pop(stack))
