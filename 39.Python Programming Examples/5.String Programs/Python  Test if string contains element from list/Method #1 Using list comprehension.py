# Python3 code to demonstrate
# checking if string contains list element
# using list comprehension

# initializing string
test_string = "There are 2 apples for 4 persons"

# initializing test list
test_list = ['apples', 'oranges']

# printing original string
print("The original string : " + test_string)

# printing original list
print("The original list : " + str(test_list))

# using list comprehension
# checking if string contains list element
res = [ele for ele in test_list if(ele in test_string)]

# print result
print("Does string contain any list element : " + str(bool(res)))
