# Python3 code to demonstrate
# check for minimum N occureneces of K
# using next() + islice()
from itertools import islice

# initializing list
test_list = [1, 3, 5, 5, 4, 5]

# printing original list
print("The original list is : " + str(test_list))

# initializing k
k = 5

# initializing N
N = 3

# using next() + islice()
# checking occurrences of K atleast N times
func = (True for i in test_list if i == k)
res = next(islice(func, N - 1, None), False)

# printing result
print("Does %d occur atleast %d times ? :" % (k, N) + str(res))
