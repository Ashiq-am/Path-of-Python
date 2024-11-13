# Create an empty stack
stack = []

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
# Display the top of the stack
print("Top of Stack:", stack[-1])
# insert an element

stack.append(4)

# element inserted at the back
print("Top of Stack after inserting an element:", stack[-1])

# Display the stack
print("Stack:", stack)

popped_element = stack.pop()
print("Popped Element:", popped_element)

# Display the updated stack
print("Updated Stack:", stack)
