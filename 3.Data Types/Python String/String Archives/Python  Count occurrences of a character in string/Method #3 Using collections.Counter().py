# Python3 code to demonstrate
# occurrence frequency using
# collections.Counter()
from collections import Counter

# initializing string
test_str = "GeeksforGeeks"

# using collections.Counter() to get count
# counting e
count = Counter(test_str)

# printing result
print ("Count of e in GeeksforGeeks is : "
					+ str(count['e']))
