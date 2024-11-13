# Python3 code to demonstrate working of
# Rear Addition of Record
# using deque() + append()
from collections import deque

# Initializing list
test_list = [('is', 2), ('best', 3)]

# printing original list
print("The original list is : " + str(test_list))

# Initializing tuple to add
add_tuple = ('gfg', 1)

# Rear Addition of Record
# using deque() + append()
res = deque(test_list)
res.append(add_tuple)

# printing result
print("The tuple after adding is : " + str(list(res)))
