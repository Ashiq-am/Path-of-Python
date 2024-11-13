# Python3 code to demonstrate
# getting sublist element till N
# using map() + itemgetter() + islice()
from operator import itemgetter
from itertools import islice

# initializing list
test_list = [['Geeks', 1, 15], ['for', 3, 5], ['Geeks', 3, 7]]

# printing original list
print("The original list : " + str(test_list))

# initializing N
N = 2

# using map() + itemgetter() + islice()
# getting sublist element till N
res = list(map(itemgetter(0), islice(test_list, 0, N)))

# print result
print("The first element of sublist till N : " + str(res))
