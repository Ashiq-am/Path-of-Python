# Python3 code to demonstrate working of
# Elements with K digit
# Using list comprehension + str()

# initializing list
test_list = [56, 72, 875, 9, 173]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 7

# extracting all elements with digit K using
# in operator after string conversion using str()
res = [ele for ele in test_list if str(K) in str(ele)]

# printing result
print("Elements with digit K : " + str(res))
