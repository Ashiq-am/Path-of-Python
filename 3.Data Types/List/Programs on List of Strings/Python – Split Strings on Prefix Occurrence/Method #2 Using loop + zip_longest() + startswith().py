# Python3 code to demonstrate working of
# Split Strings on Prefix Occurrence
# Using loop + zip_longest() + startswith()
from itertools import zip_longest

# initializing list
test_list = ["geeksforgeeks", "best", "geeks", "and", "geeks", "love", "CS"]

# printing original list
print("The original list is : " + str(test_list))

# initializing prefix
pref = "geek"

res, temp = [], []

for x, y in zip_longest(test_list, test_list[1:]):
    temp.append(x)

    # if prefix is found, split and start new list
    if y and y.startswith(pref):
        res.append(temp)
        temp = []
res.append(temp)

# printing result
print("Prefix Split List : " + str(res))
