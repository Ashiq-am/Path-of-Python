# Python3 code to demonstrate
# joining only adjacent words in list
# list comprehension + "*" operator

# initializing list
test_list = ['Geeks', '5', 'for', '9', 'Geeks' , '2', '5']

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + "*" operator
# joining only adjacent words in list
res = [''.join([i for i in test_list if not i.isdigit()]),
				*[j for j in test_list if j.isdigit()]]

# print result
print("The joined adjacent word list(ignoring digits) : " + str(res))
