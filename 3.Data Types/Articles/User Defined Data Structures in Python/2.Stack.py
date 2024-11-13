stack = ['first', 'second', 'third']
print(stack)

print()

# pushing elements
stack.append('fourth')
stack.append('fifth')
print(stack)
print()

# printing top
n = len(stack)
print(stack[n-1])
print()

# poping element
stack.pop()
print(stack)
