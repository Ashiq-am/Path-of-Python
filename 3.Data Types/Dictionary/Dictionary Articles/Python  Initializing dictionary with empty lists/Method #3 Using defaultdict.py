# Python3 code to demonstrate
# to initialize dictionary with list
# using defaultdict
from collections import defaultdict

# initializing dict with lists
new_dict = defaultdict(list)

# performing append
# shows no error
new_dict[0].append('GeeksforGeeks')

# printing result
print("New dictionary created : " + str(dict(new_dict)))
