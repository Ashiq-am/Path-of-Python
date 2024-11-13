# Python3 code to demonstrate working of
# K sized N random elements
# Using generator + shuffle()
from random import shuffle


# get random list
def random_list(sub, K):
    while True:
        shuffle(sub)
        yield sub[:K]


# initializing list
test_list = [6, 9, 1, 8, 4, 7]

# initializing K, N
K, N = 3, 4

# printing original list
print("The original list is : " + str(test_list))

res = []
# getting N random elements
for idx in range(0, N):
    res.append(next(random_list(test_list, K)))

# printing result
print("K sized N random lists : " + str(res))
