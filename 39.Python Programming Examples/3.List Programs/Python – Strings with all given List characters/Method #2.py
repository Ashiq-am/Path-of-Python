# Python3 code to demonstrate working of
# Strings with all List characters
# Using all() + list comprehension

# initializing list
test_list = ["Geeks", "Gfg", "Geeksforgeeks", "free"]

# printing original list
print("The original list is : " + str(test_list))

# initializing char_list
chr_list = ['g', 'f']

# using all() to check containment of all characters
res_list = [sub for sub in test_list if all(ele in sub for ele in chr_list)]

# printing results
print("Filtered Strings : " + str(res_list))
