# Python3 code to demonstrate working of
# Values frequency across Dictionaries lists
# Using list comprehension + dictionary comprehension + count()

# initializing lists
test_list1 = [{"Gfg" : 6}, {"is" : 9}, {"best" : 10}]
test_list2 = [{"a" : 6}, {"b" : 10}, {"c" : 9}, {"d" : 6}, {"e" : 9}, {"f" : 9}]

# printing original list
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# extracting values from target dictionary
temp = [val for sub in test_list2 for key, val in sub.items()]

# frequency mapping from 1st dictionary keys
res = {key : temp.count(val) for sub in test_list1 for key, val in sub.items()}

# printing result
print("The frequency dictionary : " + str(res))
