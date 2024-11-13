# Python3 code to demonstrate working of
# Remove strings with any non-required character
# Using list comprehension + any()

# initializing list
test_list = ["gfg", "is", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# non-required char list
chr_list = ['f', 'm', 'n', 'i']

# checking for all strings
# removing if contains even 1 character
res = [sub for sub in test_list if not any(ele in sub for ele in chr_list)]

# printing result
print("Filtered Strings : " + str(res))
