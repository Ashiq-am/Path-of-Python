# Python program to illustrate
# importing list-like container with
# fast appends and pops on either end
from collections import deque
s = 'geek'

# make a new deque
d = deque(s)

# add a new entry to the right side
d.append('y')

# add a new entry to the left side
d.appendleft('h')
print(d)

d.pop() # return and remove the rightmost item

d.popleft() # return and remove the lefttmost item

# print list deque in reverse
print(list(reversed(d)))
