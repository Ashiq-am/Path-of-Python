# Python3 code to demonstrate working of
# Multiple indices Replace in String
# Using list comprehension + join()

# initializing string
test_str = 'geeksforgeeks is best'

# printing original string
print("The original string is : " + test_str)

# initializing list
test_list = [2, 4, 7, 10]

# initializing repl char
repl_char = '*'

# Multiple indices Replace in String
# Using list comprehension + join()
temp = list(test_str)
res = [repl_char if idx in test_list else ele for idx, ele in enumerate(temp)]
res = ''.join(res)

# printing result
print("The String after performing replace : " + str(res))
