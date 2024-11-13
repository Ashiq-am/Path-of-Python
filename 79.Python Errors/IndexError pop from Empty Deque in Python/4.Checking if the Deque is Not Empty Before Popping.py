from collections import deque

my_deque = deque()

if my_deque:
	result = my_deque.pop()
	print(result)
else:
	print('The deque is empty')
