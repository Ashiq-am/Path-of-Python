# Python3 code to demonstrate
# Interlist Perfect Square Pairs
# using Counter() + set() + loop + product()
from itertools import product
from collections import Counter


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return Counter(factors)


# Initializing lists
test_list1 = [4, 5, 6, 7, 3, 4]
test_list2 = [6, 4, 2, 8, 9, 4]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Flatten List to individual elements
# using Counter() + set() + loop + product()
prime_fac = {idx: prime_factors(idx) for idx in set(test_list1) | set(test_list2)}
res = set()
for a, b in product(test_list1, test_list2):
    combined_counts = prime_fac[a] + prime_fac[b]
    if all(v % 2 == 0 for v in combined_counts.values()):
        res.add(tuple(sorted([a, b])))

# printing result
print("The perfect square pairs are : " + str(res))
