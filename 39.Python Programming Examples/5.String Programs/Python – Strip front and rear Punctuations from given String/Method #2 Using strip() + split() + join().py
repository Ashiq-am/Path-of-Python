# Python3 code to demonstrate working of
# Strip Punctuations from String
# Using strip() + split() + join()
from string import punctuation

# initializing string
test_str = '%$Gfg is b !! est(*^&*'

# printing original string
print("The original string is : " + str(test_str))

# strip is used to remove rear punctuations
res = ' '.join([ele.strip(punctuation) for ele in test_str.split()])

# printing result
print("The stripped string : " + str(res))
