# Python3 code to demonstrate
# append from front and remove from rear
# using collections.deque
from collections import deque

# initializing list
test_list = [4, 5, 7, 3, 10]

# printing original list
print("The original list : " + str(test_list))

# using collections.deque
# append from front and remove from rear
res = deque(test_list)
res.appendleft(13)
res.pop()
res = list(res)

# printing result
print("The list after append and removal : " + str(res))
