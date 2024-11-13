# Python3 code to demonstrate working of
# Dictionary values String Length Summation
# Using map() + len() + sum()

# initializing dictionary
test_dict = {'gfg': '2345',
             'is': 'abcde',
             'best': 'qwerty'}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Dictionary values String Length Summation
# Using map() + len() + sum()
res = sum(map(len, test_dict.values()))

# printing result
print("The string values length summation : " + str(res))
