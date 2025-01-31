class stack:
	# Method for pushing data into stack
	def push(self, st, data):
		st.append(data)

	# Method for pop
	def pop(self, st):
		if len(st) > 0:
			ans = st.pop()
			print("Removed element from the st : ", ans)
		else:
			print("The stack is Empty")

	# Method to get top of stack
	def top(self, st):
		if len(st) > 0:
			return st[len(st) - 1]

	# Method to check stack is Empty or not
	def isEmpty(self, st):
		if len(st) == 0:
			return 1
		else:
			return 0

	# Method to get size of stack
	def size(self, st):
		return len(st)


# Creating Object of stack class
st = stack()


my_stack = ["Lokesh", "Diwakar", "Aniket", "Ritik"]

# Printing the stack
print(my_stack)

# Printing the size of stack
print(st.size(my_stack))

# Removing the element of stack
st.pop(my_stack)

# Printing the top element of stack
print("Top element in the stack : ", st.top(my_stack))

# Check stack is Empty or not
print(st.isEmpty(my_stack))

# Push element into stack
st.push(my_stack, "Vimal Kant")

# Stack after Push
print(my_stack)
