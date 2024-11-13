queue = ['first', 'second', 'third']
print(queue)

print()

# pushing elements
queue.append('fourth')
queue.append('fifth')
print(queue)
print()

# printing head
print(queue[0])

# printing tail
n = len(queue)
print(queue[n-1])
print()

# poping element
queue.remove(queue[0])
print(queue)
