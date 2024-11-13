# Python3 code to demonstrate working of
# Consecutive Repetition of Characters
# Using chain() + repeat()
from itertools import chain, repeat

# initializing list
test_list = ['g', 'f', 'g', 'i', 's', 'b', 'e', 's', 't']

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# Consecutive Repetition of Characters
# Using chain() + repeat()
res = list(chain.from_iterable(repeat(chr, K) for chr in test_list))

# printing result
print("The list after Consecutive Repetition is : " + str(res))
