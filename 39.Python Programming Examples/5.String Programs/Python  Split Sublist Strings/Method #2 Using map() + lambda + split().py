# Python3 code to demonstrate
# Split Sublist Strings
# using map() + lambda + split()

# initializing list
test_list = [['GfG is best'], ['All love Gfg'], ['Including me']]

# printing original list
print("The original list : " + str(test_list))

# using map() + lambda + split()
# Split Sublist Strings
res = list(map(lambda sub: sub[0].split(' '), test_list))

# print result
print("The list after splitting strings : " + str(res))
