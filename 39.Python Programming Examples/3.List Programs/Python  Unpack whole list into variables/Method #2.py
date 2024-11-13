# Python3 code to demonstrate working of
# Unpack whole list into variables
# using Namedtuple
from collections import namedtuple

# initialize list
test_list = [1, 3, 7, 4, 2]

# printing original list
print("The original list is : " + str(test_list))

# Unpack whole list into variables
# using Namedtuple
temp = namedtuple("temp", "one two three four five")
res = temp(*test_list)

# printing result
print("Variables as assigned are : " + str(res.one) + " "
									+ str(res.two) + " "
									+ str(res.three) + " "
									+ str(res.four) + " "
									+ str(res.five))
