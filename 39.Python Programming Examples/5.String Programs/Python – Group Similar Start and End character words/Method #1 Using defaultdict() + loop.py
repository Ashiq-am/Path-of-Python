# Python3 code to demonstrate working of
# Group Similar Start and End character words
# Using defaultdict() + loop
from collections import defaultdict


def end_check(word):
    sub1 = word.strip()[0]
    sub2 = word.strip()[-1]
    temp = sub1 + sub2
    return temp


def front_check(word):
    sub = word.strip()[1:-1]
    return sub


# initializing string
test_str = 'geeksforgeeks is indias best and bright for geeks'

# printing original string
print("The original string is : " + str(test_str))

# Group Similar Start and End character words
# Using defaultdict() + loop
test_list = test_str.split()
res = defaultdict(set)
for ele in test_list:
    res[end_check(ele)].add(front_check(ele))

# printing result
print("The grouped dictionary is : " + str(dict(res)))
