# Python3 code to demonstrate working of
# Initialize common value to keys
# Using defaultdict()
from collections import defaultdict

# Initialize dictionary
test_dict = dict()

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Initialize common value to keys
# Using defaultdict()
res = defaultdict(lambda: 4, test_dict)
res_demo = res['Geeks']

# printing result
print("The value of key is : " + str(res_demo))
