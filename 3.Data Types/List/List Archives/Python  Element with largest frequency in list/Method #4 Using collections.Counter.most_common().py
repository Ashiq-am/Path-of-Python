# Python3 code to demonstrate
# to get most frequent element
# using collections.Counter.most_common()
from collections import Counter

# initializing list
test_list = [9, 4, 5, 4, 4, 5, 9, 5, 4]

# printing original list
print("Original list : " + str(test_list))

# using most_common to
# get most frequent element
test_list = Counter(test_list)
res = test_list.most_common(1)[0][0]

# printing result
print("Most frequent number is : " + str(res))
