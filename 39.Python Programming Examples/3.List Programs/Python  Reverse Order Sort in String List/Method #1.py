# Python3 code to demonstrate working of
# Reverse Order Sort in String List
# using list comprehension + sorted() + join() + reverse

# initialize list
test_list = ['gfg', 'is', 'good']

# printing original list
print("The original list : " + str(test_list))

# Reverse Order Sort in String List
# using list comprehension + sorted() + join() + reverse
res = [''.join(sorted(ele, reverse = True)) for ele in test_list]

# printing result
print("List after string reverse sorting : " + str(res))
