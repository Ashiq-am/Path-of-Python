# Python3 code to demonstrate
# Get Kth element till N
# using map() + itemgetter() + islice()
from operator import itemgetter
from itertools import islice

# initializing list
test_list = [['Geeks', 1, 15], ['for', 3, 5], ['Geeks', 3, 7]]

# printing original list
print("The original list : " + str(test_list))

# initializing N
N = 2

# initializing K
K = 1

# using map() + itemgetter() + islice()
# Get Kth element till N
res = list(map(itemgetter(K), islice(test_list, 0, N)))

# print result
print("The Kth element of sublist till N : " + str(res))
