# Python3 code to demonstrate working of
# Equal character frequencies
# Using Counter() + loop
from collections import Counter

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# getting maximum frequency character
# using Counter()
freq_dict = Counter(test_str)
max_freq = test_str.count(max(freq_dict, key=freq_dict.get))

# equating frequencies
res = test_str
for chr in test_str:

    # if frequencies don't match max_freq
    if res.count(chr) != max_freq:
        res += chr * (max_freq - test_str.count(chr))

    # printing result
print("Equal character frequency String : " + str(res))
