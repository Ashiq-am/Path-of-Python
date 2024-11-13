# Python3 code to demonstrate
# K occurrence element Test
# using next() + islice()
from itertools import islice

# initializing list
test_list = [1, 3, 5, 5, 4, 5]

# printing original list
print("The original list is : " + str(test_list))

# initializing k
k = 3

# initializing N
N = 5

# using next() + islice()
# K occurrence element Test
func = (True for i in test_list if i == N)
res = next(islice(func, k - 1, None), False)

# printing result
print("Does N occur K times ? : " + str(res))
