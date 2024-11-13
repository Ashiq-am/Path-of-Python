# Python3 code to demonstrate working of
# Adding tuple to front of list
# using deque() + appendleft()
from collections import deque

# Initializing list
test_list = [('is', 2), ('best', 3)]

# printing original list
print("The original list is : " + str(test_list))

# Initializing tuple to add
add_tuple = ('gfg', 1)

# Adding tuple to front of list
# using deque() + appendleft()
res = deque(test_list)
res.appendleft(add_tuple)

# printing result
print("The tuple after adding is : " + str(list(res)))
