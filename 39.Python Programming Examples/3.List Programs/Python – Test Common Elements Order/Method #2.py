# Python3 code to demonstrate
# Test Common Elements Order
# using list comprehension + set()

# Initializing lists
test_list1 = ['Gfg', 'is', 'for', 'Geeks']
test_list2 = [1, 'Gfg', 2, 'Geeks']

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Test Common Elements Order
# using list comprehension + set()
temp = set(test_list1) & set(test_list2)
temp1 = [val for val in test_list1 if val in temp]
temp2 = [val for val in test_list2 if val in temp]
res = temp1 == temp2

# printing result
print ("Are common elements in order ? : " + str(res))
