# Python3 code to demonstrate
# List extension by K
# using itertools.chain() + itertools.tee() + zip()
from itertools import chain, tee

# initializing list
test_list = [4, 5, 2, 8]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 3

# using itertools.chain() + itertools.tee() + zip()
# to extend list
res = list(chain(*zip(*tee(test_list, K))))

# printing result
print("The resultant list after extension is : " + str(res))
