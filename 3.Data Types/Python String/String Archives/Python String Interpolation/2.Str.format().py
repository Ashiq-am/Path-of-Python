# Python program to demonstrate
# string interpolation


n1 = 'Hello'
n2 ='GeeksforGeeks'

# for single substitution
print('Hello, {}'.format(n1))

# for single or multiple substitutions
# let's say b1 and b2 are formal parameters
# and n1 and n2 are actual parameters
print("{b1}! This is {b2}.".format(b1 = n1, b2 = n2))

# else both can be same too
print("{n1}! This is {n2}.".format(n2 = n2, n1 = n1))
