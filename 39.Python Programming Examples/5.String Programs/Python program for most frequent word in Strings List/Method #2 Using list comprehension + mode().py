# Python3 code to demonstrate working of
# Most frequent word in Strings List
# Using list comprehension + mode()
from statistics import mode

# initializing Matrix
test_list = ["gfg is best for geeks", "geeks love gfg", "gfg is best"]

# printing original list
print("The original list is : " + str(test_list))

# getting all words
temp = [wrd for sub in test_list for wrd in sub.split()]

# getting frequency
res = mode(temp)

# printing result
print("Word with maximum frequency : " + str(res))
