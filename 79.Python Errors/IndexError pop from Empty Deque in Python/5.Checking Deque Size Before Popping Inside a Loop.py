from collections import deque

my_deque = deque()

for _ in range(3):
	if my_deque:
		result = my_deque.pop()
		print(result)
	else:
		print('The deque is empty')
