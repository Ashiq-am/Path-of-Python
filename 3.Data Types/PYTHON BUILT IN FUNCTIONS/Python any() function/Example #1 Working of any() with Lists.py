# All elements of list are true
l = [ 4, 5, 1]
print(any( l ))

# All elements of list are false
l = [ 0, 0, False]
print(any( l ))

# Some elements of list are
# true while others are false
l = [ 1, 0, 6, 7, False]
print(any( l ))

# Empty List
l = []
print(any( l ))
