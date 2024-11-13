# import gc module
import gc

# create list object
a = [1,2,3,4,5]
print(a)

# create a variable
b = 12
print(b)

# create tuple object
c = (1,2,3,4,5)
print(c)

# create a dictionary object
d = {'a':1, 'b':2}
print(d)

# get all the initialized objects
gc.get_objects()
