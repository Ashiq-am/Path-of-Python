# Python3 code to demonstrate working of
# Sort Strings in String list
# using list comprehension + sorted() + join()

# initialize list
test_list = ['gfg', 'is', 'good']

# printing original list
print("The original list : " + str(test_list))

# Sort Strings in String list
# using list comprehension + sorted() + join()
res = [''.join(sorted(ele)) for ele in test_list]

# printing result
print("List after string sorting : " + str(res))
