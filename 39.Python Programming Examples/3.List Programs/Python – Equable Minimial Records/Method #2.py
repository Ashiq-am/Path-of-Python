# Python3 code to demonstrate working of
# Equable Minimial Records
# Using groupby() + filter() + lambda
from itertools import groupby

# initializing list
test_list = [('Gfg', 12, 5), ('is', 13, 6), ('best', 12, 2), ('CS', 13, 2)]

# printing original list
print("The original list is : " + str(test_list))

# initializing Equate index
eq_idx = 2

# initializing min index
min_idx = 3

# Equable Minimial Records
# Using groupby() + filter() + lambda
res = []
for k, val in groupby(test_list, lambda sub: sub[eq_idx - 1]):
    res.append(min(filter(lambda sub: sub[eq_idx - 1] == k, test_list),
                   key=lambda sub: sub[min_idx - 1]))
res = list(set(res))

# printing result
print("Equable Minimal Records : " + str(res))
