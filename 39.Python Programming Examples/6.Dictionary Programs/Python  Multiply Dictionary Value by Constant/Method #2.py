# Python3 code to demonstrate working of
# Multiply Dictionary Value by Constant
# Using defaultdict()
from collections import defaultdict

# Initialize dictionary
test_dict = defaultdict(int)

# printing original dictionary
print("The original dictionary : " + str(dict(test_dict)))

# Initialize K
K = 5

# Using defaultdict()
# Multiply Dictionary Value by Constant
test_dict['best'] *= K

# printing result
print("Dictionary after the multiplication of key : " + str(dict(test_dict)))
