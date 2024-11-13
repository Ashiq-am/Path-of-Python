# Python3 code to demonstrate working of
# Trail and lead padding of strings list
# using list comprehension

# initialize list
test_list = ["a", "b", "c"]

# printing original list
print("The original list : " + str(test_list))

# initialize pad_str
pad_str = 'gfg'

# Trail and lead padding of strings list
# using list comprehension
res = [pad_str + ele + pad_str for ele in test_list]

# printing result
print("The String list after padding : " + str(res))
