# Python3 code to demonstrate working
# of Extract string between 2 substrings
# Using index() + string slicing

# initializing string
test_str = "Gfg is best for geeks and CS"

# printing original string
print("The original string is : " + str(test_str))

# initializing substrings
sub1 = "is"
sub2 = "and"

# getting index of substrings
idx1 = test_str.index(sub1)
idx2 = test_str.index(sub2)

# length of substring 1 is added to
# get string from next character
res = test_str[idx1 + len(sub1) + 1: idx2]

# printing result
print("The extracted string : " + res)
