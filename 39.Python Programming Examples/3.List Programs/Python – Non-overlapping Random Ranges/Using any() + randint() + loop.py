# Python3 code to demonstrate working of
# Non-overlapping Random Ranges
# Using loop + any() + randint()
import random

# initializing N
N = 7

# initializing K
K = 5

# Non-overlapping Random Ranges
# Using loop + any() + randint()
tot = 10000
res = set()
for _ in range(N):

    temp = random.randint(0, tot - K)
    while any(temp >= idx and temp <= idx + K for idx in res):
        temp = random.randint(0, tot - K)

    res.add(temp)
res = [(idx, idx + K) for idx in res]

# printing result
print("The N Non-overlapping Random ranges are : " + str(res))
