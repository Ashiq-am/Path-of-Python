# Python3 code to demonstrate working of
# Split heterogenous type list
# using list comprehension + isinstance

# initialize list
test_list = ['gfg', 1, 2, 'is', 'best']

# printing original list
print("The original list : " + str(test_list))

# Split heterogenous type list
# using list comprehension + isinstance
res_str = [ele for ele in test_list if isinstance(ele, str)]
res_int = [ele for ele in test_list if isinstance(ele, int)]

# printing result
print("Integer list : " + str(res_int))
print("String list : " + str(res_str))
