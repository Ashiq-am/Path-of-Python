# Python code to demonstrate working of
# Nth column Maximum in tuple list
# using imap() + max() + itemgetter()
from operator import itemgetter
from itertools import imap

# initialize list
test_list = [(5, 6, 7), (1, 3, 5), (8, 9, 19)]

# printing original list
print("The original list is : " + str(test_list))

# initialize N
N = 2

# Nth column Maximum in tuple list
# using imap() + max() + itemgetter()
idx = itemgetter(N)
res = max(imap(idx, test_list))

# printing result
print("Maximum of Nth Column of Tuple List : " + str(res))
