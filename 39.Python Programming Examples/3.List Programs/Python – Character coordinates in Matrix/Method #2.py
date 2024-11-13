# Python3 code to demonstrate working of
# Character coordinates in Matrix
# Using regex() + loop
import re

# initializing list
test_list = ['23f45.;4d', '5678d56d', '789', '5678g']

# printing original list
print("The original list is : " + str(test_list))

# Character coordinates in Matrix
# Using regex() + loop
res = []
for key, val in enumerate(test_list):
    temp = re.search('([a-zA-Z]+)', val)
    if temp:
        res.append((key, temp.start()))

# printing result
print("Character indices : " + str(res))
