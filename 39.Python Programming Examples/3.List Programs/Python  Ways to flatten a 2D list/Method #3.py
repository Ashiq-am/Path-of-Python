# Python code to demonstrate
# converting 2d list into 1d list
# using functools.reduce

# import functools
from functools import reduce

ini_list = [[1, 2, 3],
            [3, 6, 7],
            [7, 5, 4]]

# printing initial list
print("initial list ", str(ini_list))

# converting 2d list into 1d
# using functools.reduce
flatten_list = reduce(lambda z, y: z + y, ini_list)

# printing flatten_list
print("final_result", str(flatten_list))
