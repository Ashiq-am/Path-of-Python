# Python3 code to demonstrate
# to add multiple similar values
# using extend() + itertools.repeat()
from itertools import repeat

# using extend() + itertools.repeat() to add multiple values
# adds 3, 50 times.
res = []
res.extend(repeat(3, 50))

# printing result
print ("The filtered list is : " + str(res))
