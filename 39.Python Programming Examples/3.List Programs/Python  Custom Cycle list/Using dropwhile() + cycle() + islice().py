# Python3 code to demonstrate working of
# Custom Cycle list
# using dropwhile() + cycle() + islice()
import itertools

# initialize list
test_list = [3, 4, 5, 7, 1]

# printing original list
print("The original list is : " + str(test_list))

# initialize element for start cycle
K = 7

# initialize size of cycle list
N = 12

# Custom Cycle list
# using dropwhile() + cycle() + islice()
res = list(itertools.islice(itertools.dropwhile(lambda i: i != K, itertools.cycle(test_list)), N))

# printing result
print("The cycled list is : " + str(res))
