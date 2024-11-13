# Python3 code to demonstrate working of
# Dictionary Key Value lists combinations
# Using product() + zip() + loop
from itertools import product

# initializing dictionary
test_dict = {"Gfg": [4, 5, 7],
             "is": [1, 2, 9],
             "Best": [9, 4, 2]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

temp = list(test_dict.keys())
res = dict()
cnt = 0

# making key-value combinations using product
for combs in product(*test_dict.values()):
    # zip used to perform cross keys combinations.
    res[cnt] = [[ele, cnt] for ele, cnt in zip(test_dict, combs)]
    cnt += 1

# printing result
print("The computed combinations : " + str(res))
