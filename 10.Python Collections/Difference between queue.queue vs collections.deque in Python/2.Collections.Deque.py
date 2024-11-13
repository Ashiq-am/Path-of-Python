# import module
from collections import deque

# initialise
dq = deque(['first','second','third'])
print(dq)
deque(['first', 'second', 'third'])

# adding more values
dq.append('fourth')
dq.appendleft('zeroth')
print(dq)
deque(['zeroth', 'first', 'second', 'third', 'fourth'])

# adding value to a specified index
dq.insert(0,'fifth')
print(dq)
deque(['fifth', 'zeroth', 'first', 'second', 'third', 'fourth'])

# removing values
dq.pop()
'fourth'
print(dq)
deque(['fifth', 'zeroth', 'first', 'second', 'third'])
dq.remove('zeroth')
print(dq)
deque(['fifth', 'first', 'second', 'third'])
