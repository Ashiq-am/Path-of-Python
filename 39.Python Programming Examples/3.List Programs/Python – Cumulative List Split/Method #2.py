# Python3 code to demonstrate working of
# Cummulative List Split
# Using accumulate() + join()
from itertools import accumulate

# initializing list
test_list = ['gfg-is-all-best']

# printing original list
print("The original list is : " + str(test_list))

# initializing Split char
spl_char = "-"

# Cummulative List Split
# Using accumulate() + join()
temp = test_list[0].split(spl_char)
res = list(accumulate(temp, lambda x, y: spl_char.join([x, y])))

# printing result
print("The Cummulative List Splits : " + str(res))
