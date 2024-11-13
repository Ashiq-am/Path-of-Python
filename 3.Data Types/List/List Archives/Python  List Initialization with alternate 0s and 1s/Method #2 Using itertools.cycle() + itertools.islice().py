# Python3 code to demonstrate
# to perform cyclic initialization
# using itertools.cycle() + itertools.islice()
import itertools

# count of 1
count_1 = 4

# count of 0
count_0 = 3

# total length of list
size = 16

# getting pattern
pattern = [1] * count_1 + [0] * count_0

# initializing list cyclically
# using itertools.cycle() + itertools.islice()
test_list = list(itertools.islice(itertools.cycle(pattern), size))

# printing list after change
print ("The list after initializing : " + str(test_list))
