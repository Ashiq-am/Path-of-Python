# Python3 code to demonstrate working of
# Distinct Positive Integers Sum to K
# Using combinations() + sum()
from itertools import combinations

# initializing K
K = 19

# printing K
print("The value of K : " + str(K))

res = []
flag = 0
for idx in range(K - 1, 0, -1):

    # forming combinations
    for sub in combinations(range(1, K), idx):
        if sum(sub) == K and flag == 0:
            res.extend(list(sub))
            flag = 1
            break
        else:
            continue
        break

# printing result
print("The Required elements : " + str(res))
