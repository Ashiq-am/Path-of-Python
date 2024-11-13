# Python3 code to demonstrate working of
# Remove Kth character from strings list
# using list comprehension + list slicing

# initialize list
test_list = ['akash', 'nikhil', 'manjeet', 'akshat']

# printing original list
print("The original list : " + str(test_list))

# initialize K
K = 3

# Remove Kth character from strings list
# using list comprehension + list slicing
res = [ele[:K] + ele[K + 1:] for ele in test_list]

# printing result
print("List after removal of Kth character of each string : " + str(res))
