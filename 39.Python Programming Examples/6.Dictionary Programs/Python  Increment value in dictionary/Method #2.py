# Python3 code to demonstrate working of
# Increment value in dictionary
# Using defaultdict()
from collections import defaultdict

# Initialize dictionary
test_dict = defaultdict(int)

# printing original dictionary
print("The original dictionary : " + str(dict(test_dict)))

# Using defaultdict()
# Increment value in dictionary
test_dict['best'] += 3

# printing result
print("Dictionary after the increment of key : " + str(dict(test_dict)))
