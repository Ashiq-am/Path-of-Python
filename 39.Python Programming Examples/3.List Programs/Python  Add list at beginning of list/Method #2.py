# Python3 code to demonstrate working of
# Adding list at beginning of list
# using deque.extendleft() + reversed()
from collections import deque

# initialize list
test_list = [1, 4, 5, 7, 6]

# initialize add list
add_list = [3, 4, 2, 10]

# printing original list
print("The original list is : " + str(test_list))

# printing add list
print("The add list is : " + str(add_list))

# Adding list at beginning of list
# using deque.extendleft() + reversed()
res = deque(test_list)
res.extendleft(reversed(add_list))

# printing result
print("The original updated list is : " + str(list(res)))
