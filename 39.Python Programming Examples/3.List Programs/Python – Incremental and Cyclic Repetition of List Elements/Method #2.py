# Python3 code to demonstrate
# Incremental and Cyclic Repetition of List Elements
# using cycle() + loop + zip()
from itertools import cycle

# Initializing list
test_list = ['g', 'f', 'g', 'C', 'S']

# printing original list
print("The original list is : " + str(test_list))

# Initializing range
i, j = 2, 4

# Incremental and Cyclic Repetition of List Elements
# using cycle() + loop + zip()
res = []
for k, l in zip(cycle(range(i, j + 1)), test_list):
    res.append(k * l)

# printing result
print("Repetition List is : " + str(res))
