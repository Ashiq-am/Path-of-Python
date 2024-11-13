# Python3 program to show that
# a string can be appended to a string.

a = 'Geeks'

# output is displayed
print(a)
a = a + 'for'

print(a) # works fine










"""In the second program, interpreter makes a copy of the original string and then work on it and modifies it. 
So the expression a = a +’for’ doesn’t change string but reassigns the variable a to the new string generated 
by the result and drops down the previous string."""