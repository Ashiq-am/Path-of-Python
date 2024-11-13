# Python3 code to demonstrate working of
# Initialize dictionary with None values
# Using zip() + repeat()
from itertools import repeat

# Using zip() + repeat()
# Initialize dictionary with None values
res = dict(zip(range(10), repeat(None)))

# printing result
print("The dictionary with None values : " + str(res))
