# Python3 code to demonstrate working of
# Each word frequency percentage
# Using combined one-liner
from collections import Counter

# initializing list
test_list = ["Gfg is best for geeks", "All love Gfg",
             "Gfg is best for CS", "For CS geeks Gfg is best"]

# printing original list
print("The original list is : " + str(test_list))

# mapping using Counter()
mappd = Counter(" ".join(ele for ele in test_list).split())

# getting share of each word
res = {key: val / sum(mappd.values()) for key,
                                          val in mappd.items()}

# printing result
print("Percentage share of each word : " + str(res))
