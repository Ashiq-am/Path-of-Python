# Python3 code to demonstrate working of
# Suffix removal from String list
# using list comprehension + endswith()

# initialize list
test_list = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']

# printing original list
print("The original list : " + str(test_list))

# initialize suff
suff = 'x'

# Suffix removal from String list
# using list comprehension + endswith()
res = [ele for ele in test_list if not ele.endswith(suff)]

# printing result
print("List after removal of suffix elements : " + str(res))
