# Python code to demonstrate
# converting 2d list into 1d list
# using list comprehension

# import chain
from itertools import chain

ini_list = [[1, 2, 3],
            [3, 6, 7],
            [7, 5, 4]]

# printing initial list
print("initial list ", str(ini_list))

# converting 2d list into 1d
# using list comprehension
flatten_list = [j for sub in ini_list for j in sub]

# printing flatten_list
print("final_result", str(flatten_list))
