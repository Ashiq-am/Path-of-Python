# Python code to demonstrate range() vs xrange()
# on basis of operations usage

# initializing a with range()
a = range(1,6)

# initializing a with xrange()
x = range(1,6)

# testing usage of slice operation on range()
# prints without error
print ("The list after slicing using range is : ")
print (a[2:5])

# testing usage of slice operation on xrange()
# raises error
print ("The list after slicing using xrange is : ")
print (x[2:5])
