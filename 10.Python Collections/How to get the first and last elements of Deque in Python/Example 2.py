# importing the module
from collections import deque

# creating a deque
dq = deque(['Geeks', 'for', 'Geeks', 'is', 'good'])

# displaying the deque
print(dq)

# fetching and deleting the first element
print(dq.popleft())

# fetching and deleting the last element
print(dq.pop())

# displaying the deque
print(dq)
