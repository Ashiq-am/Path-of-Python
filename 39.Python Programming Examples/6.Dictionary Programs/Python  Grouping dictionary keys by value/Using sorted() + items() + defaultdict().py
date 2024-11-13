# Python3 code to demonstrate working of
# Grouping dictionary keys by value
# Using sorted() + items() + defaultdict()
from collections import defaultdict

# Initialize dictionary
test_dict = {'gfg': 1, 'is': 2, 'best': 1, 'for': 3, 'CS': 2}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Using sorted() + items() + defaultdict()
# Grouping dictionary keys by value
res = defaultdict(list)
for key, val in sorted(test_dict.items()):
    res[val].append(key)

# printing result
print("Grouped dictionary is : " + str(dict(res)))
