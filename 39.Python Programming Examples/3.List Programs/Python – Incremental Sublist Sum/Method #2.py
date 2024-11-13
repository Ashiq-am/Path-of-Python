# Python3 code to demonstrate
# Incremental Sublist Sum
# using itemgetter() + takewhile() + islice() + sum()
from itertools import islice, takewhile
from operator import itemgetter

# initializing list
test_list = [4, 7, 8, 10, 12, 15, 13, 17, 14, 5]

# printing original list
print("The original list : " + str(test_list))

# using itemgetter() + takewhile() + islice() + sum()
# Incremental Sublist Sum
temp = iter(test_list)
res = {key: val for key, val in takewhile(itemgetter(1), ((i, sum(list(islice(temp, i)))) for i in range(1, len(test_list))))}

# printing result
print("The Incremental Sublist Sum is : " + str(res))
