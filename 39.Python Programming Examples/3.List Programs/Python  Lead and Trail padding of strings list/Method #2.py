# Python3 code to demonstrate working of
# Trail and lead padding of strings list
# using list comprehension + string formatting

# initialize list
test_list = ["a", "b", "c"]

# printing original list
print("The original list : " + str(test_list))

# initialize pad_str
pad_str = 'gfg'

# Trail and lead padding of strings list
# using list comprehension + string formatting
temp = pad_str + '{0}' + pad_str
res = [temp.format(ele) for ele in test_list]

# printing result
print("The String list after padding : " + str(res))
