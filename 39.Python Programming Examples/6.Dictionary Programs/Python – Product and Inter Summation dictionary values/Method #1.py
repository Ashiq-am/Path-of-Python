# Python3 code to demonstrate working of
# Product and Inter Summation dictionary values
# Using zip() + map() + sum() + loop

# helper function
def mul(sub):
    res = 1


    for ele in sub:
        res *= int(ele)

    return res

# initializing dictionary
test_dict = {'gfg' : [4, 5, 6], 'is' : [1, 3, 4], 'best' : [7, 8, 9]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Product and Inter Summation dictionary values
# Using zip() + map() + sum() + loop
temp = zip(*test_dict.values())
res = sum(map(mul, temp))

# printing result
print("The summations of product : " + str(res))
