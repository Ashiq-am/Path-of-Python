# Python3 code to demonstrate
# Flatten List to individual elements
# using chain() + isinstance()
from itertools import chain

# Initializing list
test_list = ['gfg', 1, [5, 6, 'geeks'], 67.4, [5], 'best']

# printing original list
print("The original list is : " + str(test_list))

# Flatten List to individual elements
# using chain() + isinstance()
res = list(chain(*[ele if isinstance(ele, list) else [ele] for ele in test_list]))

# printing result
print("The List after flattening : " + str(res))
