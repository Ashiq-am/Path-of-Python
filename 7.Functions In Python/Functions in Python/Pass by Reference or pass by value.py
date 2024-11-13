# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20

# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)




"""When we pass a reference and change the received reference to something else, 
the connection between passed and received parameter is broken. For example, consider below program."""





def myFun(x):

# After below line link of x with previous
# object gets broken. A new object is assigned
# to x.
 x = [20, 30, 40]

# Driver Code (Note that lst is not modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)




"""Another example to demonstrate that reference link is broken if we assign a new value (inside the function)."""



def myFun(x):

# After below line link of x with previous
# object gets broken. A new object is assigned
# to x.
 x = 20

# Driver Code (Note that lst is not modified
# after function call.
x = 10
myFun(x)
print(x)





'''Exercise: Try to guess the output of following code.'''


def swap(x, y):
    temp = x
    x = y
    y = temp

# Driver code
x = 2
y = 3
swap(x, y)
print(x)
print(y)


