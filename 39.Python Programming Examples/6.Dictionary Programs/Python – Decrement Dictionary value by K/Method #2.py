# Python3 code to demonstrate working of
# Decrement Dictionary value by K
# Using defaultdict()
from collections import defaultdict

# Initialize dictionary
test_dict = defaultdict(int)

# printing original dictionary
print("The original dictionary : " + str(dict(test_dict)))

# Initialize K
K = 5

# Using defaultdict()
# Decrement Dictionary value by K
test_dict['best'] -= K

# printing result
print("Dictionary after the decrement of key : " + str(dict(test_dict)))
