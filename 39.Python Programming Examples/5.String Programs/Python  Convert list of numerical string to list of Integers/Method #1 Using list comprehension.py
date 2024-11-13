# Python3 code to demonstrate
# converting string list to integer list
# using list comprehension

# initializing list
test_list = [['24'], ['45'], ['78'], ['40']]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension
# converting string list to integer list
res = [[int(i) for i in sub] for i in test_list for sub in i]

# print result
print("The list after conversion : " + str(res))
