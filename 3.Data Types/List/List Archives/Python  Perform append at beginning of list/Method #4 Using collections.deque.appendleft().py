# Python3 code to demonstrate
# to add element at beginning
# using collections.deque.pushleft()
from collections import deque

# initializing list
test_list = [1, 3, 4, 5, 7]

# printing initial list
print("Original list : " + str(test_list))

# using collections.deque.pushleft()
# to append at beginning
# append 6
test_list = deque(test_list)
test_list.appendleft(6)
test_list = list(test_list)

# printing resultant list
print("Resultant list is : " + str(test_list))
