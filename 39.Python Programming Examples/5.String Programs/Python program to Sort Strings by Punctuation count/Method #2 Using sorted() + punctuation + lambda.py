# Python3 code to demonstrate working of
# Sort Strings by Punctuation count
# Using sorted() + punctuation + lambda
from string import punctuation

# initializing list
test_list = ["gfg@%^", "is", "Best!", "fo@#r", "@#$ge24eks!"]

# printing original list
print("The original list is : " + str(test_list))

# performing sort using sorted() with lambda
# function for filtering
res = sorted(test_list, key=lambda strng: len(
	[ele for ele in strng if ele in punctuation]))

# printing result
print("Sorted Strings list : " + str(res))
