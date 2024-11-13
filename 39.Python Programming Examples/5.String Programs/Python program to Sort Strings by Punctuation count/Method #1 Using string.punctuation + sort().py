# Python3 code to demonstrate working of
# Sort Strings by Punctuation count
# Using string.punctuation + sort()
from string import punctuation


def get_pnc_count(strng):
    # getting punctuation count
    return len([ele for ele in strng if ele in punctuation])


# initializing list
test_list = ["gfg@%^", "is", "Best!", "fo@#r", "@#$ge24eks!"]

# printing original list
print("The original list is : " + str(test_list))

# performing inplace sort
test_list.sort(key=get_pnc_count)

# printing result
print("Sorted Strings list : " + str(test_list))
