# Python3 code to demonstrate working of
# Remove prefix strings from list
# using list comprehension + startswith()

# initialize list
test_list = ['xall', 'xlove', 'gfg', 'xit', 'is', 'best']

# printing original list
print("The original list : " + str(test_list))

# initialize prefix
pref = 'x'

# Remove prefix strings from list
# using list comprehension + startswith()
res = [ele for ele in test_list if not ele.startswith(pref)]

# printing result
print("List after removal of Kth character of each string : " + str(res))
