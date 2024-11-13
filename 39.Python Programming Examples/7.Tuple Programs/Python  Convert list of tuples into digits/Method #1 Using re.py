# Python code to convert list of tuples into
# list of all digits which exists
# in elements of list.

# Importing
import re

# Input list initialization
lst = [(11, 100), (22, 200), (33, 300), (44, 400), (88, 800)]

# Using re
temp = re.sub(r'[\[\]\(\), ]', '', str(lst))

# Using set
Output = [int(i) for i in set(temp)]

# Printing output
print("Initial List is :", lst)
print("Output list is :", Output)
