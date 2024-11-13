# Python3 code to demonstrate working of
# Check if Kth index elements are unique
# Using Counter() + all()
from collections import Counter

# initializing list
test_list = ["gfg", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# getting count of each Kth index item
count = Counter(sub[K] for sub in test_list)

# extracting result
res = all(val < 2 for val in count.values())

# printing result
print("Is Kth index all unique : " + str(res))
