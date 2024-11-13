# Python code to demonstrate
# converting 2d list into 1d list
# using chain.from_iterables

# import chain
from itertools import chain

ini_list = [[1, 2, 3],
            [3, 6, 7],
            [7, 5, 4]]

# printing initial list
print("initial list ", str(ini_list))

# converting 2d list into 1d
# using chain.from_iterables
flatten_list = list(chain.from_iterable(ini_list))

# printing flatten_list
print("final_result", str(flatten_list))
