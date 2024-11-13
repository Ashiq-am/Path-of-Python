# Python program to understand range
# this creates a list of 0 to 5
# integers

demo = range(6)

# print the demo
print(demo)

# it will generate error
print(next(demo))



'''Because range is iterable so we can get a iterator with the help of them but we 
can not directly call next in next. 
Below example explains it clearly'''





# Python program to understand range

# creates an iterator
demo = iter(range(6))

# print iterator
print(demo)

# use next
print(next(demo))
