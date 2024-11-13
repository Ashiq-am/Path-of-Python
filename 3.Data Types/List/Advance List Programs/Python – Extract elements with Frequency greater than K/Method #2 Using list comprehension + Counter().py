# Python3 code to demonstrate working of
# Extract elements with Frequency greater than K
# Using list comprehension + Counter()
from collections import Counter

# initializing list
test_list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]

# printing string
print("The original list : " + str(test_list))

# initializing K
K = 2

# using list comprehension to bind result
res = [ele for ele, cnt in Counter(test_list).items() if cnt > K]

# printing results
print("The required elements : " + str(res))
