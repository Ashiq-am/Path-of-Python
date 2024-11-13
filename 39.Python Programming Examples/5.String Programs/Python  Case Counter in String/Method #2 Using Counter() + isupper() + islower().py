# Python3 code to demonstrate working of
# Case Counter in String
# using Counter() + isupper() + islower()
from collections import Counter

# initializing string
test_str = "GFG is For GeeKs"

# printing original string
print("The original string is : " + test_str)

# Case Counter in String
# using Counter() + isupper() + islower()
res = Counter("upper" if ele.isupper() else "lower" if ele.islower()
			else " " for ele in test_str)

# printing result
print("The count of Upper case characters : " + str(res['upper']))
print("The count of Lower case characters : " + str(res['lower']))
