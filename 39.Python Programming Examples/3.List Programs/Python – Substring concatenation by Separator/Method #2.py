# Python3 code to demonstrate working of
# Substring concatenation by Separator
# Using join() + split() + list comprehension

# initializing list
test_list = ['gfg', 'is', '*', 'best', '*', 'for', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = '*'

# Substring concatenation by Separator
# Using join() + split() + list comprehension
res = [ele for ele in ''.join(test_list).split(K) if ele]

# printing result
print("The list after String concatenation : " + str(res))
