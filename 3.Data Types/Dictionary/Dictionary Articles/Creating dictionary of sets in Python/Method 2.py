# import defaultdict module
from collections import defaultdict

# create an empty set of dictionary
dictionary = defaultdict(set)

# enter key value pair 1
dictionary["Student Roll-no"] |= {1, 2, 3, 4, 5}

# ennter key value pair 2
dictionary["Student Aadhar No"] |= {11, 22, 33, 44, 55}

# display
dictionary
