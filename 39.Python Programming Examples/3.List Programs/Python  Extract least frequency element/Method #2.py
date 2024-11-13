# Python3 code to demonstrate working of
# Extract least frequency element
# using Counter()
from collections import Counter

# initialize list
test_list = [1, 3, 4, 5, 1, 3, 5]

# printing original list
print("The original list : " + str(test_list))

# Extract least frequency element
# using Counter
res = Counter(test_list)
tar_ele = res.most_common()[-1][0]

# printing result
print("The minimum occurring element is : " + str(tar_ele))
