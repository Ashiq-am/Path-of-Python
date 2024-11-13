from collections import deque

my_deque = deque()

try:
	result = my_deque.pop()
	print(result)
except IndexError:
	print('The deque is empty')
