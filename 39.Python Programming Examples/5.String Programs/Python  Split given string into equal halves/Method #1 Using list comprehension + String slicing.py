# Python3 code to demonstrate working of
# Splitting string into equal halves
# Using list comprehension + string slicing

# initializing string
test_str = "GeeksforGeeks"

# printing original string
print("The original string is : " + test_str)

# Using list comprehension + string slicing
# Splitting string into equal halves
res_first = test_str[0:len(test_str)//2]
res_second = test_str[len(test_str)//2 if len(test_str)%2 == 0
								else ((len(test_str)//2)+1):]

# printing result
print("The first part of string : " + res_first)
print("The second part of string : " + res_second)
