# Python3 code to demonstrate working of
# Average String lengths in list
# using map() + sum() + len()

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# Average String lengths in list
# using map() + sum() + len()
res = sum(map(len, test_list))/float(len(test_list))

# printing result
print("The Average length of String in list is : " + str(res))
