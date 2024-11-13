# Python code to demonstrate
# to remove trailing None
# elements from lists

from itertools import takewhile

# initialising lists
ini_list = [1, 2, 3, 4, None, 76, None, None, None]

# printing initial dictionary
print ("initial dictionary", str(ini_list))

# code toremove trailing None values
# from lists
res = ini_list[:-len(list(takewhile(lambda x: x == None,
								reversed(ini_list))))]
# printing result
print ("resultant list", str(res))
