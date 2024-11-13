# Python3 code to demonstrate
# repeat element K times
# using itertools.chain.from_iterable() + itertools.repeat()
import itertools

# initializing list of lists
test_list = [4, 5, 6]

# printing original list
print("The original list : " + str(test_list))

# declaring magnitude of repetition
K = 3

# using itertools.chain.from_iterable()
# + itertools.repeat() repeat elements K times
res = list(itertools.chain.from_iterable(itertools.repeat(i, K)
										for i in test_list))

# printing result
print("The list after adding elements : " + str(res))
