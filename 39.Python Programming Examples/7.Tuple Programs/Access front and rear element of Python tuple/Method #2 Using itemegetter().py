# Python3 code to demonstrate working of
# Accessing front and rear element of tuple
# using itemgetter()
from operator import itemgetter

# initialize tuple
test_tup = (10, 4, 5, 6, 7)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Accessing front and rear element of tuple
# using itemgetter()
res = itemgetter(0, -1)(test_tup)

# printing result
print("The front and rear element of tuple are : " + str(res))
