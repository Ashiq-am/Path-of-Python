# Python3 code to demonstrate working of
# Dictionary initialization with common dictionary
# Using zip() + repeat()
from itertools import repeat

# initialization Dictionary
test_dict = {'gfg' : 1, 'best' : 3}

# Using zip() + repeat()
# Dictionary initialization with common dictionary
res = dict(zip(range(4), repeat(test_dict)))

# printing result
print("The dictionary with record values : " + str(res))
