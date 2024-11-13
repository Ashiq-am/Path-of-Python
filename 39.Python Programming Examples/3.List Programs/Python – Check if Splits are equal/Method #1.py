# Python3 code to demonstrate working of
# Check if Splits are equal
# Using set() + len() + split()

# initializing string
test_str = '45# 45# 45# 45# 45'

# printing original string
print("The original string is : " + str(test_str))

# initializing splt_chr
splt_chr = "#"

# checking for length of set obtained, res stores boolean result
res = len(list(set(test_str.split(splt_chr)))) == 1

# printing result
print("Are all splits equal ? : " + str(res))
