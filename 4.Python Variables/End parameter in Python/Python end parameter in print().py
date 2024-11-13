'''By default python’s print() function ends with a newline. A programmer with C/C++ background may
wonder how to print without newline.

Python’s print() function comes with a parameter called ‘end’. By default, the value of this parameter is ‘\n’, i.e.
the new line character.
You can end a print statement with any character/string using this parameter.'''




# This Python program must be run with
# Python 3 as it won't work with 2.7.

# ends the output with a <space>
print("Welcome to" , end = ' ')
print("GeeksforGeeks", end = ' ')






'''One more program to demonstrate working of end parameter.'''





# This Python program must be run with
# Python 3 as it won't work with 2.7.

# ends the output with '@'
print("Python" , end = '@')
print("GeeksforGeeks")
