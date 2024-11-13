# Python3 code to demonstrate
# Alternate Element Repetition
# using itertools.chain.from_iterable() + itertools.repeat()
import itertools

# initializing list of lists
test_list = [4, 5, 6]

# printing original list
print("The original list : " + str(test_list))

# declaring magnitude of repetition
K = 3

# using itertools.chain.from_iterable() + itertools.repeat()
# Alternate Element Repetition
res = list(itertools.chain.from_iterable(itertools.repeat(ele, K) for idx, ele in enumerate(test_list) if idx % 2 == 0))

# printing result
print("The list after alternate repetition elements : " + str(res))
