# Python3 code to demonstrate
# converting string list to integer list
# using list comprehension + map()

# initializing list
test_list = [['24'], ['45'], ['78'], ['40']]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + map()
# converting string list to integer list
res = [list(map(int, list(sub[0]))) for sub in test_list if sub ]

# print result
print("The list after conversion : " + str(res))
